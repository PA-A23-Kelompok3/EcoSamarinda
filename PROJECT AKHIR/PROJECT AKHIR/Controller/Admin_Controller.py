from View import Tampilan_Pelapor as pelapor
from View import Tampilan_Main as Main
from View import Tampilan_Admin as admin
from Controller import Pelapor_Controller as pelacon
from Model.Database import connect_database
from prettytable import PrettyTable
import os

mydb, cursor = connect_database()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def LoginAdmin():
        Username = input('Masukkan Username Anda: ')
        if len(Username) <= 15:
            Password = input('Masukkan Password Anda: ')
            if len(Password) <= 20:
                query = "SELECT * FROM Admin WHERE Username = %s AND Password = %s"
                cursor.execute(query, (Username, Password))
                hasil = cursor.fetchone()
                if hasil:
                    admin.menu_admin(Username,cursor)
                else:
                    clear()
                    print('╔═══════════════════════════════════════════╗')
                    print("|       DATA YANG ANDA MASUKKAN SALAH       |")
                    print('╚═══════════════════════════════════════════╝')
                    input('Tekan enter untuk kembali...')
                    admin.AwalAdmin()
            else:
                print('Password tidak boleh lebih dari 20 karakter...')
                input('Tekan enter untuk kembali..')
                admin.AwalAdmin()
        else:
            print('Username tidak boleh lebih dari 15 karakter...')
            input('Tekan enter untuk kembali..')
            admin.AwalAdmin()

## SECTION LAPORAN ##

def MelihatLaporan():
    clear()
    # Mendapatkan data laporan dari database
    query_get_laporan = "SELECT * FROM informasi"
    cursor.execute(query_get_laporan)
    laporan_data = cursor.fetchall()

    # Menampilkan data laporan dengan PrettyTable
    table = PrettyTable()
    table.field_names = ["ID Informasi", "ID Pelapor", "ID Admin", "Tanggal Waktu", "Judul Informasi", "Deskripsi Informasi"]
    for laporan in laporan_data:
        table.add_row(laporan)
    
    print(table)
    input('Tekan enter untuk kembali...')

def MengeditLaporan():
    clear()
    print('╔══════════════════════════════════════════╗')
    print('|          -- MENGEDIT LAPORAN --          |')
    print('╚══════════════════════════════════════════╝')
    id_laporan = int(input("Masukkan ID laporan yang ingin diedit: "))
    
    # Cek apakah laporan ada dalam database
    query_check_laporan = "SELECT * FROM informasi WHERE ID_Informasi = %s"
    cursor.execute(query_check_laporan, (id_laporan,))
    laporan_exists = cursor.fetchone()

    if laporan_exists:
        # Meminta input pengguna untuk data yang akan diedit
        judul_baru = input("Masukkan judul informasi yang baru: ")
        deskripsi_baru = input("Masukkan deskripsi informasi yang baru: ")

        # Update data laporan di database
        query_update_laporan = "UPDATE informasi SET Judul_Informasi = %s, Deskripsi_Informasi = %s WHERE ID_Informasi = %s"
        cursor.execute(query_update_laporan, (judul_baru, deskripsi_baru, id_laporan))
        mydb.commit()

        print("Laporan berhasil diperbarui!")
    else:
        print("Laporan tidak ditemukan.")

    input('Tekan enter untuk kembali...')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

