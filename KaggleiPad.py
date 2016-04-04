# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 01:09:07 2016

@author: reddowan
"""

import numpy as np, pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.lda import LDA

train=pd.read_csv("/home/reddowan/Documents/Kaggle edx MIT/eBayiPadTrainCleaned.csv")
testKaggle=pd.read_csv("/home/reddowan/Documents/Kaggle edx MIT/eBayiPadTestCleaned.csv")

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

conditions={'Used':1,'Seller refurbished':2,'Manufacturer refurbished':2,'New':3,'New other (see details)':3}
carriers=['AT&T','Sprint','T-Mobile','Verizon']
goodcolors=['Black','White']
badcolors=['Space Gray','Gold']
storage={'16':1,'32':2,'64':3}
iPadlines={'iPad 1':1,'iPad 2':2,'iPad 3':3,'iPad 4':4,'iPad 5':5}
iPadminilines={'iPad mini':1,'iPad mini 2':2,'iPad mini 3':3,'iPad mini Retina':4}
iPadAirlines={'iPad Air':1,'iPad Air 2':2}

X=pd.DataFrame(train, columns=['biddable','startprice','condition','cellular','carrier','color','storage','productline'])
X['iPadRepair']=np.zeros(1861) 
X['iPadmini']=np.zeros(1861) 
X['iPadAir']=np.zeros(1861) 


for index, row in X.iterrows():
 if X.loc[index,'condition'] in conditions:
  X.loc[index,'condition']=conditions.get(X.loc[index,'condition'])
 elif X.loc[index,'condition']=="For parts or not working":
  X.loc[index,'iPadRepair']=1
  X.loc[index,'condition']=0
  
 if X.loc[index,'cellular']=="Unknown":
  X.loc[index,'cellular']=0
  
 if X.loc[index,'carrier'] in carriers:
  X.loc[index,'carrier']=2
 elif X.loc[index,'carrier']=="Other":
  X.loc[index,'carrier']=1
 else :
  X.loc[index,'carrier']=0
  
 if X.loc[index,'color'] in goodcolors:
  X.loc[index,'color']=1
 elif X.loc[index,'color'] in badcolors:
  X.loc[index,'color']=-1
 else :
  X.loc[index,'color']=0
  
 if X.loc[index,'storage'] in storage:
  X.loc[index,'storage']=storage.get(X.loc[index,'storage'])
 else :
  X.loc[index,'storage']=1
   
 if X.loc[index,'productline'] in iPadlines:
  X.loc[index,'productline']=iPadlines.get(X.loc[index,'productline']) 
 elif X.loc[index,'productline'] in iPadminilines:
  X.loc[index,'iPadmini']=iPadminilines.get(X.loc[index,'productline'])  
  X.loc[index,'productline']=0 
 elif X.loc[index,'productline'] in iPadAirlines:
  X.loc[index,'iPadAir']=iPadAirlines.get(X.loc[index,'productline'])  
  X.loc[index,'productline']=0
 elif X.loc[index,'productline']=="Unknown":
  X.loc[index,'productline']=0

y=pd.DataFrame(train, columns=['sold'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
clf=LDA()
clf.fit(X_train,np.ravel(y_train))
y_pred=clf.predict(X_test)
print (accuracy_score(y_test,y_pred))


clf.fit(X,np.ravel(y))
X_testKaggle=pd.DataFrame(testKaggle, columns=['biddable','startprice','condition','cellular','carrier','color','storage','productline'])
X_testKaggle['iPadRepair']=np.zeros(798) 
X_testKaggle['iPadmini']=np.zeros(798) 
X_testKaggle['iPadAir']=np.zeros(798) 


for index, row in X_testKaggle.iterrows():
 if X_testKaggle.loc[index,'condition'] in conditions:
  X_testKaggle.loc[index,'condition']=conditions.get(X_testKaggle.loc[index,'condition'])
 elif X_testKaggle.loc[index,'condition']=="For parts or not working":
  X_testKaggle.loc[index,'iPadRepair']=1
  X_testKaggle.loc[index,'condition']=0
  
 if X_testKaggle.loc[index,'cellular']=="Unknown":
  X_testKaggle.loc[index,'cellular']=0
  
 if X_testKaggle.loc[index,'carrier'] in carriers:
  X_testKaggle.loc[index,'carrier']=2
 elif X_testKaggle.loc[index,'carrier']=="Other":
  X_testKaggle.loc[index,'carrier']=1
 else :
  X_testKaggle.loc[index,'carrier']=0
  
 if X_testKaggle.loc[index,'color'] in goodcolors:
  X_testKaggle.loc[index,'color']=1
 elif X_testKaggle.loc[index,'color'] in badcolors:
  X_testKaggle.loc[index,'color']=-1
 else :
  X_testKaggle.loc[index,'color']=0
  
 if X_testKaggle.loc[index,'storage'] in storage:
  X_testKaggle.loc[index,'storage']=storage.get(X_testKaggle.loc[index,'storage'])
 else :
  X_testKaggle.loc[index,'storage']=1
   
 if X_testKaggle.loc[index,'productline'] in iPadlines:
  X_testKaggle.loc[index,'productline']=iPadlines.get(X_testKaggle.loc[index,'productline']) 
 elif X_testKaggle.loc[index,'productline'] in iPadminilines:
  X_testKaggle.loc[index,'iPadmini']=iPadminilines.get(X_testKaggle.loc[index,'productline'])  
  X_testKaggle.loc[index,'productline']=0 
 elif X_testKaggle.loc[index,'productline'] in iPadAirlines:
  X_testKaggle.loc[index,'iPadAir']=iPadAirlines.get(X_testKaggle.loc[index,'productline'])  
  X_testKaggle.loc[index,'productline']=0
 elif X_testKaggle.loc[index,'productline']=="Unknown":
  X_testKaggle.loc[index,'productline']=0
  
result=pd.DataFrame(testKaggle, columns=['UniqueID','Probability1'])
y_pred=clf.predict_proba(X_testKaggle)
result['Probability1']=y_pred

np.savetxt("/home/reddowan/Documents/Kaggle edx MIT/resultLDA.csv",result,delimiter=",",fmt='%9f')
