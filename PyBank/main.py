import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
num_rows = 0
net_total = 0
pf = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    first_row = next(csvreader)
    num_rows += 1
    net_total += int(first_row[1])
    
    for row in csvreader:
        num_rows += 1
        net_total += int(row[1])

    print(f"Total months: {num_rows}")
    print(f"Total: ${net_total}")


# print to txt file