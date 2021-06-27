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

    # for row in csvreader:
    #     pf.append(int(row[1])-int(row[1]-1)
    # print(pf)

    # lines = csvreader.readlines()
    # output = [0]
    # header = lines[0]
    # data = [int(number)] for number in lines[1:]]
    # for index, number in enumerate(data[1:],1):
    #     output.append(number-data[index-1])
    # print(output)



# find the net proft/loss
# sum_pf = 0
# for row in open(csvpath):
#     sum_pf += int(row[1])
# print(f"Total: $, {sum_pf}")

# # find the average, create a list of changes
# change_list = []
# for row in open(csvpath):
#     change_list.append()

# find the max


# find the min


# print to txt file