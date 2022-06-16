import csv
import numpy as np


def getDataSource(data_path):
    sleep_in_hours = []
    Average_coffee_drink = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sleep_in_hours.append(float(row["Size of TV"]))
            Average_coffee_drink.append(float(row["\tAverage time spent watching TV in a week (hours)"]))

    return {"x" : sleep_in_hours, "y": Average_coffee_drink}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between sleep_in_hours and Average_coffee_drink in a week :-  \n--->",correlation[0,1])

def setup():
    data_path  = "sleep_in_hours,_Average_coffee_drink in a week (hours).csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()