import pandas as pd
import numpy as np
import sys
import math
import random
import time
import csv


def readData(path):
    #read in the data
    #one-hot encode the data
    #normalize the data

    df=pd.read_csv(path)
    label=df.iloc[:,0]
    df=df.iloc[:,1:]

    cat=pd.DataFrame()
    num=pd.DataFrame()
  
    #data to be one-hot encoded
    cat=df.select_dtypes(include='object').astype('category')
   
    #data to be normalized
    num=df.select_dtypes(include='number')

    if not cat.empty:
        #one-hot encode the data
        cat=pd.get_dummies(cat,drop_first=True)
    if not num.empty:
        #normalize the data
        for column in num:
            maxx=num[column].abs().max()
            if maxx!=0:
                num[column]=num[column]/maxx
    
    #merge the data and labels back together
    if (not cat.empty) and (not num.empty):
        df=pd.concat([num,cat],axis=1)
        df=pd.concat([label,df],axis=1)
       
    elif not cat.empty:
        df=pd.concat([label,cat],axis=1)
       
    elif not num.empty:
        df=pd.concat([label,num],axis=1)       

    return df



