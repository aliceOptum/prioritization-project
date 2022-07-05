import csv
from lib2to3.pgen2.pgen import DFAState
from operator import index
from tracemalloc import stop
from queue import LifoQueue
import pandas as pd
import numpy as np

#use pandas

def run(preds, succ, file):



    #change this value to the csv file for the successors
    dfSucc = pd.read_csv(succ)



    #change this value to the csv file for the predecessors
    dfPred = pd.read_csv(preds)




    #change this value to the csv file from rally
    dfData = pd.read_csv(file)


    def addToDF (dfData,index, stack):
        current = stack.get()
        for ind in dfSucc.index:
            if (dfSucc['ID'][ind]) == current: 
                stack.put(dfSucc['Successor ID'][ind])
            

        found = dfData[dfData['Formatted ID'].str.contains(current)]
        new = dfData
        if not found.empty:
            cur = dfData[dfData['Formatted ID']==current]
            line = pd.DataFrame(data = cur.values, columns = dfData.columns)
            dfData = pd.concat([dfData.iloc[:index], line, dfData.iloc[index:]]).reset_index(drop=True)
            dfData.drop_duplicates(inplace = True)
           
    
        return(dfData)
    




        


    def modifiedBFS (dfData, current, index):
        stack = LifoQueue(maxsize=100000000)
        stack.put(current)
        while stack.qsize() > 0 :
            dfData = addToDF(dfData,index, stack)
            index += 1
        return(dfData)
    



    for ind in dfPred.index:
        value = dfPred['ID'][ind]
        pred =  dfPred['Predecessor ID'][ind]

        if value in dfData['Formatted ID'].values and pred in dfData['Formatted ID'].values:
        
            index1 = dfData.loc[dfData['Formatted ID']==value].index[0]
            predvalue = dfData[dfData['Formatted ID']==pred]
            predindex = dfData.loc[dfData['Formatted ID']==pred].index[0]


            line = pd.DataFrame(columns = dfData.columns,data = predvalue.values)

    
     
            dfData = pd.concat([dfData.iloc[:index1], line, dfData.iloc[index1:]]).reset_index(drop=True)
            dfData.drop_duplicates(inplace = True)





    for index, row in dfData.iterrows():

        current = row['Formatted ID']

    

        if current in dfSucc['ID'].values:
            index1 = dfData[dfData['Formatted ID']==current].index[0]+1
            succind = dfSucc.loc[dfSucc['ID']==current].index[0]
            val = dfSucc['Successor ID'][succind]
            dfData = modifiedBFS(dfData,val, index1)
        
            


        
    dfData.to_csv(file)
    