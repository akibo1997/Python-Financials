# Import operating system, pandas, and csv file
import os,sys
import csv
import pandas as pd

# Import the csv file and convert to dataframe
Poll_Data = pd.read_csv(r'C:\Users\akibo\Desktop\Columbia Bootcamp\Python-Financials\pypoll\Resources\election_data.csv')

# Calculate the amount of total votes
Total_Votes=Poll_Data.shape[0]-1

#Calculate the vote totals for each candidate by slicing and counting rows
#The number of rows with the candidate name will be their vote total
Khan_Votes=Poll_Data[Poll_Data.Candidate=='Khan'].shape[0]
OTooley_Votes=Poll_Data[Poll_Data.Candidate=="O'Tooley"].shape[0]
Correy_Votes=Poll_Data[Poll_Data.Candidate=='Correy'].shape[0]
Li_Votes=Poll_Data[Poll_Data.Candidate=='Li'].shape[0]


# Calculate the percentages of votes
Khan_Percentage=(Khan_Votes / Total_Votes)*100
OTooley_Percentage=(OTooley_Votes/Total_Votes)*100
Correy_Percentage=(Correy_Votes/Total_Votes)*100
Li_Percentage=(Li_Votes/Total_Votes)*100

# Determine a winner by determing the person with the greatest amount of votes in the dictionary
Results_Dictionary={'Khan':Khan_Votes,"O'Tooley":OTooley_Votes,'Correy':Correy_Votes,'Li':Li_Votes}
Winner=max(Results_Dictionary,key=Results_Dictionary.get)
print(Winner)

print("The election results are in!")
print("----------------------------")
print("Khan: "+ str(Khan_Votes) + " ("+ str(Khan_Percentage) + "%" +")")
print("Khan: "+ str(Khan_Votes) + " ("+ str(Khan_Percentage) + "%" +")")
print("Khan: "+ str(Khan_Votes) + " ("+ str(Khan_Percentage) + "%" +")")
print("Khan: "+ str(Khan_Votes) + " ("+ str(Khan_Percentage) + "%" +")")