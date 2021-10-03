##feature3
import sqlite3
from tabulate import tabulate
#import tabulate as tabulate

def keyword_Selection(var1, var2, var3):
    connection = sqlite3.connect("data/crashdb.db")
    list_column=[]
    list_values=[]

    cursor = connection.cursor()
    string = "SELECT * from CrashStatisticsVictoria where ACCIDENT_DATE>=:Start_date and ACCIDENT_DATE<=:End_date and UPPER(ACCIDENT_TYPE) like UPPER('%' || :keyword || '%') order by ACCIDENT_DATE"
    string1 = "PRAGMA TABLE_INFO(CrashStatisticsVictoria)"
    cursor.execute(string, {"Start_date": var1, "End_date": var2, "keyword": var3})
    result = cursor.fetchall()
    cursor.execute(string1)
    result1 = cursor.fetchall()


    for r in result1:
        list_column.append(r[1])

    for r in result:
        list_values.append(r)


    print(tabulate(list_values,headers=list_column))
    connection.close()

keyword_Selection('1/7/2017','1/7/2019','animal')

