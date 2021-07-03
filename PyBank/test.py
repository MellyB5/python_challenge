import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
data_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    # next_row = next(csvfile)
    # print(type(next_row))
    last = 0
    count = 0
    total = 0
    months = []
    max_increase = -99999999
    min_increase = 99999999
    total_change = 0
    

    for row in csvreader:
        total = total + int(row[1])
        count += 1
        if count>1:
            change = int(row[1]) - last
            total_change = total_change + change
            if change > max_increase:
                max_increase = change
                max_increase_month = row[0]
            if change < min_increase:
                min_increase = change
                min_increase_month = row[0]

        # data_list.append(data)
        # months.append(row[0])

        last = int(row[1])
    # print(data_list)
    print(f"""
Financial Analysis
----------------------------
Total Months: {count}
Total: ${total:,.0f}
Average  Change: ${total_change/(count-1):,.2f}
Greatest Increase in Profits: {max_increase_month} (${max_increase:,.0f})
Greatest Decrease in Profits: {min_increase_month} (${min_increase:,.0f})
""")
    # ave = sum(data_list)/len(data_list)
    # round_ave = round(ave, 2)
    # print(f"Total: ${total}")

    # print(f"Average Change: ${round_ave}")

    # increase = max(data_list)
    # decrease = min(data_list)
    # increase_mont = months[data_list.index(increase)]
    # print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
    # print(f"Greatest Decrease in Profits: {min_increase_month} (${min_increase})")