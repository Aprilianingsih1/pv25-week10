import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def initializeModel(model):
    model.setTable('member')
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, Qt.Horizontal, "ID")
    model.setHeaderData(1, Qt.Horizontal, "Name")
    model.setHeaderData(2, Qt.Horizontal, "warna")
    model.setHeaderData(3, Qt.Horizontal, "ukuran")

def createView(title, model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

def addrow():
    print(model.rowCount())
    ret = model.insertRows(model.rowCount(), 1)
    print(ret)

def findrow(i):
    delrow = i.row()
    print(delrow)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    database = QSqlDatabase.addDatabase('QSQLITE')
    database.setDatabaseName('Sepatu.db')
    model = QSqlTableModel()
    delrow = -1
    initializeModel(model)

    view1 = createView("Table  Model (View 1)", model)
    view1.clicked.connect(findrow)

    dialog = QDialog()
    layout = QVBoxLayout()
    layout.addWidget(view1)

    button = QPushButton("Add a row")
    button.clicked.connect(addrow)
    layout.addWidget(button)

    button1 = QPushButton("del a row")
    button.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
    layout.addWidget(button1)

    dialog.setLayout(layout)
    dialog.setWindowTitle("Database demonstration")
    dialog.show()
    sys.exit(app.exec_())