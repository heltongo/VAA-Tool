import sqlite3

DB_NAME = 'crashdb.db'
TABLE_NAME = 'CrashStatisticsVictoria'


def execute_select_query(select_options: str, where_clause: str):
    connection = sqlite3.connect(DB_NAME)  # Connect to the database
    records = connection.cursor().execute(
        f"SELECT {select_options} "
        f"FROM {TABLE_NAME} "
        f"{where_clause}"
    )

    # connection.commit()
    connection.close()
    return records
