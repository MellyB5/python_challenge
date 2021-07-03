import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join("analysis", "analysis.txt")

num_rows = 0
Khan = 0
Correy = 0
Li = 0
OTooley = 0

candididates = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
    header = next(csvreader)
    # first_row = next(csvreader)
    # num_rows += 1
    candididates2 = {}

    for row in csvreader:
        if row[2] not in candididates:
            candididates[row[2]] = 0
        candididates[row[2]] +=1
        if row[2] not in candididates2:
            candididates2[row[2]] = {}
        if row[1] not in candididates2[row[2]]:
            candididates2[row[2]][row[1]] = 0
        candididates2[row[2]][row[1]] +=1
        # num_rows += 1
        # if str(row[2]) == "Khan":
        #     Khan += 1
        # elif str(row[2]) == "Correy":
        #     Correy += 1
        # elif str(row[2]) == "Li":
        #     Li += 1
        # elif str(row[2]) == "O'Tooley":
        #     OTooley += 1
    
    print(candididates)
    print(candididates2)
    total = sum(candididates.values())
    print(total)
    ret = "Election Results"
    ret += "\n----------------------------"
    ret += f"\nTotal votes: {total:,.0f}"
    ret += "\n----------------------------"
    for name, votes in candididates.items():
        ret += f"\n{name}: {(votes/total)*100:.2f}% ({votes:,.0f})"
    ret += "\n----------------------------"
    print(ret)


#     total_votes = Khan + Correy + Li + OTooley
#     khan_votes = round((Khan/total_votes*100),3)
#     correy_votes = round((Correy/total_votes*100),3)
#     li_votes = round((Li/total_votes*100),3)
#     otooley_votes = round((OTooley/total_votes*100),3)
  

# # print analysis
#     analysis = (f"Election Results"
#     f"\n----------------------------"
#     f"\nTotal votes: {total_votes}"
#     "\n----------------------------"
#     f"\nKhan: {khan_votes}% ({Khan})"
#     f"\nCorrey: {correy_votes}% ({Correy})"
#     f"\nLi: {li_votes}% ({Li})"
#     f"\nO'Tooley: {otooley_votes}% ({OTooley})"
#     "\n----------------------------"
#     "\nWinner: Khan"
#     "\n----------------------------"
#     )
#     print(analysis)

# output analysis

with open(output_path,'w') as text_file:
    text_file.write(ret)
