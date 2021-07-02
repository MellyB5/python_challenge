import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# def print_votes(pypoll):
#     name = str(pypoll[2])
#     votes = int

Khan = 0
Correy = 0
Li = 0
OTooley = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
    header = next(csvreader)

    for row in csvfile:
        if str(row[2]) == "Khan":
            Khan += 1
        elif str(row[2]) == "Correy":
            Correy += 1
        elif str(row[2]) == "Li":
            Li += 1
        elif str(row[2]) == "O'Tooley":
            OTooley += 1
    
    print(Khan)
    total_votes = Khan + Correy + Li + OTooley
    print(total_votes)