import pandas as pd

mycsv = "C:\\Users\\tmlun\\python-challenge\\PyPoll\\Resources\\election_data.csv"

#C:/Users/tmlun/python-challenge/PyPoll/Resources


mydf = pd.read_csv(mycsv)

Total_Votes = mydf["Voter ID"].count()
print(Total_Votes)

