# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:34:00 2021

@author: ahmet
"""

import pandas as pd
ad = pd.read_csv("/Users/ahmet/Desktop/Python/Advertising.csv")
df = ad.copy()
df.head()
df = df.iloc[:,1:len(df)]
df.info()
df.describe().transpose()

import seaborn as sns
sns.pairplot(df, kind ="reg");
sns.jointplot(x= "TV", y = "sales", data=df, kind="reg")
x = df[["TV"]]
y = df[["sales"]]

from sklearn.model_selection import train_test_split, cross_val_score,cross_val_predict
x = df.drop("sales", axis =1)
y = df["sales"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0 )
lm = sm.OLS(y_train, x_train)
