import pandas as pd
import openpyxl

db = pd.read_csv('todolist-db.csv', sep=';')
row = 0
while True:
    try:
        db.loc[row, 'TODO']
        row += 1
    except(ValueError, KeyError):
        break
db.loc[row, 'TODO'] = todo_text
db.to_csv('todolist-db.csv', sep=';', index=False)
