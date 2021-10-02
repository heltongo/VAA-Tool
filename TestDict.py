import csv
import os
import datetime
import sqlite3
import time

FILE_DIR = os.path.dirname(os.path.realpath(__file__))
FILE_NAME = "CrashStatisticsVictoria.csv"


def read_fom_db():
    connection = sqlite3.connect('crashdb.db')  # Connect to the database

    cursor = connection.cursor()

    records = cursor.execute("SELECT * FROM CrashStatisticsVictoria")

    connection.commit()
    connection.close()

    return records


def read_csv(file_name):
    """
    Creates a generator to improve memory usage
    :param file_name:
    :return:
    """
    for row in open(os.path.join(FILE_DIR, 'data', file_name), "r"):
        yield row


def manipulate_data(file_name):
    header = []
    results = {}

    try:
        count = 0
        for row in read_csv(file_name=file_name):
            try:
                count += 1
                values = row.rstrip('\n').split(',')

                if len(values) < 18:
                    raise Exception('There are missing values')

                if not header:
                    header = values
                    continue

                values_dict = {header[index]: values[index] for index in range(0, len(header))}
                yield values_dict

            except Exception as error:
                create_output_file(
                    error=True,
                    msg='Error row {0}: {1}'.format(
                        count,
                        error.message if hasattr(error, 'message') else error
                    )
                )

        create_output_file(results=results)

    except Exception as error:
        create_output_file(
            error=True, msg='Error row {0}: {1}'.format(
                0,
                error.message if hasattr(error, 'message') else error
            )
        )


# '1/7/2013'
def calculate_period(lower_date: str, higher_date: str):
    period = [
        data
        for data in manipulate_data(FILE_NAME)
        if lower_date <= data['ACCIDENT_DATE'] <= higher_date
    ]
    return period


def calculate_hour_day_crash(lower_date: str, higher_date: str, start_hour: str, end_hour):
    period = calculate_period(lower_date=lower_date, higher_date=higher_date)

    crashes_in_hour = [data for data in period if start_hour <= data['ACCIDENT_TIME'] <= end_hour]
    return crashes_in_hour


def calculate_type(lower_date: str, higher_date: str, crash_type: str):
    period = calculate_period(lower_date=lower_date, higher_date=higher_date)

    crash_type = [data for data in period if crash_type in data['ACCIDENT_TYPE']]

    return crash_type


def calculate_alcohol(lower_date: str, higher_date: str):
    type_alcohol = calculate_type(lower_date=lower_date, higher_date=higher_date, crash_type='alcohol')

    for data in type_alcohol:
        dict_to_return = {
            "gender": data['gender'],
            "year": data['gender'],
            "time": data['gender'],
            "Age": data['gender'],
            "Vehicle_Type": data['gender'],
            "road_type": data['gender'],
        }


def create_output_file(error=False, msg='', results={}):
    """
        Function to create a output log
        :param error:
        :param msg:
        :param results:
        :return: None
    """

    if not os.path.exists(os.path.join(FILE_DIR, 'data', 'output.csv')):
        new_file = open(os.path.join(FILE_DIR, 'data', 'output.csv'), mode='w+')
        new_file.close()

    with open(os.path.join(FILE_DIR, 'data', 'output.csv'), mode='r+') as output:

        csv_reader = csv.reader(output, delimiter=',')
        output_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        if not list(csv_reader):
            # write header
            output_writer.writerow(
                ['car_num', 'total_distance', 'operating_time', 'utilisation', 'avg_speed', 'num_trips', 'ERROR', 'MSG']
            )

        if not error:
            for key, value in results.items():
                output_writer.writerow(
                    [
                        key,
                        results[key].get('distance'),
                        results[key].get('duration_h'),
                        results[key].get('distance'),
                        results[key].get('speed_km_h_avg'),
                        results[key].get('num_trips'),
                        error,
                        msg
                    ]
                )
        else:
            output_writer.writerow(
                ['', '', '', '', '', '', error, msg]
            )


if __name__ == '__main__':
    calculate_period('1/7/2013', '1/7/2013')
    calculate_hour_day_crash
