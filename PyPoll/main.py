
#import the module used to read your csv
import pandas as pd

#my csv file location - C:/Users/tmlun/python-challenge/PyPoll/Resources
mycsv = "C:\\Users\\tmlun\\python-challenge\\PyPoll\\Resources\\election_data.csv"

#read csv and create DataFrame
mydf = pd.read_csv(mycsv)

#count the total # of votes in the dataset
Total_Votes = mydf["Voter ID"].count()

#get the list of candidates that recieved votes
Candi_Name = mydf["Candidate"].unique()

#find and count the # of votes per candidate and get percentage of votes
    #set the names of the candidates
names = mydf["Candidate"].values 

    #lists to hold the # of votes for each candidate
Khan_vote=[]
Correy_vote=[]
Li_vote=[]
OTooley_vote=[]

    #for loop to go through votes and add to the correct list for each candidate
for i in names:
    if i == "Khan":
        Khan_vote.append(i)
    elif i == "Correy":
        Correy_vote.append(i)
    elif i == "Li":
        Li_vote.append(i)
    elif i == "O'Tooley":
        OTooley_vote.append(i)

#get the total vote count for each candidaten  
K_V = Khan_vote.count("Khan")
C_V = Correy_vote.count("Correy")
L_V = Li_vote.count("Li")
O_V = OTooley_vote.count("O'Tooley")

#get the vote percentage for each candidate
Khan_Percent = round((K_V/Total_Votes),2)
Correy_Percent = round((C_V/Total_Votes),2)
Li_Percent = round((L_V/Total_Votes),2)
OTooley_Percent = round((O_V/Total_Votes),2)

#Print all the data to the terminal
print("Election Results")
print("-----------------------------------------")
print("Total Votes:", Total_Votes)
print("-----------------------------------------")
print(Candi_Name[0],":",'{:.3%}'.format(Khan_Percent), K_V)
print(Candi_Name[1],":",'{:.3%}'.format(Correy_Percent), C_V)
print(Candi_Name[2],":",'{:.3%}'.format(Li_Percent), L_V)
print(Candi_Name[3],":",'{:.3%}'.format(OTooley_Percent), O_V)
print("-----------------------------------------")
print("Winner:",Candi_Name[0])
print("-----------------------------------------")

# #define an output path for a text file
output_path = "C:\\Users\\tmlun\\python-challenge\\PyPoll\\Analysis\\textfile.txt"
txtfile = open(output_path,"w+")

# #Print all the data to the txt file
print("Election Results", file=txtfile)
print("-----------------------------------------", file=txtfile)
print("Total Votes:", Total_Votes, file=txtfile)
print("-----------------------------------------", file=txtfile)
print(Candi_Name[0],":",'{:.3%}'.format(Khan_Percent), K_V, file=txtfile)
print(Candi_Name[1],":",'{:.3%}'.format(Correy_Percent), C_V, file=txtfile)
print(Candi_Name[2],":",'{:.3%}'.format(Li_Percent), L_V, file=txtfile)
print(Candi_Name[3],":",'{:.3%}'.format(OTooley_Percent), O_V, file=txtfile)
print("-----------------------------------------", file=txtfile)
print("Winner:",Candi_Name[0], file=txtfile)
print("-----------------------------------------", file=txtfile)

# #close the txt file so that the file can be written
txtfile.close()
