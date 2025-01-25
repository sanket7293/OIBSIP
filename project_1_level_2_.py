# -*- coding: utf-8 -*-
"""Project_1_Level_2_.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XK8cCelTwPSglo5D2e-s6eZFCTWoHRMl
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/Housing.csv')
df

df.isnull().sum()

df.info()

df['mainroad'] = df['mainroad'].map({'yes':1,'no':0})
df['guestroom'] = df['guestroom'].map({'yes':1,'no':0})
df['basement']= df['basement'].map({'yes':1,'no':0})
df['hotwaterheating'] = df['hotwaterheating'].map({'yes':1,'no':0})
df['airconditioning']= df['airconditioning'].map({'yes':1,'no':0})
df['prefarea'] = df['prefarea'].map({'yes':1,'no':0})

df.head()

df = pd.get_dummies(df,columns=['furnishingstatus'],drop_first=True)

df.head()

x = df.drop(columns=['price'])
y = df['price']

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train,Y_train)

y_pred = lr.predict(X_test)

from sklearn.metrics import r2_score,mean_squared_error

print('r2_score',r2_score(Y_test,y_pred))
print('MSE',mean_squared_error(Y_test,y_pred))

plt.figure(figsize=(8,6))
plt.scatter(Y_test,y_pred)
plt.plot([min(Y_test),max(Y_test)],[min(Y_test),max(Y_test)],color='r',lw=2)
plt.title('Actual vs Prediction')
plt.xlabel('Actual price')
plt.ylabel('Predicted Price')
plt.show()

plt.figure(figsize=(8,6))
sns.residplot(x=Y_test,y=y_pred)
plt.title('Residuals plot')
plt.xlabel('Actual Price')
plt.ylabel('Residuals')
plt.show()



