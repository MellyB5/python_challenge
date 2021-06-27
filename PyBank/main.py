import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

# read header row
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # lines = len(list(csvreader))
    # print("Total months")
    # print(lines)



# count the number of rows
    num_rows = 0

    for row in open(csvpath):
        num_rows += 1
    print(f"Total months: {num_rows}")

# find the net proft/loss
sum_pf = 0
for row in open(csvpath):
    sum_pf += int(row[1])
print(f"Total: ${sum_pf}")

# # find the average, create a list of changes
# change_list = []
# for row in open(csvpath):
#     change_list.append()

# find the max


# find the min


# print to txt file
