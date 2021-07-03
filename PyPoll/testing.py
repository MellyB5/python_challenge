import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')


Khan = 0
Correy = 0
Li = 0
OTooley = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    
    # header = next(csvreader)
    # print(header)

    for row in csvfile:
        row_list = row.split(sep=",")
        # print(row_list)
        if str(row_list[2][:-1]) == "Khan":
            Khan += 1
        elif str(row_list[2][:-1]) == "Correy":
            Correy += 1
        elif str(row_list[2][:-1]) == "Li":
            Li += 1
        elif str(row_list[2][:-1]) == "O'Tooley":
            OTooley += 1
    



    print(Khan)
    print(Correy)
    print(Li)
    print(OTooley)
    total_votes = Khan + Correy + Li + OTooley
    print(total_votes)

    print(f"Khan: {Khan/total_votes*100}% {(Khan)}")
    print(Correy/total_votes*100)
    print(Li/total_votes*100)
    print(OTooley/total_votes*100)
    print('---------------------------')
    print(f"Winner: Khan")
    print("---------------------------")
