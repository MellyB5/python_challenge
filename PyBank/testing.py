import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
data_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    next_row = next(csvfile)

    last = 867884

    for row in csvreader:
        data = int(row[1]) - last
        data_list.append(data)
        last = int(row[1])
    print(data_list)

    ave = sum(data_list)/len(data_list)
    round_ave = round(ave, 2)
    print(f"Average Change: ${round_ave}")

    increase = max(data_list)
    decrease = min(data_list)
    print(f"Greatest Increase in Profits: (${increase})")
    print(f"Greatest Decrease in Profits: (${decrease})")