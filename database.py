import sqlite3


class MuseumDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('pengunjung.db')
        self.cursor = self.conn.cursor()

    def buat_tabel_pengunjung(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS pengunjung
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nama TEXT NOT NULL,
                                usia INTEGER NOT NULL,
                                nomor_hp TEXT NOT NULL,
                                alamat TEXT NOT NULL)''')
        self.conn.commit()

    def tambah_pengunjung(self, nama, usia, nomor_hp, alamat):
        self.cursor.execute('INSERT INTO pengunjung (nama, usia, nomor_hp, alamat) VALUES (?, ?, ?, ?)',
                            (nama, usia, nomor_hp, alamat))
        self.conn.commit()

    def update_pengunjung(self, pengunjung_id, nama, usia, nomor_hp, alamat):
        self.cursor.execute('UPDATE pengunjung SET nama=?, usia=?, nomor_hp=?, alamat=? WHERE id=?',
                            (nama, usia, nomor_hp, alamat, pengunjung_id))
        self.conn.commit()

    def hapus_pengunjung(self, pengunjung_id):
        self.cursor.execute(
            'DELETE FROM pengunjung WHERE id=?', (pengunjung_id,))
        self.conn.commit()

    def get_data_pengunjung(self):
        self.cursor.execute('SELECT * FROM pengunjung')
        return self.cursor.fetchall()
