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
file_to_save = os.path.join("election_results.txt")

# Total votes variables
total_votes=0
candidate_options = []
candidate_votes = {}

countie_options=[]
countie_votes={}

i=0
winning_count=0
winning_porcetage=0

winning_count_countie=0
winning_count_countie_porcetage = 0



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
        
        #Voter turnout for each county
        voter_country = row[1]

        if voter_country not in countie_options:
           countie_options.append(voter_country)
           countie_votes[voter_country] = 0
        
        countie_votes[voter_country] += 1
        


        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0


        candidate_votes[candidate_name] += 1

    with open(file_to_save,'w') as txt_file:
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(f"{election_results}\n")


      
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
            #print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")

        
            if (votes > winning_count) and (vote_percentage > winning_porcetage):
                winning_count= votes
                winning_porcetage= vote_percentage
                winner = candidate_name
        
            
            candidate_results = (f"{candidate_name} recived : {vote_percentage:.1f}% ({votes:,})")  
            print(candidate_results)
            txt_file.write(candidate_results +"\n")
        txt_file.write("------------------------------------- \n")
        print("------------------------------------")
        
       
       
        
        
        
       
        #txt_file.write(f"{candidate_results}\n") 
        
        txt_file.write("County Votes: \n")
        print("Countie Votes : \n" )
        for voter_country in countie_votes :
            votes_by_countie= countie_votes[voter_country]
            votes_by_countie_porcentage = float(votes_by_countie) / float(total_votes)*100 
        
            if (votes_by_countie > winning_count_countie) and (votes_by_countie_porcentage > winning_count_countie_porcetage):
                winning_count_countie=votes_by_countie
                winning_count_countie_porcetage = votes_by_countie_porcentage
                winning_countie =  voter_country
       
            countie_results = (f'{voter_country}   recibio : {votes_by_countie_porcentage:.2f} % con {votes_by_countie}  votos')
            
            #txt_file.write(f"{countie_results} \n")

           
            

            #COUNTY RESULTS 
            
            print(countie_results)
            txt_file.write(countie_results +"\n" )
            #txt_file.write(f"Largest Countie Turnout: {winning_countie}\n")

        print("-------------------\n")
        print("Largest County Turnout: " +winning_countie)
        print("-------------------\n")
        

       
       
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: { winning_porcetage:.1f}%\n"
        f"-------------------------\n")
        print(winning_candidate_summary)



        # Save the winning candidate's results to the text file.
        txt_file.write("-----------------------------\n")
        txt_file.write("Largest County Turnout: "+winning_countie +"\n")
        txt_file.write(winning_candidate_summary)
        
        #print(countie_votes)
  

    #1.- TOTAL VOTES        
    #print(total_votes)
    #print(candidate_options)
    #print(candidate_votes)


 
