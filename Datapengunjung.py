import sys
from PyQt5.QtSql import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox, QTableView, QTableWidgetItem


class MuseumApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aplikasi Museum')
        self.setGeometry(200, 200, 600, 400)

        self.layout = QVBoxLayout()

        self.input_nama = QLineEdit()
        self.input_usia = QLineEdit()
        self.input_nomor_hp = QLineEdit()
        self.input_alamat = QLineEdit()
        self.tombol_submit = QPushButton('Submit')
        self.tombol_submit.clicked.connect(self.tambah_pengunjung)

        self.layout.addWidget(QLabel('Nama Pengunjung:'))
        self.layout.addWidget(self.input_nama)
        self.layout.addWidget(QLabel('Usia Pengunjung:'))
        self.layout.addWidget(self.input_usia)
        self.layout.addWidget(QLabel('Nomor HP Pengunjung:'))
        self.layout.addWidget(self.input_nomor_hp)
        self.layout.addWidget(QLabel('Alamat Pengunjung:'))
        self.layout.addWidget(self.input_alamat)
        self.layout.addWidget(self.tombol_submit)

        self.table_view = QTableView()  # Use QTableView instead of QTableWidget
        self.layout.addWidget(self.table_view)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("pengunjung.db")
        self.db.open()
        self.buat_tabel_pengunjung()

        self.tombol_update = QPushButton('Update')
        self.tombol_update.clicked.connect(self.update_pengunjung)
        self.layout.addWidget(self.tombol_update)

        self.tombol_hapus = QPushButton('Hapus')
        self.tombol_hapus.clicked.connect(self.hapus_pengunjung)
        self.layout.addWidget(self.tombol_hapus)

        self.tampilkan_data_pengunjung()

    def buat_tabel_pengunjung(self):
        query = QSqlQuery()
        query.exec_("""
            CREATE TABLE IF NOT EXISTS pengunjung
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            usia INTEGER NOT NULL,
            nomor_hp TEXT NOT NULL,
            alamat TEXT NOT NULL)
        """)

    def tambah_pengunjung(self):
        nama = self.input_nama.text()
        usia = self.input_usia.text()
        nomor_hp = self.input_nomor_hp.text()
        alamat = self.input_alamat.text()

        if nama and usia and nomor_hp and alamat:
            query = QSqlQuery()
            query.prepare("INSERT INTO pengunjung (nama, usia, nomor_hp, alamat) VALUES (?, ?, ?, ?)")
            query.addBindValue(nama)
            query.addBindValue(int(usia))
            query.addBindValue(nomor_hp)
            query.addBindValue(alamat)
            query.exec_()
            self.input_nama.clear()
            self.input_usia.clear()
            self.input_nomor_hp.clear()
            self.input_alamat.clear()
            self.tampilkan_data_pengunjung()
        else:
            QMessageBox.warning(self, 'Peringatan', 'Harap isi semua kolom!')

    def update_pengunjung(self):
        selected_row = self.table_view.currentIndex().row()
        if selected_row >= 0:
            model = self.table_view.model()
            pengunjung_id = model.data(model.index(selected_row, 0))
            nama = self.input_nama.text()
            usia = self.input_usia.text()
            nomor_hp = self.input_nomor_hp.text()
            alamat = self.input_alamat.text()

            if nama and usia and nomor_hp and alamat:
                query = QSqlQuery()
                query.prepare("UPDATE pengunjung SET nama=?, usia=?, nomor_hp=?, alamat=? WHERE id=?")
                query.addBindValue(nama)
                query.addBindValue(int(usia))
                query.addBindValue(nomor_hp)
                query.addBindValue(alamat)
                query.addBindValue(int(pengunjung_id))
                query.exec_()
                self.input_nama.clear()
                self.input_usia.clear()
                self.input_nomor_hp.clear()
                self.input_alamat.clear()
                self.tampilkan_data_pengunjung()
            else:
                QMessageBox.warning(self, 'Peringatan', 'Harap isi semua kolom!')
        else:
            QMessageBox.warning(self, 'Peringatan', 'Pilih pengunjung yang ingin diubah!')

    def hapus_pengunjung(self):
        selected_row = self.table_view.currentIndex().row()
        if selected_row >= 0:
            model = self.table_view.model()
            pengunjung_id = model.data(model.index(selected_row, 0))
            confirmation = QMessageBox.question(self, 'Konfirmasi', 'Apakah Anda yakin ingin menghapus pengunjung ini?', QMessageBox.Yes | QMessageBox.No)
            if confirmation == QMessageBox.Yes:
                query = QSqlQuery()
                query.prepare("DELETE FROM pengunjung WHERE id=?")
                query.addBindValue(int(pengunjung_id))
                query.exec_()
                self.tampilkan_data_pengunjung()
        else:
            QMessageBox.warning(self, 'Peringatan', 'Pilih pengunjung yang ingin dihapus!')

    def tampilkan_data_pengunjung(self):
        query = QSqlQuery()
        query.exec_("SELECT * FROM pengunjung")

        model = QSqlTableModel()
        model.setQuery(query)
        model.setHeaderData(0, 1, "ID")
        model.setHeaderData(1, 1, "Nama")
        model.setHeaderData(2, 1, "Usia")
        model.setHeaderData(3, 1, "Nomor HP")
        model.setHeaderData(4, 1, "Alamat")

        self.table_view.setModel(model)
        self.table_view.setColumnHidden(0, True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MuseumApp()
    window.show()
    sys.exit(app.exec_())
