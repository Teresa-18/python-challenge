# import os
# import csv
import pandas as pd

budget_csv = "C:\\Users\\tmlun\\python-challenge\\PyBank\\Resources\\budget_data.csv"

mydf = pd.read_csv(budget_csv)

#print(mydf)

Total_Months = mydf["Date"].count()

Total_Months

Net_Total = mydf["Profit/Losses"].sum()

Net_Total

Average_Change = round(int(mydf["Profit/Losses"].mean()),2)

Average_Change

Greatest_Inc = mydf["Profit/Losses"].max()

Greatest_Inc

Great_Inc_Date = mydf[mydf["Profit/Losses"]==1170593]

Great_Inc_Date
i_Date = "Feb-2012"

Greatest_Dec = mydf["Profit/Losses"].min()

Greatest_Dec

Great_Dec_Date = mydf[mydf["Profit/Losses"]==-1196225]

Great_Dec_Date
d_Date = "Sep-2013"

output_path = "C:\\Users\\tmlun\\python-challenge\\PyBank\\Analysis\\textfile.txt"

txtfile = open(output_path,"w+")

print("Financial Analysis", file=txtfile)

print("-----------------------------------------", file=txtfile)

# print("Total Months:", Total_Months)

# print("Total:", Net_Total)

# print("Average Change:", Average_Change)

# print("Greatest Increase in Profits:", i_Date, Greatest_Inc)

# print("Greatest Decrease in Profits:", d_Date, Greatest_Dec)



# output_path = "C:\\Users\\tmlun\\python-challenge\\PyBank\\Analysis\\"
# #C:/Users/tmlun/python-challenge/PyBank/Resources
# with open(output_path, 'w', newline= '') as csvfile
    
#     csvwrite=csv.writer(csvfile, delimiter = ',')
#     csvwrite.writerow(["Financial Analysis"])

# txt_file.write(results)
txtfile.close()