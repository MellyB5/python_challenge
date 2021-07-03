# import modules
import os
import csv

# find the path
csvpath = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "analysis,txt")

# open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# discard header row
    csv_header = next(csvfile)
    
# declare variables
    last = 0
    count = 0
    total = 0
    # months = []
    max_increase = -99999999
    max_decrease = 99999999
    total_change = 0
    
# read through csv
# add to count of months
# find the change from one month to previous
# find the greatest increase and month
# find the greatest decrease and month
    for row in csvreader:
        total = total + int(row[1])
        count += 1
        if count>1:
            change = int(row[1]) - last
            total_change = total_change + change
            if change > max_increase:
                max_increase = change
                max_increase_month = row[0]
            if change < max_decrease:
                max_decrease = change
                max_decrease_month = row[0]

        last = int(row[1])
    
# print out results
    analysis = (f"""
Financial Analysis
----------------------------
Total Months: {count}
Total: ${total:,.0f}
Average  Change: ${total_change/(count-1):,.2f}
Greatest Increase in Profits: {max_increase_month} (${max_increase:,.0f})
Greatest Decrease in Profits: {max_decrease_month} (${max_decrease:,.0f})
""")
   
print(analysis)

# save to text file
with open(output_path, 'w') as text_file:
    text_file.write(analysis)

