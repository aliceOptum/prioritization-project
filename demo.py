import csv
from lib2to3.pgen2.pgen import DFAState
from operator import index
from tracemalloc import stop
import pandas as pd
import numpy as np

#use pandas

#code to import from csv

dfSucc = pd.read_csv("feature-successors-5.csv")



dfPred = pd.read_csv("feature-predecessors-5.csv")
#print(dfPred)




dfData = pd.read_csv("input.csv")
#print(dfData)
df1 = dfData[dfData['Formatted ID'].str.contains("ST13654")==True]
#print(df1)


if "ST13686" in dfData.values:
    print("Usdfsdf")

for ind in dfPred.index:
    value = dfPred['ID'][ind]
    pred =  dfPred['Predecessor ID'][ind]

    if value in dfData.values and pred in dfData.values:
    
        index1 = dfData[dfData['Formatted ID']==value].index[0]
        #print(index1)
        predvalue = dfData[dfData['Formatted ID']==pred]
        #print(predvalue)
        predindex = dfData.loc[dfData['Formatted ID']==pred].index[0]
        
        print(dfData.columns)
        print('that was head \n')

        line = pd.DataFrame(data = predvalue.values, columns = dfData.columns, index=[index1])

        print(line)



    # pandas DaraFrame drop() Syntax
        dfData.drop(labels=None, axis=0, index=predindex, columns=None, level=None, inplace=True, errors='raise')
        dfData = pd.concat([dfData.iloc[:index1], line, dfData.iloc[index1:]]).reset_index(drop=True)
        


        #print(dfData)


    dfData.to_csv('test.csv')
    


    
  


    """
    print(index1)
    print(index2)
    """

#plan - look at successors if in there paste below to rearrange: otherwise just paste in 







"""
    for iterate in data:
        value = iterate[2]
        #print(value)
        
        
        while prow(value) != -1:
            currentRow = prows[prows.index(value)]
            print(currentRow)
            value2 = currentRow[9]
            print("this is value 2")
            print(value2)
            if value2 in data:
                writer.writerow(data[data.index(value2)])
                data.remove(value2)
                print('here')
            prows.remove(currentRow)

        if value in data:
            writer.writerow(data[data.index(value)])
        
        while value in srows:
            currentRow = srows[srows.index(value)]
            print(currentRow)
            value2 = currentRow[9]
            if value2 in data:
                writer.writerow(data[data.index(value2)])
                data.remove(value2)
                print('here')
            prows.remove(currentRow)"""
        



