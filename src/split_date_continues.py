#!/usr/bin/env python3

import pandas as pd


def split_date():
   df = pd.read_csv("src\Helsingin_pyorailijamaarat.csv", sep = ";")
    df = df.dropna(how = "all")
    df = df.dropna(axis = 1, how = "all")
    split_days = df["Päivämäärä"].str.split(expand = True)
    split_days.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    
    weekdays = {
        "ma":"Mon",
        "ti":"Tue",
        "ke":"Wed",
        "to":"Thu",
        "pe":"Fri",
        "la":"Sat",
        "su":"Sun"
    }
    
    months = {
        "tammi" : "1",
        "helmi" : "2",
        "maalis" : "3",
        "huhti" : " 4",
        "touko" : "5",
        "kesä" : "6",
        "heinä" : "7",
        "elo" : "8",
        "syys" : "9",
        "loka" : "10",
        "marras" : "11",
        "joulu" : "12"
    }
    split_days = split_days.replace(weekdays)
    split_days = split_days.replace(months)
    
    split_days["Hour"] = split_days["Hour"].str.slice(stop = 2)
    
    split_days = split_days.astype({"Month" : int, "Day" : int, "Year" : int, "Hour" : int})
    
    
    return split_days

def split_date_continues():
    pass

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
