import sqlite3

connection = sqlite3.connect('venv/Data/crashdata.db') # Connect to the database

cursor = connection.cursor()

records = cursor.execute("SELECT * FROM crashinfo Where ACCIDENT_DATE ='1/7/2013'")
for record in records:
    print(record)

connection.commit()
connection.close()