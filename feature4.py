#feature 4
import sqlite3
from tabulate import tabulate
from data.db_utils import *

def alcohol_Analysis():
    QUERY = "SELECT * from CrashStatisticsVictoria \
                WHERE ACCIDENT_DATE BETWEEN '2014-01-01' AND '2018-12-31' AND ALCOHOLTIME='Yes'\
                ORDER BY ACCIDENT_DATE, ACCIDENT_TIME"

    result = sql_data_to_list_of_dicts("Crashdb.db",QUERY)

    print(result)

    #print("Total records: ",count_keys(result))
    #print("First record date: ",result[0].get('ACCIDENT_DATE'))
    #print("Last record date: ",result[24530].get('ACCIDENT_DATE'))

#Finally :D


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