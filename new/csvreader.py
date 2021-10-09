import sys

import pandas as pd


def loadData(fileName):
    try:
        db = pd.read_csv(fileName)
        # Convert the Dates to the right format for our use
        db["ACCIDENT_DATE"] = pd.to_datetime(db["ACCIDENT_DATE"])
        return db
    except FileNotFoundError:
        # return Empty Dataframe...
        return pd.DataFrame({"A": []})


def validateData(db):
    if db.empty:
        print("The csv data is empty")
        sys.exit()


def clearData(treeView):
    treeView.delete(*treeView.get_children())
    return None
