def getStringDate (date):
    live = str(date)
    liveend = len(live)
    input = live[:liveend-2]+"20"+live[liveend-2:]
    
    return(input)
def colorConverter (color):
    output = "NA"
    if color == "Blue":
        output = "Complete"
    elif color == "Green":
        output = "On track"
    elif color == "Red":
        output = "High Risk"
    elif color == "Yellow":
        output = "At Risk"
    return output





from xml.etree.ElementPath import prepare_descendant
from openpyxl import load_workbook
import pandas as pd
import datetime
 
#load excel file
workbook = load_workbook(filename="InputChart.xlsx")
workbook.iso_dates = True
 
#open workbook
sheet = workbook.active

number = 11
 
dfData = pd.read_csv("input.csv")
pred  = pd.read_csv("feature-predecessors-5.csv")
succ = pd.read_csv("feature-successors-5.csv")
#modify the desired cell



for ind in dfData.index:
    value = dfData['Formatted ID'][ind]
    format_ID = "C" + str(number)
    progress = "H" + str(number)
    start_date = "I" + str(number)
    end_date = "J" + str(number)
    live1 = "L" + str(number)
    color = "G" + str(number)
    project = "B" + str(number)
    sheet[format_ID] = value
    name = "D" + str(number)
    predval = "E" + str(number)
    succval = "F" + str(number)
    percentage = str(dfData['% Complete'][ind])
    sheet[progress] = percentage


    sheet[project] = dfData['Project'][ind]

    sheet[start_date] = getStringDate(dfData['Planned Start'][ind])
    sheet[end_date] = getStringDate(dfData['Planned End'][ind])
    sheet[color] = colorConverter(str(dfData['Status Color'][ind]))
    sheet[name] = dfData['Name'][ind]
    
    if dfData['Formatted ID'][ind] == pred['ID'][ind]:
        sheet[predval] = pred['Predecessor ID'][ind]
    if dfData['Formatted ID'][ind] == succ['ID'][ind]:
        sheet[succval] = succ['Successor ID'][ind]

    sheet[live1] = getStringDate(dfData['Go Live'][ind])

    

    number += 1
  
 
#save the file
workbook.save(filename="InputChart.xlsx")