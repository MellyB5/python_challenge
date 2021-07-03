import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join("analysis", "analysis.txt")

num_rows = 0
Khan = 0
Correy = 0
Li = 0
OTooley = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
    header = next(csvreader)
    # first_row = next(csvreader)
    # num_rows += 1

    for row in csvreader:
        num_rows += 1
        if str(row[2]) == "Khan":
            Khan += 1
        elif str(row[2]) == "Correy":
            Correy += 1
        elif str(row[2]) == "Li":
            Li += 1
        elif str(row[2]) == "O'Tooley":
            OTooley += 1
    

    
    total_votes = Khan + Correy + Li + OTooley
    khan_votes = round((Khan/total_votes*100),3)
    correy_votes = round((Correy/total_votes*100),3)
    li_votes = round((Li/total_votes*100),3)
    otooley_votes = round((OTooley/total_votes*100),3)
  

# print analysis
    analysis = (f"Election Results"
    f"\n----------------------------"
    f"\nTotal votes: {total_votes}"
    "\n----------------------------"
    f"\nKhan: {khan_votes}% ({Khan})"
    f"\nCorrey: {correy_votes}% ({Correy})"
    f"\nLi: {li_votes}% ({Li})"
    f"\nO'Tooley: {otooley_votes}% ({OTooley})"
    "\n----------------------------"
    "\nWinner: Khan"
    "\n----------------------------"
    )
    print(analysis)

# output analysis

with open(output_path,'w') as text_file:
    text_file.write(analysis)
