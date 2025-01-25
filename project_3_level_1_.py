# -*- coding: utf-8 -*-
"""Project_3_Level_1_.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XK8cCelTwPSglo5D2e-s6eZFCTWoHRMl
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/AB_NYC_2019.csv')
df

df.isnull().sum()

df.duplicated().sum()

df.info()

df = df.drop(columns=['name','calculated_host_listings_count','neighbourhood'])

df.head()

df.info()

df['host_name'] = df['host_name'].astype(str)
df['host_name']= df['host_name'].str.replace("nan", " ")

df['host_name']=df['host_name'].str.replace('[^a-zA-Z]', '',regex=True)
df['host_name']=df['host_name'].str.replace(r'([a-z])([A-Z])', r'\1 \2', regex=True)

df.head()

# obtaning data

df_priced = df[df['price']!=0]
df_priced.head()

# if we need data for there minimum nights is a year or less

df_year = df[df['minimum_nights']<=367]
df_year.head()

# get data where available is atleast 1 day

df_available = df[df['availability_365']!=0]
df_available.head()

# converting data_type to string
df['last_review'] = df['last_review'].astype(str)
df['last_review'] = df['last_review'].str.replace("nan"," ")

# Deleting nan values
df.head()



