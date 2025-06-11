from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

def createDB():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('Sepatu.db')

    if not db.open():
        QMessageBox.critical(None, qApp.tr("Cannot open database"),
                             qApp.tr("Unable to establish a database connection.\n"
                                     "This example needs SQLite support. Please read "
                                     "the Qt SQL driver documentation for information"
                                     "how to build it.\n\n" "Click Cancel to exit."),
                                    QMessageBox.Cancel)
        return False
    query = QSqlQuery()

    query.exec_("create table member(id int primary key,"
                "Name varchar(50), warna varchar (50), ukuran varchar(50))")

    query.exec_("insert into member values(01, 'Ardiles','Hitam','43')")
    query.exec_("insert into member values(02, 'Aerostreet','Putih','44')")
    query.exec_("insert into member values(03, 'Desle','Hitam Putih','43')")
    return True

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    createDB()
