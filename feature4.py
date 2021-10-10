#feature 4
import sqlite3
import matplotlib.pyplot as plt
from tabulate import tabulate
from data.db_utils import *
import pandas as pd

def alcoholAccidents():
    labels = []
    sizes = []
    var1 = '2014-01-01'
    var2 = '2018-12-31'

    connection = sqlite3.connect("data/crashdb.db")
    cursor = connection.cursor()
    string = "SELECT SEVERITY,COUNT(*) AS 'COUNT' FROM CrashStatisticsVictoria\
                   WHERE ALCOHOLTIME='Ýes' AND ACCIDENT_DATE>=:Start_date AND ACCIDENT_DATE<=:End_date \
                   GROUP BY SEVERITY"
    cursor.execute(string, {"Start_date": var1, "End_date": var2})
    result = cursor.fetchall()

    for r in result:
        labels.append(r[0])
        sizes.append(r[1])
    # Plot
    fig, ax1 = plt.subplots()
    ax1.pie(sizes, explode=(0, 0.1, 0, 0), labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()



def alcoholMonthlyAcc():
    list1 = []
    list2 = []
    var1 = '2014-01-01'
    var2 = '2018-12-31'

    connection = sqlite3.connect("data/crashdb.db")
    cursor = connection.cursor()
    string = "SELECT STRFTIME('%m', date(ACCIDENT_DATE)) AS MONTH_YEAR,COUNT(*) AS 'COUNT' FROM CrashStatisticsVictoria\
                WHERE ALCOHOLTIME='Yes' AND ACCIDENT_DATE between '2017-07-01' AND '2018-07-01' GROUP BY STRFTIME('%m', date(ACCIDENT_DATE)) "
    cursor.execute(string)
    result = cursor.fetchall()

    for r in result:
        list1.append(r[0])
        list2.append(r[1])

    plt.figure(figsize=(8, 5))
    plt.xlabel('Months of the year')
    plt.xticks(range(0, 12))
    plt.ylabel('Number of accidents')
    plt.title('Alcohol Analysis of Accidents')
    plt.plot(list1, list2)
    plt.show()


if __name__ == "__main__":
    #alcoholMonthlyAcc()
    alcoholAccidents()
    exit()