class LaporanManager:
    def __init__(self, cursor):
        self.cursor = cursor

    def jump_search_laporan_by_id(self):
        clear()
        id_laporan = int(input("Masukkan ID laporan yang ingin Anda cari: "))

        # Mendapatkan data laporan dari database
        query_get_laporan = "SELECT * FROM informasi"
        self.cursor.execute(query_get_laporan)
        laporan_data = self.cursor.fetchall()

        # Memasukkan data laporan ke dalam linked list
        linked_list = LinkedList()
        for laporan in laporan_data:
            linked_list.insert(laporan)

        # Mengurutkan data laporan berdasarkan ID_Informasi
        laporan_data.sort(key=lambda x: x[0])

        n = len(laporan_data)
        step = int(n ** 0.5)  # Step size untuk jump search
        prev = 0
        while laporan_data[min(step, n)-1][0] < id_laporan:
            prev = step
            step += int(n ** 0.5)
            if prev >= n:
                print("Laporan tidak ditemukan.")
                input('Tekan enter untuk kembali...')
                return

        # Melakukan linear search pada blok yang relevan
        while laporan_data[prev][0] < id_laporan:
            prev += 1
            if prev == min(step, n):
                print("Laporan tidak ditemukan.")
                input('Tekan enter untuk kembali...')
                return

        # Jika ID laporan ditemukan, tampilkan informasi laporan
        if laporan_data[prev][0] == id_laporan:
            print("Laporan ditemukan:")
            table = PrettyTable()
            table.field_names = ["ID Informasi", "Tanggal dan Waktu", "Judul Informasi", "Deskripsi Informasi"]
            table.add_row([laporan_data[prev][0], laporan_data[prev][3], laporan_data[prev][4], laporan_data[prev][5]])
            print(table)
        else:
            print("Laporan tidak ditemukan.")

        input('Tekan enter untuk kembali...')

    def quicksort_asc(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less_than_pivot = [x for x in arr[1:] if x[4] < pivot[4]]
            greater_than_pivot = [x for x in arr[1:] if x[4] >= pivot[4]]
            return self.quicksort_asc(less_than_pivot) + [pivot] + self.quicksort_asc(greater_than_pivot)

    def quicksort_desc(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less_than_pivot = [x for x in arr[1:] if x[4] > pivot[4]]
            greater_than_pivot = [x for x in arr[1:] if x[4] <= pivot[4]]
            return self.quicksort_desc(less_than_pivot) + [pivot] + self.quicksort_desc(greater_than_pivot)

    def menyorting_laporan_by_title_ascending(self):
        clear()

        # Mendapatkan data laporan dari database
        query_get_laporan = "SELECT * FROM informasi"
        self.cursor.execute(query_get_laporan)
        laporan_data = self.cursor.fetchall()

        # Sorting data menggunakan Quick Sort secara ascending berdasarkan judul informasi
        sorted_laporan = self.quicksort_asc(laporan_data)

        # Menampilkan data laporan yang sudah diurutkan secara ascending berdasarkan judul informasi menggunakan PrettyTable
        table = PrettyTable()
        table.field_names = ["ID Informasi", "ID Pelapor", "ID Admin", "Tanggal dan Waktu", "Judul Informasi", "Deskripsi Informasi"]
        for laporan in sorted_laporan:
            table.add_row(laporan)
        
        print("Data laporan setelah diurutkan secara ascending berdasarkan judul informasi:")
        print(table)
        input('Tekan enter untuk kembali...')

    def menyorting_laporan_by_title_descending(self):
        clear()

        # Mendapatkan data laporan dari database
        query_get_laporan = "SELECT * FROM informasi"
        self.cursor.execute(query_get_laporan)
        laporan_data = self.cursor.fetchall()

        # Sorting data menggunakan Quick Sort secara descending berdasarkan judul informasi
        sorted_laporan = self.quicksort_desc(laporan_data)

        # Menampilkan data laporan yang sudah diurutkan secara descending berdasarkan judul informasi menggunakan PrettyTable
        table = PrettyTable()
        table.field_names = ["ID Informasi", "ID Pelapor", "ID Admin", "Tanggal dan Waktu", "Judul Informasi", "Deskripsi Informasi"]
        for laporan in sorted_laporan:
            table.add_row(laporan)
        
        print("Data laporan setelah diurutkan secara descending berdasarkan judul informasi:")
        print(table)
        input('Tekan enter untuk kembali...')




## SECTION KOMUNITAS ##


def MelihatKomunitas():
    clear()
    # Mendapatkan data laporan dari database
    query_get_komunitas = "SELECT * FROM komunitas"
    cursor.execute(query_get_komunitas)
    komunitas_data = cursor.fetchall()

    # Menampilkan data laporan dengan PrettyTable
    table = PrettyTable()
    table.field_names = ["ID Komunitas", "Nama Komunitas", "Email", "F_ID_Admin", "Narahubung"]
    for komunitas in komunitas_data:
        table.add_row(komunitas)
    
    print(table)
    input('Tekan enter untuk kembali...')



##  SECTION KEGIATAN ##


def MelihatKegiatan():
    clear()
    # Mendapatkan data laporan dari database
    query_get_kegiatan = "SELECT * FROM kegiatan"
    cursor.execute(query_get_kegiatan)
    kegiatan_data = cursor.fetchall()

    # Menampilkan data laporan dengan PrettyTable
    table = PrettyTable()
    table.field_names = ["ID Kegiatan", "F ID Admin", "Judul Kegiatan", "Deskripsi Kegiatan", "Lokasi Kegiatan"]
    for kegiatan in kegiatan_data:
        table.add_row(kegiatan)
    
    print(table)
    input('Tekan enter untuk kembali...')

def MengeditKegiatan(cursor):
    clear()
    print('╔══════════════════════════════════════════╗')
    print('|          -- MENGEDIT KEGIATAN --         |')
    print('╚══════════════════════════════════════════╝')
    id_kegiatan = int(input("Masukkan ID Kegiatan yang ingin diedit: "))
    
    # Cek apakah kegiatan ada dalam database
    query_check_kegiatan = "SELECT * FROM kegiatan WHERE ID_Kegiatan = %s"
    cursor.execute(query_check_kegiatan, (id_kegiatan,))
    kegiatan_exists = cursor.fetchone()

    if kegiatan_exists:
        # Meminta input pengguna untuk data yang akan diedit
        judul_baru = input("Masukkan judul kegiatan yang baru: ")
        deskripsi_baru = input("Masukkan deskripsi kegiatan yang baru: ")

        # Update data kegiatan di database
        query_update_kegiatan = "UPDATE kegiatan SET Judul_Kegiatan = %s, Deskripsi_Kegiatan = %s WHERE ID_Kegiatan = %s"
        cursor.execute(query_update_kegiatan, (judul_baru, deskripsi_baru, id_kegiatan))
        mydb.commit()

        print("Kegiatan berhasil diperbarui!")
    else:
        print("Kegiatan tidak ditemukan.")
        input('Tekan enter untuk kembali...')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

class KegiatanManager:
    def __init__(self, cursor):
        self.cursor = cursor

    def jump_search_kegiatan_by_id(self):
        clear()
        id_kegiatan = int(input("Masukkan ID Kegitan yang ingin Anda cari: "))

        # Mendapatkan data kegiatan dari database
        query_get_kegiatan = "SELECT * FROM kegiatan"
        self.cursor.execute(query_get_kegiatan)
        kegiatan_data = self.cursor.fetchall()

        # Memasukkan data kegiatan ke dalam linked list
        linked_list = LinkedList()
        for kegiatan in kegiatan_data:
            linked_list.insert(kegiatan)

        # Mengurutkan data kegiatan berdasarkan ID_Kegitan
        kegiatan_data.sort(key=lambda x: x[0])

        n = len(kegiatan_data)
        step = int(n ** 0.5)  # Step size untuk jump search
        prev = 0
        while kegiatan_data[min(step, n)-1][0] < id_kegiatan:
            prev = step
            step += int(n ** 0.5)
            if prev >= n:
                print("Kegiatan tidak ditemukan.")
                input('Tekan enter untuk kembali...')
                return

        # Melakukan linear search pada blok yang relevan
        while kegiatan_data[prev][0] < id_kegiatan:
            prev += 1
            if prev == min(step, n):
                print("Kegiatan tidak ditemukan.")
                input('Tekan enter untuk kembali...')
                return

        # Jika ID kegiatan ditemukan, tampilkan informasi kegiatan
        if kegiatan_data[prev][0] == id_kegiatan:
            print("Kegiatan ditemukan:")
            table = PrettyTable()
            table.field_names = ["ID Kegiatan", "Judul Kegiatan", "Deskripsi Kegiatan", "Lokasi Kegiatan"]
            table.add_row([kegiatan_data[prev][0], kegiatan_data[prev][2], kegiatan_data[prev][3], kegiatan_data[prev][4]])
            print(table)
        else:
            print("Kegiatan tidak ditemukan.")

        input('Tekan enter untuk kembali...')

    def quicksort_asc(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less_than_pivot = [x for x in arr[1:] if x[4] < pivot[4]]
            greater_than_pivot = [x for x in arr[1:] if x[4] >= pivot[4]]
            return self.quicksort_asc(less_than_pivot) + [pivot] + self.quicksort_asc(greater_than_pivot)

    def quicksort_desc(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less_than_pivot = [x for x in arr[1:] if x[4] > pivot[4]]
            greater_than_pivot = [x for x in arr[1:] if x[4] <= pivot[4]]
            return self.quicksort_desc(less_than_pivot) + [pivot] + self.quicksort_desc(greater_than_pivot)

    def menyorting_kegiatan_by_title_ascending(self):
        clear()

        # Mendapatkan data kegiatan dari database
        query_get_kegiatan = "SELECT * FROM kegiatan"
        self.cursor.execute(query_get_kegiatan)
        kegiatan_data = self.cursor.fetchall()

        # Sorting data menggunakan Quick Sort secara ascending berdasarkan judul kegiatan
        sorted_kegiatan = self.quicksort_asc(kegiatan_data)

        # Menampilkan data kegiatan yang sudah diurutkan secara ascending berdasarkan judul kegiatan menggunakan PrettyTable
        table = PrettyTable()
        table.field_names = ["ID Kegiatan", "ID Admin", "Judul Kegiatan", "Deskripsi Kegiatan", "Lokasi Kegiatan"]
        for kegiatan in sorted_kegiatan:
            table.add_row(kegiatan)
        
        print("Data kegiatan setelah diurutkan secara ascending berdasarkan judul kegiatan:")
        print(table)
        input('Tekan enter untuk kembali...')

    def menyorting_kegiatan_by_title_descending(self):
        clear()

        # Mendapatkan data kegiatan dari database
        query_get_kegiatan = "SELECT * FROM kegiatan"
        self.cursor.execute(query_get_kegiatan)
        kegiatan_data = self.cursor.fetchall()

        # Sorting data menggunakan Quick Sort secara descending berdasarkan judul kegiatan
        sorted_kegiatan = self.quicksort_desc(kegiatan_data)

        # Menampilkan data kegiatan yang sudah diurutkan secara descending berdasarkan judul kegiatan menggunakan PrettyTable
        table = PrettyTable()
        table.field_names = ["ID Kegiatan", "ID Admin", "Judul Kegiatan", "Deskripsi Kegiatan", "Lokasi Kegiatan"]
        for kegiatan in sorted_kegiatan:
            table.add_row(kegiatan)
        
        print("Data kegiatan setelah diurutkan secara descending berdasarkan judul kegiatan:")
        print(table)
        input('Tekan enter untuk kembali...')

def MenghapusKegiatan(cursor):
    clear()
    print('╔══════════════════════════════════════════╗')
    print('|         -- MENGHAPUS KEGIATAN --         |')
    print('╚══════════════════════════════════════════╝')
    id_kegiatan = int(input("Masukkan ID Kegiatan yang ingin dihapus: "))
    
    # Cek apakah kegiatan ada
    query_check_kegiatan = "SELECT * FROM kegiatan WHERE ID_Kegiatan = %s"
    cursor.execute(query_check_kegiatan, (id_kegiatan,))
    kegiatan_exists = cursor.fetchone()

    if not kegiatan_exists:
        print('╔══════════════════════════════════════════╗')
        print('|        KEGIATAN TIDAK DITEMUKAN          |')
        print('╚══════════════════════════════════════════╝')
        input('Tekan enter untuk kembali...')
        return

    # Hapus semua komentar yang terkait
    query_delete_comments = "DELETE FROM komentar WHERE F_ID_Kegiatan = %s"
    cursor.execute(query_delete_comments, (id_kegiatan,))

    # Hapus kegiatan
    query_delete_kegiatan = "DELETE FROM kegiatan WHERE ID_Kegiatan = %s"
    cursor.execute(query_delete_kegiatan, (id_kegiatan,))

    print('╔══════════════════════════════════════════╗')
    print('|        KEGIATAN BERHASIL DI HAPUS        |')
    print('╚══════════════════════════════════════════╝')
    input('Tekan enter untuk kembali...')

def get_admin_id_by_username(cursor, username):
    query = "SELECT ID_Admin FROM Admin WHERE Username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def TambahKegiatan(cursor, mydb, Username):
    clear()
    print('╔══════════════════════════════════════════╗')
    print('|        -- MENAMBAHKAN KEGIATAN --        |')
    print('╚══════════════════════════════════════════╝')
    try:
        F_ID_Admin = get_admin_id_by_username(cursor, Username)
        if not F_ID_Admin:
            print('╔══════════════════════════════════════════╗')
            print('|           ADMIN TIDAK DITEMUKAN          |')
            print('╚══════════════════════════════════════════╝')
            return
        judul_kegiatan = input('Masukkan Judul Kegiatan: ')
        if len(judul_kegiatan) <= 200:
            deskripsi_kegiatan = input('Masukkan Deskripsi Kegiatan: ')
            if len(deskripsi_kegiatan) <= 500:
                lokasi_kegiatan = input('Masukkan Lokasi Kegiatan: ')
                if len(lokasi_kegiatan) <= 100:
                    # Menambahkan kegiatan ke dalam database
                    query_add_kegiatan = "INSERT INTO kegiatan (F_ID_Admin, Judul_Kegiatan, Deskripsi_Kegiatan, Lokasi_Kegiatan) VALUES (%s, %s, %s, %s)"
                    cursor.execute(query_add_kegiatan, (F_ID_Admin, judul_kegiatan, deskripsi_kegiatan, lokasi_kegiatan))
                    mydb.commit()
                    print("Kegiatan berhasil ditambahkan!")
                else:
                    print('Lokasi tidak boleh lebih dari 100 karakter...')
                    input('Tekan enter untuk kembali..')
            else:
                print('Deskripsi tidak boleh lebih dari 500 karakter...')
                input('Tekan enter untuk kembali..')
        else:
            print('Judul tidak boleh lebih dari 200 karakter...')
            input('Tekan enter untuk kembali..')
    except Exception as e:
        print("Error:", e)
        input('Tekan enter untuk kembali..')
