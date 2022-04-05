# Final Deliverables / Pseudocode
 #1) Total number of votes cast
 #2) A complete list of candidates who received votes
 #3) Total number of votes each candidate received
 #4) Percentage of votes each candidate won
 #5) The winner of the election based on popular vote
# Import the datetime class from the datetime module

import datetime as dt
 # Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# print the present time.
print("The time right now is ", now)

import csv
dir(csv)

dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})

# Add our dependencies.
import csv
import os
# Assign a variable for the file to load from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
# To do: read and analyze the data here
 file_reader= csv.reader(election_data)

    # Read and print the header row.
 headers = next(file_reader)
 print(headers)

 # Print each row in the CSV file.
 for row in file_reader:
     print(row)

# Using the with statement open the file as a text file.
 with open(file_to_save, "w") as txt_file:
  # Write some data to the file.
    txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")  
