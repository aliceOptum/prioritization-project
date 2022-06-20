from openpyxl import load_workbook
import pandas as pd
 
#load excel file
workbook = load_workbook(filename="dependenciestemplate.xlsx")
 
#open workbook
sheet = workbook.active

number = 9
 
dfData = pd.read_csv("input.csv")
#modify the desired cell
sheet["D9"] = "Full Name"


for ind in dfData.index:
    value = dfData['Formatted ID'][ind]
    input = "D" + str(number)
    sheet[input] = value
    number += 1
  
 
#save the file
workbook.save(filename="dependenciestemplate.xlsx")