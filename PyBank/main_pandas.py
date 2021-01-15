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
    '/Users/Corsair_Barillas/Documents/FAB/Quant/UMBootcamp/UM_Homework/HW3_Python/python-challenge/PyBank/Resources/budget_data.csv')

# Find the total number of Months in the Entire Period

print("----------------------------------------------")
Total_Months = profit_data['Date'].count()
print("Total Months Evaluated:" , Total_Months)

#ADDITIONAL CALCULATION: Calculate the Number of Months with Positive Profit
Positive_Months = len(profit_data[profit_data['Profit/Losses']>0])
print("Profitable Months:", Positive_Months)

#ADDITIONAL CALCULATION: Calculate the Number of Months with Losses
Negative_Months = len(profit_data[profit_data['Profit/Losses']<0])
print("Lossing Months:",Negative_Months)
print("----------------------------------------------")

# Calculate Total Net Profit for the Entire Period

Total_NetProfit = profit_data['Profit/Losses'].sum()
print("Total Net Profit:",'{:,.2f}'.format(Total_NetProfit))

# ADDITIONAL CALCULATION: Calculate Largest Profit in a Month

Max_MonthProfit = profit_data['Profit/Losses'].max()
print("Largest Monthly Profit:",'{:,.2f}'.format(Max_MonthProfit))

# ADDITIONAL CALCULATION: Calculate Largest Loss in a Month

Min_MonthProfit = profit_data['Profit/Losses'].min()
print("Minimum Monthly Profit:",'{:,.2f}'.format(Min_MonthProfit))

# ADDITIONAL CALCULATION: Calculate Average Monthly Profit
Mean_MonthProfit = profit_data['Profit/Losses'].mean()
print("Average Monthly Profit:",'{:,.2f}'.format(Mean_MonthProfit))
print("----------------------------------------------")

# Find the Change in Monthly Profit
profit_data['monthly_delta'] = profit_data['Profit/Losses'].diff()
mean_profit_delta = profit_data['monthly_delta'].mean()

print("Average Change in Profit:",'{:,.2f}'.format(mean_profit_delta))

# Find the largest monthly profit delta

max_profit_delta = profit_data['monthly_delta'].max()
print("Largest Positive Change in Profit:",'{:,.2f}'.format(max_profit_delta))

# Find the smalles monthly profit delta

min_profit_delta = profit_data['monthly_delta'].min()
print("Largest Negative Change in Profit:", '{:,.2f}'.format(min_profit_delta))
print("----------------------------------------------")

maxprofitdelta_date = profit_data.loc[profit_data['monthly_delta']==max_profit_delta,"Date"]
print("Date of Largest Profit Delta:",maxprofitdelta_date)

minprofitdelta_date = profit_data.loc[profit_data['monthly_delta']==min_profit_delta,"Date"]
print("Date of Largest Loss Delta:", minprofitdelta_date)