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

#open file
with open(file_to_load,"r") as electio_data:
    file_reader = csv.reader(electio_data)

    #To do -
   
    # Print the header row.
    headers = next(file_reader)
    print(headers)

 

 
