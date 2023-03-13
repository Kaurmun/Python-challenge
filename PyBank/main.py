import csv

# Set the file path for the budget data CSV file
budget_data_path = "Resources/budget_data.csv"

# Initialize variables to store data
total_months = 0
total_profit = 0
previous_profit = 0
profit_change_list = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

# Open the CSV file using a context manager
with open(budget_data_path, newline='') as csvfile:
    # Use the csv.reader function to read the contents of the file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Count the number of months and add the profit/losses to the total
        total_months += 1
        total_profit += int(row[1])

        # Calculate the change in profit/losses
        current_profit = int(row[1])
        if previous_profit != 0:
            profit_change = current_profit - previous_profit
            profit_change_list.append(profit_change)

            # Determine the greatest increase and decrease in profit
            if profit_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = profit_change
            elif profit_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_change

        previous_profit = current_profit

# Calculate the average change in profit/losses
average_profit_change = sum(profit_change_list) / len(profit_change_list)

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_profit_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Open the output text file using a context manager
output_file_path = "analysis/budget_data_analysis.txt"
with open(output_file_path, 'w') as txtfile:
    # Write the results to the file using the write() function
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit}\n")
    txtfile.write(f"Average Change: ${average_profit_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
