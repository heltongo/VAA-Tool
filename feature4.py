#feature 4
import sqlite3
from tabulate import tabulate

def alcohol_Analysis():
    list_column=[]
    list_values=[]

    connection = sqlite3.connect("Crashdb.db")
    cursor = connection.cursor()
    string = "SELECT * from CrashStatisticsVictoria \
                WHERE ACCIDENT_DATE BETWEEN '2017-07-01' AND '2017-07-30'\
                ORDER BY ACCIDENT_DATE, ACCIDENT_TIME"
    string1 = "PRAGMA TABLE_INFO(CrashStatisticsVictoria)"
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