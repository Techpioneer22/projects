# -*- coding: utf-8 -*-
"""Copy of Project Banking Trans_Fraud fraud.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uVBwR2auAA11r2EsP8ruLKoxy2CmQO7V
"""
import os
import numpy as np
import pandas as pd
import tensorflow as tf
import pickle
from sklearn.utils import shuffle
from sklearn.preprocessing import MinMaxScaler 
from keras.layers import Dense
from keras.layers import Dropout
import seaborn as sn
import matplotlib as pt
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])
reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])

"""Compiled by:
1.  Perceviarance Chitima R195807D
2. Emmanuel Banda R197226Y
3. Agness Mashonganyika R195845Q

                Credit card fraud Detection
                
"""

from keras.models import Sequential
from google.colab import drive
drive.mount('/content/drive')

df_full =pd.read_csv('/content/drive/My Drive/Colab Notebooks/creditcard.csv')

df_full.describe()

df_full.head(5)

df_full.Class.value_counts()

df_full.sort_values( by='Class', ascending= False , inplace=True)

df_full.drop('Time', axis=1, inplace=True)

#Assigning the first 3000 samples to a new dataframe
df_sample = df_full.iloc[:3000, :]

df_sample.Class.value_counts()

shuffle_df = shuffle(df_sample, random_state= 42)

#slitting data into 2 .. training and testing segments
df_train = shuffle_df[0:2400]
df_test = shuffle_df[2400: ]

#Spliting each dataframe into feature and label
train_feature = np.array(df_train.values[:, 0:29])
train_label = np.array(df_train.values[:, -1])
test_feature = np.array(df_train.values[:, 0:29])
test_label = np.array(df_train.values[:, -1])

train_feature.shape

train_label.shape

scaler = MinMaxScaler()
scaler.fit(train_feature)
train_feature_trans=scaler.transform(train_feature)
train_feature_trans = scaler.transform(test_feature)

model= Sequential()

model.add(Dense(units=200,input_dim=29,kernel_initializer='uniform', activation='relu'))

model.add(Dropout(0.5))

model.add(Dense(units=200,kernel_initializer='uniform', activation='relu'))

model.add(Dropout(0.5))

model.add(Dense(units=1,kernel_initializer='uniform', activation='sigmoid'))

model.summary()

model.compile(loss='binary_crossentropy', optimizer='adam',
metrics=['accuracy'])

train_history = model.fit(x=train_feature_trans, y=train_label,
validation_split=0.8, epochs=200,
batch_size=500, verbose=2)

# Create Pickle file from the Linear Regression Classifier(clf)
with open('lineraregression.pickle', 'wb') as dump_var:
    pickle.dump(scaler, dump_var)

# Load the Pickle fule in the memory
pickle_in = open('lineraregression.pickle', 'rb')
pickle_scaler = pickle.load(pickle_in)

# Use the Pickle file insted of clf
accuracy_pkl = pickle_scaler.fit(X_train, y_train)
accuracy_scaler = scaler.fit(X_train, y_train)
print(accuracy_pkl == accuracy_scaler)


#!pip install streamlit

#!pip install pyngrok

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st

#!ls

#!ngrok authtoken xxxxx

#!ngrok

#from pyngrok import ngrok
#!streamlit run app.py
#public_url = ngrok.connect(port = '8080')#

#!pgrep streamlit

#public_url

#!ngrok kill
