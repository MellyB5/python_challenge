import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
data_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    next_row = next(csvfile)

    last = 867844

    for row in csvreader:
        data = int(row[1]) - last
        data_list.append(data)
        last = data
    print(data_list)

    ave = sum(data_list)/len(data_list)
    print(f"Average Change: ${ave}")

    increase = max(data_list)
    decrease = min(data_list)
    print(f"Greatest Increase in Profits: ")