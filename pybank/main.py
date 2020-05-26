# Module for system
import os,sys
# Module for csv files
import csv
# module for pandas
import pandas as pd


# Leverage pandas for calculations by reading file as a dataframe
Bankfile = pd.read_csv(r'C:\Users\akibo\Desktop\Columbia Bootcamp\Python-Financials\pybank\Resources\budget_data.csv')

# Now we can calculate the neccessary information with headers as guides

Total_Months=Bankfile['Date'].count()
Total_ProfitLoss=Bankfile['ProfitLosses'].sum()
Average_PL=Bankfile['ProfitLosses'].mean()
Greatest_Loss=Bankfile['ProfitLosses'].min()
Greatest_Profit=Bankfile['ProfitLosses'].max()

# In order to print the date with the result, we can print it with the dataframe conditionally
Greatest_Loss_Month=Bankfile[Bankfile.ProfitLosses==int(Greatest_Loss)]
Greatest_Profit_Month=Bankfile[Bankfile.ProfitLosses==int(Greatest_Profit)]

# Printout of the results
print("Welcome to Python Bank!")
print("----------------------------")
print("Here are our statistics based on the data we have available:")
print("----------------------------")
print("Total Months: " + str(Total_Months))
print("Total Profit/Loss: " + str(Total_ProfitLoss))
print("Average Profit/Loss: " + str(Average_PL))
print("Greatest Profit: ")
print(Greatest_Profit_Month)
print("Greatest Loss: ")
print(Greatest_Loss_Month)

# Write the findings in a seperate text file (can be found in the 'Analysis' folder)
writer = open(r"C:\Users\akibo\Desktop\Columbia Bootcamp\Python-Financials\pybank\Analysis\Python_Analysis.txt",'w')
writer.write("Thank you for coming to Python Bank. Here is our Data. ")
# Data will be written on a new line each time due to the addition of an '/n' 
writer.write("\n Total Months: " + str(Total_Months))
writer.write("\n Total Profit/Loss: " + str(Total_ProfitLoss))
writer.write("\n Greatest Profit: ")
writer.write("\n" + str(Greatest_Profit_Month))
writer.write("\n Greatest Loss: ")
writer.write("\n" + str(Greatest_Loss_Month))