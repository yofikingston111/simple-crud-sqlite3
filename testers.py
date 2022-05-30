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

#create function read data
def lihat_data():
    try:
        sqliteConnection = sqlite3.connect('database_siswa.db')
        cursor = sqliteConnection.cursor()
        print("Berhasil Terkoneksi ke Database")

        sqlite_select_query = """SELECT * from data_siswa"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total Baris: ", len(records))
        for row in records:
            print("Id: ", row[0])
            print("Nama: ", row[1])
            print("Email: ", row[2])
            print("\n")

        cursor.close()
    except sqlite3.Error as error:
        print("Gagal Membaca Data Dari Tabel", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("koneksi SQlite Selesai")

#showing data
lihat_data()

#looking for function
def get_data_siswa(id):
    try:
        sqliteConnection = sqlite3.connect('database_siswa.db')
        cursor = sqliteConnection.cursor()
        print("Berhasil terkoneksi ke Database")

        sql_select_query = """select * from data_siswa where id = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("ID yang dimasukkan", id)
        for row in records:
            print("Nama: ", row[1])
            print("Email ", row[2])
        cursor.close()

    except sqlite3.Error as error:
        print("Gagal Terkoneksi ke SQlite", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("Koneksi SQlite Selesai")

get_data_siswa(3)

#update data for function is from database
def update_data_siswa(id, nama):
    try:
        sqliteConnection = sqlite3.connect('database_siswa.db')
        cursor = sqliteConnection.cursor()
        print("Berhasil terknokensi ke database")

        sql_update_query = """Update data_siswa set nama = ? where id = ? """
        data = (nama, id)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Update Data Sukses")
        cursor.close()

    except sqlite3.Error as error:
        print("gagal terknoneksi ke tabel", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("Koneksi SQlite selesai")

#update data
update_data_siswa(2, 'kiplirbg')