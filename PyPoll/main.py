import csv

# Set the file path for the input and output files
input_file = "Resources/election_data.csv"

# Initialize variables to hold the vote count and candidate information
total_votes = 0
candidates = {}

# Read in the CSV file
with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    header = next(csvreader)
    
    # Iterate over each row in the CSV file
    for row in csvreader:
        # Increment the total vote count
        total_votes += 1
        
        # Get the candidate name from the row
        candidate_name = row[2]
        
        # If the candidate has not been added to the dictionary yet, add them with a vote count of 1
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        # If the candidate is already in the dictionary, increment their vote count
        else:
            candidates[candidate_name] += 1

# Determine the winner by finding the candidate with the most votes
winner = max(candidates, key=candidates.get)

# Print the results to the console
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
# Iterate over each candidate in the dictionary and print their name, vote percentage, and vote count
for candidate, votes in candidates.items():
    vote_percentage = round(votes / total_votes * 100, 3)
    print(f"{candidate}: {vote_percentage}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Open the output file

output_file = "analysis/election_results.txt"

with open(output_file, 'w') as outfile:
    # Print the results to the text file
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    # Iterate over each candidate in the dictionary and print their name, vote percentage, and vote count
    for candidate, votes in candidates.items():
        vote_percentage = round(votes / total_votes * 100, 3)
        outfile.write(f"{candidate}: {vote_percentage}% ({votes})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("-------------------------")

