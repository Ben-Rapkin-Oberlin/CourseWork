#Reads CSV

import pandas as pd
import numpy as np
import sys


import csv
def readData(path):
    #figure out which rows are continuous and which are nominal
    #copy nominal data to new list
    #copy continuous data to new list
    #hot encode nominal data note not enough to drop one column, must make sure it can be represented by the other columns
    #normalize continuous data
    #recombine data
    #currently dropping first, this is more than he asked for need to check in
    data = pd.read_csv(path)
    if path=="minst_5v8.csv":
        return data
    label=data.columns.to_numpy()
    datatype=[]
    for x in data.loc[0]:
        try: #data will be numeric
            a=float(x)
            datatype.append("continuous")
        except: #data will be nominal
            datatype.append("nominal")
    nomdf = pd.DataFrame()
    condf = pd.DataFrame()
    labelnom=[]
    labelcon=[]
    for i in range(len(datatype)):
        if datatype[i]=="nominal":
            nomdf[nomdf.columns.to_numpy().size]=data[label[i]]
            labelnom.append(label[i])
        else:
            condf[condf.columns.to_numpy().size]=data[label[i]].astype(float)
            labelcon.append(label[i])
    nomdf.columns=labelnom
    condf.columns=labelcon
    try:
        nomdf = pd.get_dummies(nomdf, drop_first=True).astype(float)
    except:
        pass
    #normalize continuous data
    for i in range(len(labelcon)):
        big=condf[labelcon[i]].max()
        small=condf[labelcon[i]].min()
        if big== 0.0 and small==0.0:
            a=labelcon[i]
            condf=condf.assign(a=lambda x: 0.0) 
        else:
            condf[labelcon[i]]=(condf[labelcon[i]]-small)/(big-small)
    try:
        df=pd.concat([condf,nomdf],axis=1)
        return df
    except:
        if nomdf.empty:
            return condf
        else:
            return nomdf
   # print(df.loc[240:245])
    return df