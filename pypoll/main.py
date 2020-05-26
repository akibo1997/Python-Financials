# Import operating system, pandas, and csv file
import os,sys
import csv
import pandas as pd

# Import the csv file and convert to dataframe
Poll_Data = pd.read_csv(r'C:\Users\akibo\Desktop\Columbia Bootcamp\Python-Financials\pypoll\Resources\election_data.csv')

# Calculate the amount of total votes
# You can get the total votes by getting the rows of the dataframe and slicing the output so it just gives you the rows
# Slice the output to just the first number (the rows) and subtract by one to account for the header
Total_Votes=Poll_Data.shape[0]-1

# Calculate the vote totals for each candidate by slicing and counting rows
# The number of rows with the candidate name will be their vote total
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

# Printout of results
print("The election results are in!")
print("----------------------------")
print("Total Votes: "+ str(Total_Votes))
print("----------------------------")
print("Khan: "+ str(Khan_Votes) + " ("+ str(Khan_Percentage) + "%" +")")
print("O'Tooley: "+ str(OTooley_Votes) + " ("+ str(OTooley_Percentage) + "%" +")")
print("Correy: "+ str(Correy_Votes) + " ("+ str(Correy_Percentage) + "%" +")")
print("Li: "+ str(Li_Votes) + " ("+ str(Li_Percentage) + "%" +")")
print("And the winner is... "+str(Winner)+"!")

# Write the findings in a seperate text file (can be found in the 'Analysis' folder)
writer = open(r"C:\Users\akibo\Desktop\Columbia Bootcamp\Python-Financials\pypoll\Analysis\Pypoll_Analysis.txt",'w')
# Use /n to write each instruction on a seperate line
writer.write("\n The election results are in!")
writer.write("\n ----------------------------")
writer.write("\n Total Votes: "+ str(Total_Votes))
writer.write("\n ----------------------------")
writer.write("\n Khan: "+ str(Khan_Votes) + " ("+ str(Khan_Percentage) + "%" +")")
writer.write("\n O'Tooley: "+ str(OTooley_Votes) + " ("+ str(OTooley_Percentage) + "%" +")")
writer.write("\n Correy: "+ str(Correy_Votes) + " ("+ str(Correy_Percentage) + "%" +")")
writer.write("\n Li: "+ str(Li_Votes) + " ("+ str(Li_Percentage) + "%" +")")
writer.write("\n And the winner is... "+str(Winner)+"!")