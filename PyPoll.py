#The data we need to retrive
    #1. The total number of votes cast
    #2. A complete list of candidates who recived votes
    #3. The porcentage of votes each candidate won
    #4. The total number of votes each candidate won
    #5. The winner of the election based on popular vote

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Total votes variable
total_votes=0
candidate_options = []
candidate_votes = {}
i=0
winning_count=0
winning_porcetage=0


#open file
with open(file_to_load,"r") as election_data:
    file_reader = csv.reader(election_data)

    #To do -
   
    # Print the header row.
    headers = next(file_reader)
    #Loop over each row    
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

            
            
        candidate_votes[candidate_name] += 1


    #Structure of candidate-votes dictionary
    # candidate_votes = {"candidate_name1": votes, "candidate_name2": votes, "candidate_name3": votes}
        # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage}% of the vote.")

    
        if (votes > winning_count) and (vote_percentage > winning_porcetage):
            winning_count= votes
            winning_porcetage= vote_percentage
            winner = candidate_name
    
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

   


winning_candidate_summary = (
f"-------------------------\n"
f"Winner: {winner}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: { winning_porcetage:.1f}%\n"
f"-------------------------\n")
print(winning_candidate_summary)     

#1.- TOTAL VOTES        
#print(total_votes)
#print(candidate_options)
#print(candidate_votes)


 
