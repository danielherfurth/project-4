# %%
import csv_to_sqlite

# all the usual options are supported
options = csv_to_sqlite.CsvOptions(typing_style="full", encoding='utf-8')
input_files = ['data/test.csv', 'data/train.csv']  # pass in a list of CSV files
csv_to_sqlite.write_csv(input_files, "output.sqlite", options)

#%%
import pandas as pd
test = pd.read_csv('data/train.csv')

test.dropna(inplace=True)
import sqlite3

conn = sqlite3.connect('output.sqlite')

test.to_sql('train', conn)

#%%
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)

test = pd.read_csv('data/train.csv')

test = test.iloc[:,1:-1]
test.dropna(inplace=True)

test.to_csv('train_.csv')
#%%
train = pd.read_csv('data/train.csv')

train[['title', 'author', 'text', 'label']]

#%%
train.to_csv('data/train_.csv')

#%%
train = pd.read_csv(r'C:\Users\danie\desktop\train.csv')

#%%
train.head()

#%%
train = train.iloc[:,1:]

#%%
train.fillna('unknown', inplace=True)
train.to_csv('data/train_.csv')

#%%
train.isna().sum()

#%%
test = pd.read_csv(r'C:\Users\danie\desktop\test.csv')

test= test.iloc[:,1:]

#%%
test.fillna('unknown', inplace=True)

test.to_csv('data/test_.csv')

#%%
import csv_to_sqlite

csv_to_sqlite.start(['data/train_.csv', 'data/test_.csv'])