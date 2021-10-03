#feature 4
import sqlite3
from tabulate import tabulate


def sql_data_to_list_of_dicts(path_to_db, select_query):
    """Returns data from an SQL query as a list of dicts."""
    try:
        con = sqlite3.connect(path_to_db)
        con.row_factory = sqlite3.Row
        things = con.execute(select_query).fetchall()
        unpacked = [{k: item[k] for k in item.keys()} for item in things]
        return unpacked
    except Exception as e:
        print(f"Failed to execute. Query: {select_query}\n with error:\n{e}")
        return []
    finally:
        con.close()

def count_keys(dict):
    count = 0
    for i in enumerate(dict):
        count += 1
    return count



def alcohol_Analysis():
    QUERY = "SELECT * from CrashStatisticsVictoria \
                WHERE ACCIDENT_DATE BETWEEN '2014-01-01' AND '2018-12-31' AND ALCOHOLTIME='Yes'\
                ORDER BY ACCIDENT_DATE, ACCIDENT_TIME"

    result = sql_data_to_list_of_dicts("Crashdb.db", QUERY)

    print("Total records: ",count_keys(result))
    print("First record date: ",result[0].get('ACCIDENT_DATE'))
    print("Last record date: ",result[24530].get('ACCIDENT_DATE'))

#Finally  :D


# STOP
'''
#def calculate_alcohol(records):
    type_alcohol = calculate_type(lower_date=lower_date, higher_date=higher_date, crash_type='alcohol')

    for data in type_alcohol:
        records = {
            "gender": data['gender'],
            "year": data['gender'],
            "time": data['gender'],
            "Age": data['gender'],
            "Vehicle_Type": data['gender'],
            "road_type": data['gender'],
        }
'''
if __name__ == "__main__":
    alcohol_Analysis()
    exit()