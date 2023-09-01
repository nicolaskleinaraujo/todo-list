from PyQt5 import uic, QtWidgets
import pandas as pd

def init(): # runs when the program starts (row 58)
    # adds the db to the screen
    db = pd.read_csv('todolist-db.csv', sep=';')
    if db.size != 0:
        row = 0
        while True:
            try:
                todo_text = db.loc[row, 'TODO']
                list.todo_list.addItem(todo_text)
                row += 1
            except(ValueError, KeyError):
                break


def add_item():
    # takes the to-do item
    todo_text = list.todo_item.text()
    if todo_text != '':
        # adds the to-do to the screen
        list.todo_list.addItem(todo_text)
        # adds the to-do to the db
        row = 0
        while True:
            try:
                db.loc[row, 'TODO']
                row += 1
            except(ValueError, KeyError):
                break
        db.loc[row, 'TODO'] = f'{todo_text}'
        db.to_csv('todolist-db.csv', sep=';', index=False)
    # cleans the text label
    list.todo_item.setText('')


def delete_item():
    # saves the row on a variant
    current_row = list.todo_list.currentRow()
    # removes the to-do of the db
    db.drop(db.index[current_row], inplace=True)
    db.to_csv('todolist-db.csv', sep=';', index=False)
    # removes the to-do of the screen
    list.todo_list.takeItem(current_row)


# applying the funcs to the respctive buttons
app = QtWidgets.QApplication([])
list = uic.loadUi("window.ui")
list.add_button.clicked.connect(add_item)
list.done_button.clicked.connect(delete_item)

# running the app
list.show()
db = pd.read_csv('todolist-db.csv', sep=';')
init()
app.exec()
