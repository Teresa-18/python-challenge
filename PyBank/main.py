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

#get the mean for the Profit/Losses column of dataset and round
Change = round(int(mydf["Profit/Losses"].mean()),2)

#format the mean to currency without commas and decimals
Average_Change = '${:}'.format(Change)

#get the greatest increase in profits
Increase = mydf["Profit/Losses"].max()

#format the greatest increase without commas or decimals
Greatest_Increase = '${:}'.format(Increase)

#need to find the date of the Greatest Increase with a df
Inc_Date = mydf[mydf["Profit/Losses"]==1170593]

#pull date out of df so only the Date can be printed
Great_Inc_Date = Inc_Date['Date']
print(Great_Inc_Date.to_string())

#enter date in quotes so can be printed in output without extra "Name:, dtype"
Greatest_Inc_Date = "Feb-2012"

#get the decrease in losses
Decrease = mydf["Profit/Losses"].min()

#format the greatest decrease without commas or decimals
Greatest_Decrease = '${:}'.format(Decrease)

#need to find the date of the Greatest Decrease with a df
Dec_Date = mydf[mydf["Profit/Losses"]==-1196225]

#pull date out of df so only the Date can be printed
Great_Dec_Date = Dec_Date["Date"]
print(Great_Dec_Date.to_string())

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
