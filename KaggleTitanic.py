# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 22:10:26 2016

@author: reddowan
"""
import numpy as np, pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

train=pd.read_csv("/home/reddowan/Documents/Kaggle Titanic/train.csv")
testKaggle=pd.read_csv("/home/reddowan/Documents/Kaggle Titanic/test.csv")
X=pd.DataFrame(train, columns=['Pclass','Sex','SibSp','Parch'])
X['Sex'].replace(to_replace="male",value=-1,inplace=1)
X['Sex'].replace(to_replace="female",value=1,inplace=1)
X['Pclass2']=np.zeros(891) 
X['Pclass3']=np.zeros(891) """24% de survie en classe 3, 47% en classe 2, 63% de survie en classe 1. Overall 38% de survie"""
for index, row in X.iterrows():
 if X.loc[index,'Pclass']==3:
  X.loc[index,'Pclass3']=1
  X.loc[index,'Pclass']=0
 if X.loc[index,'Pclass']==2:
  X.loc[index,'Pclass2']=1
  X.loc[index,'Pclass']=0

y=pd.DataFrame(train, columns=['Survived'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf=DecisionTreeClassifier(max_depth=5)
clf.fit(X_train,np.ravel(y_train))
y_pred=clf.predict(X_test)
print (accuracy_score(y_test,y_pred))

clf.fit(X,np.ravel(y))
X_testKaggle=pd.DataFrame(testKaggle, columns=['Pclass','Sex','SibSp','Parch'])
X_testKaggle['Sex'].replace(to_replace="male",value=-1,inplace=1)
X_testKaggle['Sex'].replace(to_replace="female",value=1,inplace=1)
X_testKaggle['Pclass2']=np.zeros(418) """taille des zeros à remplir"""
X_testKaggle['Pclass3']=np.zeros(418)
for index, row in X_testKaggle.iterrows():
 if X_testKaggle.loc[index,'Pclass']==3:
  X_testKaggle.loc[index,'Pclass3']=1
  X_testKaggle.loc[index,'Pclass']=0
 if X_testKaggle.loc[index,'Pclass']==2:
  X_testKaggle.loc[index,'Pclass2']=1
  X_testKaggle.loc[index,'Pclass']=0
result=pd.DataFrame(testKaggle, columns=['PassengerId','Survived'])
y_pred=clf.predict(X_testKaggle)
result['Survived']=y_pred

tree.export_graphviz(clf,out_file="tree.dot",feature_names=['Pclass','Sex','SibSp','Parch','Pclass2','Pclass3'],class_names=['Death','Alive'],filled=True, rounded=True)  
                         
    
np.savetxt("/home/reddowan/Documents/Kaggle Titanic/resultTree5.csv",result,delimiter=",",fmt='%3d')
