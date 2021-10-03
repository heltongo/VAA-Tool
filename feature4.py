#feature 4
import sqlite3
from tabulate import tabulate

def alcohol_Analysis():
    list_column=[]
    list_values=[]

    connection = sqlite3.connect("Crashdb.db")
    cursor = connection.cursor()
    #string = "SELECT * from CrashStatisticsVictoria where ACCIDENT_DATE>=:Start_date and ACCIDENT_DATE<=:End_date"
    string = "SELECT * from CrashStatisticsVictoria \
                WHERE ACCIDENT_DATE BETWEEN '2017-07-01' AND '2017-07-30'\
                ORDER BY ACCIDENT_DATE, ACCIDENT_TIME"
                # WHERE ACCIDENT_DATE between ('1/7/2017') and ('1/7/2019')"
    # WHERE ACCIDENT_DATE between Datetime('2009-11-13 00:00:00') and Datetime('2009-11-15 23:59:59')>=('1/7/2017') and ACCIDENT_DATE<=('1/7/2019')"
    #strftime('%Y-%m-%d', Date)
    string1 = "PRAGMA TABLE_INFO(CrashStatisticsVictoria)"
    # cursor.execute(string), {"Start_date": var1, "End_date": var2})
    cursor.execute(string)
    result = cursor.fetchall()
    cursor.execute(string1)
    result1 = cursor.fetchall()


    for r in result1:
        list_column.append(r[1])

    for r in result:
        list_values.append(r)


    print(tabulate(list_values,headers=list_column))
    connection.close()

alcohol_Analysis()
exit()