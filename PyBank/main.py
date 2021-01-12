# Python Challenge: PyBank
# Code by F. Barillas

# This challenges involves reading a csv file containing
# monthly P&L for a business.
# The required reporting includes:
#
# Total Number of Months in the Analyzed Period
# Total Net Profit
# The Average Monthly Change in Profits
# Date and Amount of the Larget Monthly Increase in Profits
# Date and Amount of the Largest Monthly Decrease in Profits
#
# As Additional Challenge the following additional metrics
# were calculated:
#
# Number of Months with Profit
# Number of Months with Loss
# Date and Amount of Largest Profit
# Date and Amoutn of the Largest Loss

# Reading the File

import os
import pandas as pd
import csv

profit_data = pd.read_csv(
    '/Users/Corsair_Barillas/Documents/FAB/Quant/UM Bootcamp/UM_Homework/HW3_Python/python-challenge/PyBank/Resources/budget_data.csv')

# Find the total number of Months in the Entire Period

Total_Months = profit_data['Date'].count()
print(Total_Months)

# Calculate Total Net Profit for the Entire Period

Total_NetProfit = profit_data['Profit/Losses'].sum()
print('{:,}'.format(Total_NetProfit))

# ADDITIONAL CALCULATION: Calculate Largest Profit in a Month

Max_MonthProfit = profit_data['Profit/Losses'].max()
print('{:,}'.format(Max_MonthProfit))

# ADDITIONAL CALCULATION: Calculate Largest Loss in a Month

Min_MonthProfit = profit_data['Profit/Losses'].min()
print('{:,}'.format(Min_MonthProfit))

# ADDITIONAL CALCULATION: Calculate Average Monthly Profit
Mean_MonthProfit = profit_data['Profit/Losses'].mean()
print('{:,}'.format(Mean_MonthProfit))

# Find the Change in Monthly Profit
monthly_delta = profit_data['Profit/Losses'].diff()
mean_profit_delta = monthly_delta.mean()

print(('{:,}'.format(mean_profit_delta))

# Find the largest monthly profit delta
largest_profit_delta = monthly_delta.max()

print('{:,}'.format(largest_profit_delta))

# Find the smalles monthly profit delta
smallest_profit_delta = monthly_delta.min()

print('{:,}'.format(smallest_profit_delta))

# Find the date of the largest monthly profit delta




# Find the date of the smalles monthly profit delta