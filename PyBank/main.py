# Solved HW Budget Data

# Approach is to create a third list with the monthly delta in Profit/Losses

import csv

month_date = []
monthly_profit = []
monthly_delta =[0]

with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Reading all columns into the lists
    for row in csvreader:
        month_date.append(row[0])
        monthly_profit.append(int(row[1]))

# Find Total Number of Months in Analysis
total_months = len(monthly_profit)
print("Total Months =",total_months)

# Find Total Net Profit in Analysis Period
Net_Profit = sum(monthly_profit)
print('{:,.2f}'.format(Net_Profit))

# Find the Largest Profit, Largest Loss, and Average Profit
Max_Profit = max(monthly_profit)
Min_Profit = min(monthly_profit)
Mean_Profit = Net_Profit/total_months

print('{:,.2f}'.format(Max_Profit))
print('{:,.2f}'.format(Min_Profit))
print('{:,.2f}'.format(Mean_Profit))

# Compute the Monthly Delta and Save into a New List
for x in range(1, total_months):
    delta = (monthly_profit[x]-monthly_profit[x-1])
    monthly_delta.append(delta)

# Find the Largest Monthly (+)Change, Largest Monthly (-)Change, Average Delta
Max_ProfitDelta = max(monthly_delta)
Min_ProfitDelta = min(monthly_delta)
deltamonths = len(monthly_delta)-1
print(deltamonths)
Mean_ProfitDelta = sum(monthly_delta)/deltamonths
print(Mean_ProfitDelta)

print('{:,.2f}'.format(Max_ProfitDelta))
print('{:,.2f}'.format(Min_ProfitDelta))

# Find the Date of the Largest Positive and Negative Monthly Delta
for x in range(1, total_months):
    if monthly_delta[x] == Max_ProfitDelta:
        MaxProfitDelta_Date = month_date[x]
    if monthly_delta[x] == Min_ProfitDelta:
        MinProfitDelta_Date = month_date[x] 

print("Max Profit Delta Date= ", MaxProfitDelta_Date)           
print("Min Profit Delta Date= ", MinProfitDelta_Date)

# Summarized Terminal Output

print("---------------------------------------------")
print("P&L High Level Summary Report")
print(" ")
print("---------------------------------------------")
print("Total Months =",total_months)
print("Total Net Profit =",'{:,.2f}'.format(Net_Profit))
print("Largest Monthly Profit =",'{:,.2f}'.format(Max_Profit))
print("Largest Monthly Loss =",'{:,.2f}'.format(Min_Profit))
print("Average Monthly Profit= ",'{:,.2f}'.format(Mean_Profit))
print(" ")
print("---------------------------------------------")
print("Largest Positive Monthly Change: ",'{:,.2f}'.format(Max_ProfitDelta)," Occured on: ", MaxProfitDelta_Date)
print("Largest Negative Monthly Change: ",'{:,.2f}'.format(Min_ProfitDelta)," Occurred on: ", MinProfitDelta_Date)
print("Average Monthly Change: ", Mean_ProfitDelta)
print(" ")
print("---------------------------------------------")

# Writing Results to a text file
with open('Financial_summary.txt','w') as f:
    f.write("P&L High Level Summary Report" + "\n" + "---------------------------------------" + "\n" 
    + "Number of Periods Analyzed:  " + str(total_months) + "\n"
    + "Total Net Profit:            " + str(Net_Profit) + "\n"
    + "Largest Monthly Profit:      " + str(Max_Profit) + "\n"
    + "Largest Monthly Loss:        " + str(Min_Profit) + "\n"
    + "Mean Monthly Profit:         " + str(Mean_Profit) + "\n"
    + " ---------------------------------------------------" + "\n"
    + "Largest Positive Profit Monthly Change: " + str(Max_ProfitDelta) + "   Occurred on " + str(MaxProfitDelta_Date) + "\n"
    + "Largest Negative Profit Monthly Change: " + str(Min_ProfitDelta) + "   Occurred on " + str(MinProfitDelta_Date) + "\n"
    + "            Mean Profit Monthly Change: " + str(Mean_ProfitDelta) + "\n"
    + " ---------------------------------------------------")

