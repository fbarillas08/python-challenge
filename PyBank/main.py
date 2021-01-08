# Python Challenge: PyBank
# Code by F. Barillas

# This challenges involves reading a csv file containing monthly P&L for a business.
# The required reporting includes:
#
# Total Number of Months in the Analyzed Period
# Total Net Profit
# The Average Monthly Change in Profits
# Date and Amount of the Larget Monthly Increase in Profits
# Date and Amount of the Largest Monthly Decrease in Profits
#
# As Additional Challenge the following additional metrics were calculated:
#
# Number of Months with Profit
# Number of Months with Loss
# Date and Amount of Largest Profit
# Date and Amoutn of the Largest Loss

# Reading the File

import os

import csv

csvpath = os.path.join('.','Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")

    print(csvreader)




