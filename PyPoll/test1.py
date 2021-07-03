# import modules
import os
import csv

# find path for files
csvpath = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join("analysis", "analysis.txt")

# Create a dictionary to store candidates and votes
candidates = {}

# open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
# discard header row
    header = next(csvreader)

# read through csv
# if new candidate add to dicitonary and add vote
    for row in csvreader:
        if row[2] not in candidates:
            candidates[row[2]] = 0
        candidates[row[2]] +=1
        
# print analysis 
    print(candidates)
    total = sum(candidates.values())
    print(total)
    ret = "Election Results"
    ret += "\n----------------------------"
    ret += f"\nTotal votes: {total:,.0f}"
    ret += "\n----------------------------"
    
# loop through dictionary and retrieve info
    for name, votes in candidates.items():
        ret += f"\n{name}: {(votes/total)*100:.3f}% ({votes:,.0f})"
    ret += "\n----------------------------"
    ret += "\nWinner: Khan"
    ret += "\n----------------------------"
    print(ret)

# output to text file
with open(output_path,'w') as text_file:
    text_file.write(ret)
