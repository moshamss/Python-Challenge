import os
import csv

data = os.path.join("budget_data.csv")
output_file = os.path.join("budget_output.txt")
months = 0
total = 0
month_change = []
change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 100000000000]

with open(data) as data:
    reader = csv.reader(data)
    header = next(reader)
    first_row = next(reader)
    total = total + int(first_row[1])
    previous = int(first_row[1])
    months = months + 1

    for row in reader:
        total = total + int(row[1])
        delta = int(row[1]) - previous
        previous = int(row[1])
        change = change + [delta]
        month_change = month_change + [row[0]]
        months = months + 1

        if delta > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = delta

        if delta < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = delta

average_change = sum(change)/len(change)
output = ("\n"
         f"Financial Analysis\n"
         f"------------------\n"
         f"Total Months: {months}\n"
         f"Total: ${total}\n"
         f"Average  Change: ${average_change:.2f}\n"
         f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
         f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
         )
print(output)
with open(output_file, "w") as output_file:
    output_file.write(output)
