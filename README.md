# Election_Analysis

## Overview of Project
This analysis contains information on elections in 3 different counties in the United States, in which 3 candidates participated.

A python program was made to determine:
* 1.- The total number of votes.
* 2.- Automatically determine the number of participating candidates
* 3.- The number of votes per candidate.
* 4.- Automatically determine the number of counties contained in the database
* 5.- Number of votes per county.
* 6.- County with the most votes

## Election-Audit Results: 
*  ### How many votes were cast in this congressional election?
    - The fisrst task was to determinate the total number of votes, no matters by now, the number of candidates and counties in this election. in order to determine the total number of votes the followig code was used:

        "headers = next(file_reader)
        for row in file_reader:
            total_votes += 1
            candidate_name = row[2]"

    If we inspec the data, we can notice that the first row of the csv file is a Header row. in te previous code the "Next" function skips the firts row. 
    the "For" loop is used to loop over all rows in the file and add by 1 the "total_votes" variable to get the total number of votes. 

*  ### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
    - One challenge of this analysis was to determine the number of counties that contains the information within the csv file and then calculate the percentage of votes for each county.

        if voter_country not in countie_options:  
           countie_options.append(voter_country)
           countie_votes[voter_country] = 0
        countie_votes[voter_country] += 1

    An "If" function is used to determine if the list "countie_options" has already an element with the same name. if not, the "append" function will add it into the list and add +1 to this countie.

    Once the number of votes per countie is got, the percentage is calculated with the "total_votes" variable. 

        votes_by_countie_porcentage = float(votes_by_countie) / float(total_votes)*100  

*  ### Which county had the largest number of votes?
    - The algorith shows that the countie with the largest number of votes was: Denver
    - ![alt text](https://github.com/[dani1925]/[Election_Analysis]/blob/[main]/image1.JPG ?raw=true)


*  ### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received. 
    - Charles Casper Stockham recived : 23.0% (85,213)
    - Diana DeGette recived : 73.8% (272,892)
    - Raymon Anthony Doane recived : 3.1% (11,606)
*  ### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    - Winner: Diana DeGette
      Winning Vote Count: 272,892
      Winning Percentage: 73.8%


## Election-Audit Summary: 

In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.