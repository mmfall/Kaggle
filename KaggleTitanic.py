# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 22:10:26 2016

@author: reddowan
"""
import numpy as np, panda as pd
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

train=pd.read_csv("/home/reddowan/Documents/Kaggle Titanic/train.csv")
testKaggle=pd.read_csv("/home/reddowan/Documents/Kaggle Titanic/test.csv")
X=pd.DataFrame(train, columns=['Pclass','Sex'])
X['Sex'].replace(to_replace="male",value=0,inplace=1)
X['Sex'].replace(to_replace="female",value=1,inplace=1)
y=pd.DataFrame(train, columns=['Survived'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
clf=RandomForestClassifier()
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print (accuracy_score(y_test,y_pred))

clf.fit(X,y)
X_testKaggle=pd.DataFrame(testKaggle, columns=['Pclass','Sex'])
X_testKaggle['Sex'].replace(to_replace="male",value=0,inplace=1)
X_testKaggle['Sex'].replace(to_replace="female",value=1,inplace=1)
result=pd.DataFrame(testKaggle, columns=['PassengerId','Survived'])
y_pred=clf.predict(X_testKaggle)
result['Survived']=y_pred

np.savetxt("/home/reddowan/Documents/Kaggle Titanic/result.csv",result,delimiter=",",fmt='%3d')
