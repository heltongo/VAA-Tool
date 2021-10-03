import sqlite3

DB_NAME = 'crashdb.db'
TABLE_NAME = 'CrashStatisticsVictoria'


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

def test_Dictionary():
    QUERY = "SELECT * from CrashStatisticsVictoria"

    result = sql_data_to_list_of_dicts("Crashdb.db", QUERY)

    print("Total records: ",count_keys(result))
    print("First record date: ",result[0].get('ACCIDENT_DATE'))
    print("Last record date: ",result[74907].get('ACCIDENT_DATE'))

if __name__ == "__main__":
    test_Dictionary()
    exit()
