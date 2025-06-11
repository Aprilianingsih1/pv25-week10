import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox


class MuseumApp(QMainWindow):
    def __init__(self):
        super().__init__()
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

        self.data_pengunjung = []

    def tambah_pengunjung(self):
        nama = self.input_nama.text()
        usia = self.input_usia.text()

        if nama and usia:
            pengunjung = {'nama': nama, 'usia': usia}
            self.data_pengunjung.append(pengunjung)
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

        for pengunjung in self.data_pengunjung:
            label_pengunjung = QLabel(
                f'Nama: {pengunjung["nama"]}, Usia: {pengunjung["usia"]}')
            layout_pengunjung.addWidget(label_pengunjung)

        self.tampilan_pengunjung.setLayout(layout_pengunjung)
        self.layout.addWidget(self.tampilan_pengunjung)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    museum_app = MuseumApp()
    museum_app.show()
    sys.exit(app.exec_())
