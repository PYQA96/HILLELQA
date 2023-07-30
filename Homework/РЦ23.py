import pandas as pd

data = pd.read_csv('data.csv')

data.drop('Возраст', axis=1, inplace=True)

data.to_excel('data.xlsx', index=False, engine='openpyxl')