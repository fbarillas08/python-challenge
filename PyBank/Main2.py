# Solved HW Budget Data

import csv

row_count = 0
total_sum = 0
total_change = 0
largest_increase = 0
largest_decrease = 0

with open('Resources/budget_data.csv','r') as my_data:
    reader = csv.reader(my_data)
    header = next(reader)

    first_row = next(reader)
    last_month_value = first_row[1]
    row_count += 1
    total_sum += int(first_row[1])


    for row in reader:
        monthly_change += int(row[1])-last_month_value
        total_change += monthly_change
        largest_increase = max(largest_increase, monthly_change)
        largest_decrease = min(largest_increase, monthly_change)

        row_count += 1
        total_sum += int(row[1])

        last_month_value = int(row[1])







