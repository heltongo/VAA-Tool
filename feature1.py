#feature 1
import sqlite3
from tabulate import tabulate

def date_Selection(var1, var2):
    list_column=[]
    list_values=[]
    connection = sqlite3.connect("Crashdb.db")
    cursor = connection.cursor()
    string = "SELECT * from CrashStatisticsVictoria where ACCIDENT_DATE>=:Start_date and ACCIDENT_DATE<=:End_date"
    string1 = "PRAGMA TABLE_INFO(CrashStatisticsVictoria)"
    cursor.execute(string, {"Start_date": var1, "End_date": var2})
    result = cursor.fetchall()
    cursor.execute(string1)
    result1 = cursor.fetchall()


    for r in result1:
        list_column.append(r[1])

    for r in result:
        list_values.append(r)


    print(tabulate(list_values,headers=list_column))
    connection.close()

date_Selection("var1", "var2")
# date_Selection('1/7/2016','1/7/2017')
# date_Selection('2016-07-01','2017-07-01')
