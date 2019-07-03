import csv
import os
csv_file = "budget_data.csv"

with open('budget_data.csv') as budget_data:
    readCSV = csv.reader(budget_data)

    next(readCSV)
    revenue = []
    date = []
    rev_change = []

    for row in readCSV:
        print("0: ", row[0],", 1:",row[1])
        revenue.append(float(row[1]))
        date.append(row[0])


print("Financial Analysis")
print("---------------------")
print("Total Months:", len(date))
print("Total Revenue: $", sum(revenue))

for i in range(1, len(revenue)):
    rev_change.append(revenue[i] - revenue[i - 1])
    avg_rev_change = sum(rev_change) / len(rev_change)

    max_rev_change = max(rev_change)

    min_rev_change = min(rev_change)

    max_rev_change_date = str(date[rev_change.index(max(rev_change))])
    min_rev_change_date = str(date[rev_change.index(min(rev_change))])


print("Average Revenue Change: $", round(avg_rev_change))
print("Greatest Increase in Revenue:", max_rev_change_date, "($", max_rev_change, ")")
print("Greatest Decrease in Revenue:", min_rev_change_date, "($", min_rev_change, ")")





