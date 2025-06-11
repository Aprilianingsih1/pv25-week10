import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem


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

        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.conn = sqlite3.connect('pengunjung.db')
        self.cursor = self.conn.cursor()
        self.buat_tabel_pengunjung()

        self.tombol_update = QPushButton('Update')
        self.tombol_update.clicked.connect(self.update_pengunjung)
        self.layout.addWidget(self.tombol_update)

        self.tombol_hapus = QPushButton('Hapus')
        self.tombol_hapus.clicked.connect(self.hapus_pengunjung)
        self.layout.addWidget(self.tombol_hapus)

        self.tampilkan_data_pengunjung()

    def buat_tabel_pengunjung(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS pengunjung
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nama TEXT NOT NULL,
                                usia INTEGER NOT NULL,
                                nomor_hp TEXT NOT NULL,
                                alamat TEXT NOT NULL)''')
        self.conn.commit()

    def tambah_pengunjung(self):
        nama = self.input_nama.text()
        usia = self.input_usia.text()
        nomor_hp = self.input_nomor_hp.text()
        alamat = self.input_alamat.text()

        if nama and usia and nomor_hp and alamat:
            self.cursor.execute('INSERT INTO pengunjung (nama, usia, nomor_hp, alamat) VALUES (?, ?, ?, ?)',
                                (nama, usia, nomor_hp, alamat))
            self.conn.commit()
            self.input_nama.clear()
            self.input_usia.clear()
            self.input_nomor_hp.clear()
            self.input_alamat.clear()
            self.tampilkan_data_pengunjung()
        else:
            QMessageBox.warning(self, 'Peringatan', 'Harap isi semua kolom!')

    def update_pengunjung(self):
        selected_row = self.table_widget.currentRow()
        if selected_row >= 0:
            pengunjung_id = self.table_widget.item(selected_row, 0).text()
            nama = self.input_nama.text()
            usia = self.input_usia.text()
            nomor_hp = self.input_nomor_hp.text()
            alamat = self.input_alamat.text()

            if nama and usia and nomor_hp and alamat:
                self.cursor.execute('UPDATE pengunjung SET nama=?, usia=?, nomor_hp=?, alamat=? WHERE id=?',
                                    (nama, usia, nomor_hp, alamat, pengunjung_id))
                self.conn.commit()
                self.input_nama.clear()
                self.input_usia.clear()
                self.input_nomor_hp.clear()
                self.input_alamat.clear()
                self.tampilkan_data_pengunjung()
            else:
                QMessageBox.warning(self, 'Peringatan',
                                    'Harap isi semua kolom!')
        else:
            QMessageBox.warning(self, 'Peringatan',
                                'Pilih pengunjung yang ingin diubah!')

    def hapus_pengunjung(self):
        selected_row = self.table_widget.currentRow()
        if selected_row >= 0:
            pengunjung_id = self.table_widget.item(selected_row, 0).text()
            confirmation = QMessageBox.question(self, 'Konfirmasi', 'Apakah Anda yakin ingin menghapus pengunjung ini?',
                                                QMessageBox.Yes | QMessageBox.No)
            if confirmation == QMessageBox.Yes:
                self.cursor.execute(
                    'DELETE FROM pengunjung WHERE id=?', (pengunjung_id,))
                self.conn.commit()
                self.tampilkan_data_pengunjung()
        else:
            QMessageBox.warning(self, 'Peringatan',
                                'Pilih pengunjung yang ingin dihapus!')

    def tampilkan_data_pengunjung(self):
        self.cursor.execute('SELECT * FROM pengunjung')
        data_pengunjung = self.cursor.fetchall()

        column_count = len(data_pengunjung[0])
        row_count = len(data_pengunjung)

        self.table_widget.setColumnCount(column_count)
        self.table_widget.setRowCount(row_count)

        for row in range(row_count):
            for col in range(column_count):
                item = QTableWidgetItem(str(data_pengunjung[row][col]))
                self.table_widget.setItem(row, col, item)

        self.table_widget.setHorizontalHeaderLabels(
            ['ID', 'Nama', 'Usia', 'Nomor HP', 'Alamat'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MuseumApp()
    window.show()
    sys.exit(app.exec_())
