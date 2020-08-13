# -*- coding: utf-8 -*-
"""formatting_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jj0O_slAbJjYDPV7N9b0e5WXlgbl57Bf
"""

import numpy as np
import pandas as pd
from google.colab import files

files.upload() # upload studentAssesment_original.csv and online_classroom_data_original.csv
files.upload()
# FORMATTING online_classroom_data_original.csv
data1 = pd.read_csv('online_classroom_data_original.csv', decimal = ',')
data1 = data1.drop(columns = ['student', 'total_posts', 'timeonline', 'helpful_post', 'nice_code_post', 'collaborative_post', 'confused_post', 'creative_post', 'bad_post', 'amazing_post', 'Approved'])
col = data1.loc[: , "sk1_classroom":"sk4_classroom"]
data1['avg_score'] = col.mean(axis=1)
dataset = pd.read_csv('online_classroom_data_original.csv', decimal = ',')
dataset = dataset.drop(columns = ['student', 'sk1_classroom', 'helpful_post', 'nice_code_post', 'collaborative_post', 'confused_post', 'creative_post', 'bad_post', 'amazing_post', 'sk2_classroom', 'sk5_classroom', 'sk3_classroom', 'sk4_classroom', 'Approved'])
data1['avg_score'] *= 10
data1 = data1.drop(columns = ['sk1_classroom', 'sk2_classroom', 'sk3_classroom', 'sk5_classroom', 'sk4_classroom'])
dataset['final_score']= data1['avg_score']

dataset.columns = ['total_posts', 'time_online', 'final_score']
dataset = dataset.astype('float')
z1 = dataset['total_posts']
y1 = dataset['final_score']
x1 = dataset['time_online']
x1 /= 960
z1 /= 16
indexNames = dataset[dataset['time_online'] >= 25].index
dataset.drop(indexNames, inplace=True)
dataset.to_csv('online_classroom_data_formatted.csv')

# FORMATTING studentAssesment_original.csv
dataset = pd.read_csv('studentAssesment_original.csv')
dataset = dataset.drop(columns = ['id_assessment', 'id_student', 'is_banked'])
dataset = dataset.dropna()
dataset = dataset[:359]
dataset.columns = ['date_submitted', 'final_score']
x = dataset['date_submitted']
y = dataset['final_score']
dataset = dataset[~(x >= 40) | ~(y <=200)]
x = dataset['date_submitted']
y = dataset['final_score']
total_time = np.max(x) - np.min(x)
dataset.to_csv('studentAssesment_formatted.csv')