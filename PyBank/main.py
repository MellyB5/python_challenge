import os
import csv
 
csvpath = os.path.join ("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

# read header row
csv_header = next(csvreader)
print(f"CSV Header: {csv_header}")

# count the number of rows
num_rows = 0

for row in open(csvpath):
    num_rows += 1
    print(f"Total months: {row}")

# find the net proft/loss
sum_pf = 0
for row in open(csvpath):
    sum_pf += row[1]
    print(f"Total: ${sum_pf}")


