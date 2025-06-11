from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

def createDB():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('datapengunjung.db')

    if not db.open():
        QMessageBox.critical(None, qApp.tr("Cannot open database"),
                             qApp.tr("Unable to establish a database connection.\n"
                                     "This example needs SQLite support. Please read "
                                     "the Qt SQL driver documentation for information"
                                     "how to build it.\n\n" "Click Cancel to exit."),
                                    QMessageBox.Cancel)
        return False
    query = QSqlQuery()

    query.exec_("CREATE TABLE IF NOT EXISTS pengunjung (id INTEGER PRIMARY KEY AUTOINCREMENT,nama TEXT NOT NULL,usia INTEGER NOT NULL,nomor_hp TEXT NOT NULL,alamat TEXT NOT NULL)")

    query.exec_("INSERT INTO pengunjung (nama, usia, nomor_hp, alamat) VALUES (?, ?, ?, ?)",(nama, usia, nomor_hp, alamat))
    query.exec_('UPDATE pengunjung SET nama=?, usia=?, nomor_hp=?, alamat=? WHERE id=?',
                            (nama, usia, nomor_hp, alamat, pengunjung_id))
    query.exec_('DELETE FROM pengunjung WHERE id=?', (pengunjung_id,))
    query.exec_('SELECT * FROM pengunjung')
    return True

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    createDB()
