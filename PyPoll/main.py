# Python Challenge: PyPoll
# Code by F. Barillas

# This exercise consists in reading a file containing the votes in a small town's election
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.


# Reading the csv file
import os
import csv
import collections

from collections import Counter

# Storage for computed data


candidate_list=[]
candidate_votes =[]

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Finding the List of Candidates

    for row in csvreader:
        candidate_votes.append(row[2])
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
    
# Find the Total Number of Votes Cast
Total_votes = (len(candidate_votes))        

# Find the votes per candidate
Votes_tally = Counter(candidate_votes)

# Find the Candidate With Most Votes
Votes_tally.most_common()
votes_winner = Votes_tally.most_common(1)[0][0]

# Define variables for each candidate tally
Kahn_votes = Votes_tally['Khan']
Correy_votes = Votes_tally['Correy']
Li_votes = Votes_tally['Li']
OTooley_votes = Votes_tally["O'Tooley"]

print("-----------------------------------------------------")
print("Election Results")
print("Candidates:",candidate_list)
print("-----------------------------------------------------")
print('Total Votes =','{:,}'.format(Total_votes))
print("-----------------------------------------------------")
print("   Votes for Khan =",'{:,}'.format(Votes_tally['Khan']),"Percent of Votes:",'{:.2f}'.format(Kahn_votes/Total_votes*100),"%")
print(" Votes for Correy =",'{:,}'.format(Votes_tally['Correy']),"  Percent of Votes:",'{:.2f}'.format(Correy_votes/Total_votes*100),"%")
print("     Votes for Li =",'{:,}'.format(Votes_tally['Li']), "  Percent of Votes:",'{:.2f}'.format(Li_votes/Total_votes*100),"%")
print("Votes for O'Tooley=",'{:,}'.format(Votes_tally["O'Tooley"]),"   Percent of Votes:",'{:.2f}'.format(OTooley_votes/Total_votes*100),"%")
print("")
print("-----------------------------------------------------")
print("Election Winner: ", votes_winner)
print("-----------------------------------------------------")
print("")

# Writing Results to a text file
with open('election_results.txt','w') as f:
    f.write("Election Results" + "\n"+ "-----------------------------" + "\n" + "Total Votes =  " +  str(Total_votes)+ "\n"
    + "----------------------------------"+ "\n"
    + "   Votes for Khan =" + str(Kahn_votes) + "   Percent of Votes="+ str(Kahn_votes/Total_votes*100) + "%" + "\n"
    + " Votes for Correy ="+ str(Correy_votes) + "   Percent of Votes="+ str(Correy_votes/Total_votes*100) + "%" +"\n"
    + "     Votes for Li =" + str(Li_votes) + "   Percent of Votes="+ str(Li_votes/Total_votes*100) + "%" +"\n"
    + "Votes for O'Tooley =" + str(OTooley_votes)+"   Percent of Votes="+ str(OTooley_votes/Total_votes*100) + "%" + "\n"
    +  "----------------------------------"+ "\n"
    + "Election Winner =  " + str(votes_winner) + "\n"
    + "----------------------------------"+ "\n" 
    )   
    f.close()