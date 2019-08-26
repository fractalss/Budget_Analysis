# Modules
import os
import csv

#Initialization 
count_months = 0
total_amount = 0
current_value = 0
last_value = 0
change = 0
change_total = 0
average_change = 0
greatest_increase_profits  = -1e+30
greatest_decrease_profits = 1e+30

# Set path for file
csvpath = os.path.join("budget_data.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    # Loop through the data 
    for row in csvreader:
        # Incrementing the count for months
        count_months = count_months + 1
        current_value = float(row[1])
        total_amount = total_amount + current_value
        # Finding the difference between current entry and last entry
        change = current_value - last_value
        # Set change to zero, for the first month
        if (count_months == 1):
            change = 0
        change_total = change_total + change
        # Finding the greatest value in change
        if (change > greatest_increase_profits):
            greatest_increase_profits = change
            month_of_greatest_increase = row[0]
        # Finding the smallest value in change
        if (change < greatest_decrease_profits):
            greatest_decrease_profits = change
            month_of_greatest_decrease = row[0]
        # Setting the current value to last entry before iterating
        last_value = current_value

    average_change = change_total/(count_months - 1)


# Printing out the analysis in terminal
print("Financial Analysis \n")
print("------------------------ \n")
print(f" Total Months : {count_months}\n")
print(f" Total : ${total_amount} \n")
print(" Average Change : $"+"{:.2f}".format(average_change)+"\n")
print(f" Greatest Increase in Profits : {month_of_greatest_increase}  (${greatest_increase_profits})\n")
print(f" Greatest Decrease in Profits : {month_of_greatest_decrease} (${greatest_decrease_profits})\n")

# Specify the file to write to
output_path = os.path.join( "analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as datafile:
    # Printing out the analysis in terminal
    datafile.write("Financial Analysis \n")
    datafile.write("------------------------ \n")
    datafile.write(f" Total Months : {count_months}\n")
    datafile.write(f" Total : ${total_amount} \n")
    datafile.write(" Average Change : $"+"{:.2f}".format(average_change)+"\n")
    datafile.write(f" Greatest Increase in Profits : {month_of_greatest_increase}  (${greatest_increase_profits})\n")
    datafile.write(f" Greatest Decrease in Profits : {month_of_greatest_decrease} (${greatest_decrease_profits})\n")

      



