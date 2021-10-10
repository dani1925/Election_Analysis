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

*  Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
*  Which county had the largest number of votes?
*  Provide a breakdown of the number of votes and the percentage of the total votes each candidate received. 
*  Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

## Election-Audit Summary: 

In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.