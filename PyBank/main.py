import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
num_rows = 0
net_total = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    # print(row)
    header = next(csvreader)
    first_row = next(csvreader)
    num_rows += 1
    net_total += int(first_row[1])
    for row in csvreader:
        num_rows += 1
        net_total += int(row[1])

    print(num_rows)
    print(net_total)

        
    # count the number of rows
    # num_rows = 0

    # for row in open(csvpath):
    #     num_rows += 1
    # print(f"Total months: {num_rows}")

    # total_net = 0
    # for row in csvreader:
    #     total_net += int(row[1])
    # print(total_net)

#find the sum of p/f
    # pf = []
    # for row in open(csvpath):
    #     pf.append(row[1])
    # print(pf)
# total = sum(pf)
# print("Total $", total)




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
