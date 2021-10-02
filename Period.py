import sqlite3
from datetime import datetime


def period(lower_date, higher_date):
    connection = sqlite3.connect('crashdb.db')  # Connect to the database

    cursor = connection.cursor()

    records = cursor.execute(
        f"SELECT * "
        f"FROM CrashStatisticsVictoria "
        f"WHERE ACCIDENT_DATE >='{lower_date}' "
        f"AND ACCIDENT_DATE <='{higher_date}'"
    )

    for record in records:
        print(record[4])

    connection.commit()
    connection.close()


def accident_per_hour():
    connection = sqlite3.connect('crashdb.db')  # Connect to the database

    cursor = connection.cursor()

    records = cursor.execute("SELECT count(*) FROM CrashStatisticsVictoria")

    for record in records:
        datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
        print(record[4])

    connection.commit()
    connection.close()


if __name__ == '__main__':
    accident_per_hour()
    period(lower_date='1/7/2013', higher_date='1/7/2013')
