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

#identify the values Profit/losses in the column
Profit_Loss = mydf["Profit/Losses"].values

#lists to hold the values and monthly changes
profit = []
monthly_change = []

#iterate through Profit_Loss and profit to add to lists
for x in Profit_Loss:  
    profit.append(x)
    
for i in range(len(profit)-1):
    monthly_change.append(profit[i+1]-profit[i])
    
#get the mean of monthly changes and round
Avg_change = round(sum(monthly_change)/85,2)

#get the greatest increase and greatest Decrease in profits/losses
Increase = max(monthly_change)
Decrease = min(monthly_change)

#find the date of the Greatest Increase and Greatest Decrease
Inc_Date = mydf[mydf["Profit/Losses"]==1170593]
Dec_Date = mydf[mydf["Profit/Losses"]==-1196225]

#pull dates out of the dfs
Great_Inc_Date = Inc_Date['Date']
Great_Dec_Date = Dec_Date["Date"]

#format dates so only dates will print in output
Greatest_Inc_Date = (Great_Inc_Date).values
Greatest_Dec_Date = (Great_Dec_Date).values

#Print all the data to the terminal
print("Financial Analysis")
print("-----------------------------------------")
print("Total Months:", Total_Months)
print("Total:", '${:}'.format(Total))
print("Average Change:", '${:}'.format(Avg_change))
print("Greatest Increase in Profits:", str(Greatest_Inc_Date)[1:-1], '${:}'.format(Increase))
print("Greatest Decrease in Profits:", str(Greatest_Dec_Date)[1:-1], '${:}'.format(Decrease))

#define an output path for a text file
output_path = "C:\\Users\\tmlun\\python-challenge\\PyBank\\Analysis\\textfile.txt"
txtfile = open(output_path,"w+")

#Print all the data to the txt file
print("Financial Analysis", file=txtfile)
print("-----------------------------------------", file=txtfile)
print("Total Months:", Total_Months, file=txtfile)
print("Total:", '${:}'.format(Total), file=txtfile)
print("Average Change:", '${:}'.format(Avg_change), file=txtfile)
print("Greatest Increase in Profits:", str(Greatest_Inc_Date)[1:-1], '${:}'.format(Increase), file=txtfile)
print("Greatest Decrease in Profits:", str(Greatest_Dec_Date)[1:-1], '${:}'.format(Decrease), file=txtfile)

#close the txt file so that the file can be written
txtfile.close()
