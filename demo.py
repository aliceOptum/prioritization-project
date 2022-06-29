import csv
from lib2to3.pgen2.pgen import DFAState
from operator import index
from tracemalloc import stop
from queue import LifoQueue
import pandas as pd
import numpy as np

#use pandas

#code to import from csv
dfSucc = pd.read_csv("feature-successors-5.csv")



dfPred = pd.read_csv("feature-predecessors-5.csv")
#print(dfPred)




dfData = pd.read_csv("input.csv")
#print(dfData)

#print(df1)

def addToDF (dfData,index, stack):
    current = stack.get()
    print(current)
    for ind in dfSucc.index:
        if (dfSucc['ID'][ind]) == current: 
            stack.put(dfSucc['Successor ID'][ind])
            print("this added")
          

    found = dfData[dfData['Formatted ID'].str.contains(current)]
    new = dfData
    if not found.empty:
        print("HERE")
        cur = dfData[dfData['Formatted ID']==current]
        print(cur.values)
        line = pd.DataFrame(data = cur.values, columns = dfData.columns)
        dfData = pd.concat([dfData.iloc[:index], line, dfData.iloc[index:]]).reset_index(drop=True)
        print("NEW VERSION")
        print(dfData)
   
    return(dfData)
  




    


def modifiedBFS (dfData, current, index):
    stack = LifoQueue(maxsize=100000000)
    stack.put(current)
    while stack.qsize() > 0 :
        print("hereMOD")
        dfData = addToDF(dfData,index, stack)
        print("DID IT CHANGE??")
        print(dfData)
        print("old")
        print(stack.qsize())
        index += 1
    return(dfData)
 



for ind in dfPred.index:
    value = dfPred['ID'][ind]
    pred =  dfPred['Predecessor ID'][ind]

    if value in dfData['Formatted ID'].values and pred in dfData['Formatted ID'].values:
    
        index1 = dfData.loc[dfData['Formatted ID']==value].index[0]
        print(index1)
        predvalue = dfData[dfData['Formatted ID']==pred]
        #print(predvalue)
        predindex = dfData.loc[dfData['Formatted ID']==pred].index[0]


        line = pd.DataFrame(columns = dfData.columns,data = predvalue.values)

  



    # pandas DaraFrame drop() Syntax
        #dfData.drop(labels=None, axis=0, index=predindex, columns=None, level=None, inplace=True, errors='raise')
        dfData = pd.concat([dfData.iloc[:index1], line, dfData.iloc[index1:]]).reset_index(drop=True)
        dfData.drop_duplicates(inplace = True)
    dfData.to_csv('test.csv')

print(len(dfData))



for ind in dfData.index:

    current = dfData['Formatted ID'][ind]
    print(current)
  

    if current in dfSucc['ID'].values:
        index1 = dfData[dfData['Formatted ID']==current].index[0]+1
        succind = dfSucc.loc[dfSucc['ID']==current].index[0]
        val = dfSucc['Successor ID'][succind]
        print("this is val")
        print(val)
        dfData = modifiedBFS(dfData,val, index1)
       
        

    dfData.to_csv('test.csv')
      

print(len(dfData))


        



