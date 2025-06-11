import sys
# import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox


class MuseumApp(QMainWindow):
    def _init_(self):
        super()._init_()
        self.setWindowTitle('Aplikasi Museum')
        self.setGeometry(200, 200, 400, 300)

        self.layout = QVBoxLayout()

        self.input_nama = QLineEdit()
        self.input_usia = QLineEdit()
        self.tombol_submit = QPushButton('Submit')
        self.tombol_submit.clicked.connect(self.tambah_pengunjung)

        self.layout.addWidget(QLabel('Nama Pengunjung:'))
        self.layout.addWidget(self.input_nama)
        self.layout.addWidget(QLabel('Usia Pengunjung:'))
        self.layout.addWidget(self.input_usia)
        self.layout.addWidget(self.tombol_submit)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.conn = sqlite3.connect('pengunjung2.db')
        self.cursor = self.conn.cursor()
        self.buat_tabel_pengunjung()

    def buat_tabel_pengunjung(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS pengunjung
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nama TEXT NOT NULL,
                                usia INTEGER NOT NULL)''')
        self.conn.commit()

    def tambah_pengunjung(self):
        nama = self.input_nama.text()
        usia = self.input_usia.text()

        if nama and usia:
            self.cursor.execute(
                'INSERT INTO pengunjung (nama, usia) VALUES (?, ?)', (nama, usia))
            self.conn.commit()
            self.input_nama.clear()
            self.input_usia.clear()
            self.tampilkan_data_pengunjung()
        else:
            QMessageBox.warning(self, 'Peringatan', 'Harap isi semua kolom!')

    def tampilkan_data_pengunjung(self):
        if hasattr(self, 'tampilan_pengunjung'):
            self.tampilan_pengunjung.setParent(None)

        self.tampilan_pengunjung = QWidget()
        layout_pengunjung = QVBoxLayout()

        self.cursor.execute('SELECT * FROM pengunjung')
        data_pengunjung = self.cursor.fetchall()

        for pengunjung in data_pengunjung:
            label_pengunjung = QLabel(
                f'Nama: {pengunjung[1]}, Usia: {pengunjung[2]}')
            layout_pengunjung.addWidget(label_pengunjung)

        self.tampilan_pengunjung.setLayout(layout_pengunjung)
        self.layout.addWidget(self.tampilan_pengunjung)


if _name_ == '_main_':
    app = QApplication(sys.argv)
    museum_app = MuseumApp()
    museum_app.show()
    sys.exit(app.exec_())
