import sqlite3
def tambah_data(id, nama, email):
    try:
        sqliteConnection = sqlite3.connect('database_siswa.db')
        cursor = sqliteConnection.cursor()
        print("Berhasil terkoneksi ke database")

        sqlite_insert_with_param = """INSERT INTO data_siswa
                                    (id, nama, email)
                                    VALUES(?, ?, ?);"""
        data_tuple = (id, nama, email)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Berhasil menambah data ke tabel")

        cursor.close()
    except sqlite3.Error as error:
        print("Error Gagal Terkoneksi ke Database",error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("Koneksi SQlite Selesai")

tambah_data(2, 'rijal', 'rijal@gmail.com')
tambah_data(3, 'mimin', 'mimin@gmail.com')
