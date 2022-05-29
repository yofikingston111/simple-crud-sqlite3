#import modul
import sqlite3

try:
    sqliteConnection = sqlite3.connect('database_siswa.db')
    #create table database
    sqlite_create_table_query = '''CREATE TABLE data_siswa(
                                id INTEGER PRIMARY KEY,
                                nama TEXT NOT NULL,
                                email text NOT NULL UNIQUE);'''

    #adding data to database
    cursor = sqliteConnection.cursor()
    print("Database berhasil terkoneksi")

    #execution for asking sql
    cursor.execute(sqlite_create_table_query)
    print('Tabel berhhasil dibuat')

    # sqlite_select_Query = "select sqlite_version();"
    # cursor.execute(sqlite_select_Query)
    # record = cursor.fetchall()
    # print("Sqlite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error Gagal terkoneksi ke Database", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("Koneksi Databas Selesai")
