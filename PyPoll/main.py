import os
import csv

input_data = os.path.join("election_data.csv")
output_file = os.path.join("election_output.txt")
total = 0
vote = {}
candidate = []
winner_votes = 0
winner = ""

with open(input_data) as data:
    reader = csv.reader(data)
    header = next(reader)

    for row in reader:
        total = total + 1
        name = row[2]
        if name not in candidate:
            candidate.append(name)
            vote[name] = 0

        vote[name] = vote[name] + 1
        Results = (f"\n\nElection Results\n"
                   f"--------------------\n"
                   f"Total Votes: {total}\n"
                   f"--------------------\n")
    print(Results, end = "")

with open(output_file, "w") as output:
    output.write(Results)

    for candidate in vote:
        votes = vote.get(candidate)
        percent = float(votes)/float(total) * 100

        if (votes > winner_votes):
            winner = candidate
            winner_votes = votes

        vote_counts = f"{candidate}: {percent:.3f}% ({votes})\n"
        print(vote_counts, end = "")
        output.write(vote_counts)

        winner_result = (f"--------------------\n"
                         f"Winner: {winner}\n"
                         f"--------------------\n")
    print(winner_result, end = "")
    output.write(winner_result)
