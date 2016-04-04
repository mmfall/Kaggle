# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 01:09:07 2016

@author: reddowan
"""

import numpy as np, pandas as pd

train=pd.read_csv("/home/reddowan/Documents/Kaggle edx MIT/eBayiPadTrainCleaned.csv")
testKaggle=pd.read_csv("/home/reddowan/Documents/Kaggle edx MIT/eBayiPadTestCleaned.csv")
"""train.loc[:,'Unnamed: 11']
train.loc[:,'Unnamed: 12']"""
list(train.columns.values)
np.unique(train['biddable']) """array([0, 1])"""
np.unique(train['condition']) """array(['For parts or not working', 'Manufacturer refurbished', 'New',
       'New other (see details)', 'Seller refurbished', 'Used'], dtype=object)"""
np.unique(train['cellular']) """array(['0', '1', 'Unknown'], dtype=object)"""
np.unique(train['carrier']) """array(['AT&T', 'None', 'Other', 'Sprint', 'T-Mobile', 'Unknown', 'Verizon'], dtype=object)"""
np.unique(train['color']) """array(['Black', 'Gold', 'Space Gray', 'Unknown', 'White'], dtype=object)"""
np.unique(train['storage']) """array(['128', '16', '32', '64', 'Unknown'], dtype=object)"""
np.unique(train['productline']) """array(['Unknown', 'iPad 1', 'iPad 2', 'iPad 3', 'iPad 4', 'iPad 5',
       'iPad Air', 'iPad Air 2', 'iPad mini', 'iPad mini 2', 'iPad mini 3',
       'iPad mini Retina'], dtype=object)"""


X=pd.DataFrame(train, columns=['biddable','startprice','condition','cellular','carrier','color','storage','productline'])
for index, row in X.iterrows():
 if X.loc[index,'condition'] in conditions={'Used':0,'Seller refurbished':1,'New':2,'New other (see details)':2}
  X.loc[index,'condition']=conditions.get(X.loc[index,'condition'])
 """if X.loc[index,'condition']=="Used":
  X.loc[index,'condition']=0
 elif X.loc[index,'condition']=="Seller refurbished":
  X.loc[index,'condition']=1
 elif X.loc[index,'condition']=="New":
  X.loc[index,'condition']=2
 elif X.loc[index,'condition']=="New other (see details)":
  X.loc[index,'condition']=2 
 """elif X.loc[index,'condition'].isdigit()==True:
  X.loc[index,'condition']=X.loc[index,'cellular']
  
 if X.loc[index,'cellular']=="Unknown":
  X.loc[index,'cellular']=-1
 elif X.loc[index,'cellular'].isdigit()==False:
  X.loc[index,'cellular']=X.loc[index,'carrier']
  
 if X.loc[index,'carrier'] in carriers=['AT&T','Sprint','T-Mobile','Verizon']:
  X.loc[index,'carrier']=2
 elif X.loc[index,'carrier']=="Other":
  X.loc[index,'carrier']=1
 else :
  X.loc[index,'carrier']=0
  
 if X.loc[index,'storage']=="Unknown"
  X.loc[index,'storage']=0
 elif X.loc[index,'storage'].isdigit()==False:
  X.loc[index,'storage']=X.loc[index,'productline']

 if X.loc[index,'productline'] in productlines={'iPad 1':0,'iPad 2':1,'iPad 3':2,'iPad 4':3}
  X.loc[index,'productline']=conditions.get(X.loc[index,'productline']) 
  
  
  
y=pd.DataFrame(train, columns=['sold'])
