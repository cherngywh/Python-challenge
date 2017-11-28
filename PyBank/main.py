import os
import csv

count = 0
total_revenue = 0
revenue_change = []

csvpath = os.path.join('resource', 'budget_data_1.csv')

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvreader = list(csvreader)
    for row in range(1, len(csvreader)):

        # Total Months
        count += 1

        # Total Revenue
        total_revenue += int(csvreader[row][1])
    for row in range(1, len(csvreader)-1):    

        # Average Revenue Change
        old_revenue = int(csvreader[row][1])
        new_revenue = int(csvreader[row+1][1])
        revenue_change.append(new_revenue-old_revenue)
        ave_change = round(sum(revenue_change) / len(revenue_change))

        # The greatest Increase/Decrease month
        max_change = max(revenue_change)
        min_change = min(revenue_change)
        max_index = revenue_change.index(max_change)
        min_index = revenue_change.index(min_change)
        max_month = max_index + 2
        min_month = min_index + 2

print ("Financial Analysis")
print ("----------------------------")
print ("Total Months:", count)
print ("Total Revenue: $" + str(total_revenue))
print ("Average Revenue Change: $" + str(ave_change))
print ("Greatest Increase in Revenue: ", csvreader[max_month][0], "($" + str(max_change) + ")")
print ("Greatest Decrease in Revenue: ", csvreader[min_month][0], "($" + str(min_change) + ")")





            




