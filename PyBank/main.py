#import the module used to read your csv
import pandas as pd

#my csv file location - C:/Users/tmlun/python-challenge/PyBank/Resources
budget_csv = "C:\\Users\\tmlun\\python-challenge\\PyBank\\Resources\\budget_data.csv"

#read csv and create DataFrame
mydf = pd.read_csv(budget_csv)

#count the total # of months in the dataset
Total_Months = mydf["Date"].count()

#Net total of the Profit/Losses column of dataset
Total = mydf["Profit/Losses"].sum()

#format the net total to currency without commas or decimals
Net_Total = '${:}'.format(Total)

#get the mean for the Profit/Losses column of dataset
    #identify the values in the column
Profit_Loss = mydf["Profit/Losses"].values

    #list to hold the values
profit = []

    #list to hold the monthly changes 
monthly_change = []

    #iterate through Profit_Loss to add to the profit list
for x in Profit_Loss:  
    profit.append(x)
    
    #iterate through Profit_Loss to add to the monthly_change list
for i in range(len(profit)-1):
    monthly_change.append(profit[i+1]-profit[i])
    
    #get the mean and round
Avg_change = round(sum(monthly_change)/85,2)

#format the mean to currency without commas and decimals
Average_Change = '${:}'.format(Avg_change)

#get the greatest increase in profits
Increase = max(monthly_change)

#format the greatest increase without commas or decimals
Greatest_Increase = '${:}'.format(Increase)

#need to find the date of the Greatest Increase with a df
Inc_Date = mydf[mydf["Profit/Losses"]==1170593]

#pull date out of df so only the Date can be printed
Great_Inc_Date = Inc_Date['Date']

#enter date in quotes so can be printed in output without extra "Name:, dtype"
Greatest_Inc_Date = "Feb-2012"

#get the greatest decrease in losses
Decrease = min(monthly_change)

#format the greatest decrease without commas or decimals
Greatest_Decrease = '${:}'.format(Decrease)

#need to find the date of the Greatest Decrease with a df
Dec_Date = mydf[mydf["Profit/Losses"]==-1196225]

#pull date out of df so only the Date can be printed
Great_Dec_Date = Dec_Date["Date"]

#enter date in quotes so can be printed in output without extra "Name:, dtype"
Greatest_Dec_Date = "Sep-2013"

#Print all the data to the terminal
print("Financial Analysis")

print("-----------------------------------------")

print("Total Months:", Total_Months)

print("Total:", Net_Total)

print("Average Change:", Average_Change)

print("Greatest Increase in Profits:", Greatest_Inc_Date, Greatest_Increase)

print("Greatest Decrease in Profits:", Greatest_Dec_Date, Greatest_Decrease)

#define an output path for a text file
output_path = "C:\\Users\\tmlun\\python-challenge\\PyBank\\Analysis\\textfile.txt"
# output_path = "C:\\Users\\tmlun\\python-challenge\\PyBank\\Analysis\\"

txtfile = open(output_path,"w+")

#Print all the data to the txt file
print("Financial Analysis", file=txtfile)

print("-----------------------------------------", file=txtfile)

print("Total Months:", Total_Months, file=txtfile)

print("Total:", Net_Total, file=txtfile)

print("Average Change:", Average_Change, file=txtfile)

print("Greatest Increase in Profits:", Greatest_Inc_Date, Greatest_Increase, file=txtfile)

print("Greatest Decrease in Profits:", Greatest_Dec_Date, Greatest_Decrease, file=txtfile)

#close the txt file so that the file can be written
txtfile.close()
