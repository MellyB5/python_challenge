import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

num_rows = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
    header = next(csvreader)
    first_row = next(csvreader)
    num_rows += 1

    for row in csvreader:
        num_rows += 1
    
    print(f"Total votes: {num_rows}")
    