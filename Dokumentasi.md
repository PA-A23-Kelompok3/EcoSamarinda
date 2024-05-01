# EcoSamarinda
---
### Deskripsi Program

> Program Aplikasi EcoSamarinda adalah sebuah program inovatif yang bertujuan untuk meningkatkan partisipasi masyarakat dalam pelestarian lingkungan di Kota Samarinda. Aplikasi ini dirancang untuk memungkinkan masyarakat secara langsung melaporkan masalah lingkungan yang mereka temui kepada pemerintah daerah. Dengan menggunakan EcoSamarinda, masyarakat dapat dengan mudah menyampaikan informasi tentang berbagai masalah lingkungan seperti sampah, pencemaran air atau udara, kerusakan hutan, dan lain sebagainya.

> Program ini dibuat dengan menggunakan bahasa pemrograman Python dan mengimplementasikan struktur data Linked List. Aplikasi peminjaman ruang kelas ini juga menggunakan sebuah database, yaitu database MySQL yang digunakan untuk menyimpan data Admin, Informasi, Kegiatan, Komentar, Komunitas, Pelapor, Pengguna
---
### Struktur Project
> 1. Folder Controller, berisi file-file controller yang akan mengatur alur program serta mengambil data dari model dan menampilkan ke view.
> - File Controller Admin, sebagai file controller yang berisi logika untuk manajemen login akun Admin 
> - File Controller Komunitas, sebagai file controller yang berisi logika untuk manajemen data Komunitas dalam bentuk linked list, dimana data dalam linked list diambil dari database.
> - File Controller Pelapor, sebagai file controller yang berisi logika untuk manajemen data Pelapor dalam bentuk linked list seperti Registrasi, Login, dan Membuat Laporan
> - File Controller Pengguna, sebagai file controller yang berisi logika untuk manajemen akun Pengguna dalam bentuk linked list seperti Registrasi, Login, serta menampilkan data Pengguna

> 2. Folder Model, berisi file-file model yang berisi fungsi-fungsi untuk mengakses database dan memproses data.
> - File Database, sebagai file yang berisi class untuk menghubungkan python dan database.

> 3. Folder View, berisi file-file view yang berisi tampilan antarmuka aplikasi yang akan dilihat oleh pengguna.
> - File Tampilan_Admin, sebagai halaman untuk menampilkan keseluruhan informasi dari Melihat Laporan, Kegiatan serta Melihat, Mengedit, Mencari, Menyorting, Membuat dan Menghapus Laporan atau Kegiatan. 
> - File Tampilan_Komunitas, sebagai halaman untuk menampilkan informasi dari Komunitas
> - File Tampilan_Main, sebagai halaman untuk menampilkan ucapan selamat datang di program, serta memberi pilihan menu
> - File Tampilan_Pelapor, sebagai halaman untuk Registrasi dan Melakukan Pelaporan
> - File Tampilan_Pengguna, sebagai halaman untuk Registrasi dan Melihat Kegiatan/Komunitas.

> 4. File main, sebagai file utama yang berfungsi untuk menjalankan program.
---
### Fitur dan Fungsionalitas 

Pada program ini terdapat modul library yang digunakan, seperti :
> 1. import mysql.connector: Baris ini mengimpor modul mysql.connector, yang menyediakan fungsi untuk terhubung dan berinteraksi dengan database MySQL di Python.
> 2. import prettytable berguna ketika perlu menampilkan data dalam format tabel di konsol atau dalam laporan teks.
> 3. import datetime adalah modul bawaan dalam Python yang menyediakan kelas dan fungsi untuk bekerja dengan tanggal dan waktu.
> 4. import getpass digunakan untuk menerima input password dari pengguna tanpa menampilkan input yang diketikkan ke layar.
> 5. import os adalah modul bawaan dalam Python yang menyediakan berbagai fungsi untuk berinteraksi dengan sistem operasi yang sedang digunakan
---
## Penjelasan Program

### Model
- Model - Database.py
```
import mysql.connector

def connect_database():
    try:
        mydb = mysql.connector.connect (
            host = "localhost",
            user = "root",
            password = "",
            database = "ecosamarinda"
        )
        cursor = mydb.cursor()
        return mydb, cursor
    except mysql.connector.Error as err:
        print(F"Error: {err}")
        return None, None
```
Kode diatas adalah bagian dari sebuah fungsi bernama connect_database() yang bertujuan untuk menghubungkan ke database MySQL menggunakan modul mysql.connector dalam bahasa pemrograman Python.

---

### View
- View - Tampilan_Admin.py
```
from View import Tampilan_Main as main
from Controller import Admin_Controller as admin
from Controller.Admin_Controller import LaporanManager
from Controller.Admin_Controller import KegiatanManager
from Model.Database import connect_database
import os

mydb, cursor = connect_database()

object = LaporanManager(cursor)
object2 = KegiatanManager(cursor)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def AwalAdmin():
    clear()
    print('╔═════════════════ PILIH MENU ════════════════╗')
    print("| [1] LOGIN                                 |")
    print('|                                           |')
    print("| [2] KELUAR                                |")
    print('╚═══════════════════════════════════════════╝')
    pilih = int(input("Masukkan pilihan Anda (1-2): "))
    if pilih == 1:
        admin.LoginAdmin()
    elif pilih == 2:
        main.main_menu()

def laporan(Username, cursor):
    while True:
        clear()
        print('╔═════════ Pilih Opsi Yang Anda Inginkan ═════════╗')
        print('| [1] Melihat Laporan                             |')
        print('|                                                 |')
        print('| [2] Mengedit Laporan                            |')
        print('|                                                 |')
        print('| [3] Mencari Laporan                             |')
        print('|                                                 |')
        print('| [4] Menyorting Laporan (Berdasarkan Judul)      |')
        print('|                                                 |')
        print('| [5] Kembali                                     |')
        print('╚═════════════════════════════════════════════════╝')
        masukan = int(input("Masukkan pilihan Anda (1-5): "))
        if masukan == 1:
            admin.MelihatLaporan()
        elif masukan == 2:
            admin.MengeditLaporan()
        elif masukan == 3:
            object.jump_search_laporan_by_id()
        elif masukan == 4:
            clear()
            print('╔══════ MENU SORTING (BERDASARKAN JUDUL) ══════╗')
            print("| [1] SORTING ASCENDING                        |")
            print('|                                              |')
            print("| [2] SORTING DESCENDING                       |")
            print('|                                              |')
            print("| [3] Kembali                                  |")
            print('╚══════════════════════════════════════════════╝')
            pilihan = int(input('Masukkan pilihan Anda (1-3): '))
            if pilihan == 1:
                object.menyorting_laporan_by_title_ascending()
            elif pilihan == 2:
                object.menyorting_laporan_by_title_descending()
            elif pilihan == 3:
                continue
        elif masukan == 5:
            menu_admin(Username, cursor)

def kegiatan(Username, cursor):
    while True:
        clear()
        print('╔═══════ Pilih Opsi Yang Anda Inginkan ═══════╗')
        print('| [1] Membuat Kegiatan                        |')
        print('|                                             |')
        print('| [2] Melihat Kegiatan                        |')
        print('|                                             |')
        print('| [3] Mengedit Kegiatan                       |')
        print('|                                             |')
        print('| [4] Mencari Kegiatan                        |')
        print('|                                             |')
        print('| [5] Menyorting Laporan                      |')
        print('|                                             |')
        print('| [6] Menghapus Kegiatan                      |')
        print('|                                             |')
        print('| [7] Kembali                                 |')
        print('╚═════════════════════════════════════════════╝')
        masukan = int(input("Masukkan pilihan Anda (1-6): "))
        if masukan == 1 :
            admin.TambahKegiatan(cursor, mydb, Username)
        elif masukan == 2:
            admin.MelihatKegiatan()
        elif masukan == 3:
            admin.MengeditKegiatan(cursor)
        elif masukan == 4:
            object2.jump_search_kegiatan_by_id()
        elif masukan == 5:
            clear()
            print('╔═════ MENU SORTING (BERDASARKAN JUDUL) ═════╗')
            print("| [1] SORTING ASCENDING                      |")
            print('|                                            |')
            print("| [2] SORTING DESCENDING                     |")
            print('|                                            |')
            print("| [3] Kembali                                |")
            print('╚════════════════════════════════════════════╝')
            pilihan = int(input('Masukkan pilihan Anda (1-3): '))
            if pilihan == 1:
                object2.menyorting_kegiatan_by_title_ascending()
            elif pilihan == 2:
                object2.menyorting_kegiatan_by_title_descending()
            elif pilihan == 3:
                continue
        elif masukan == 6:
            admin.MenghapusKegiatan(cursor)
        menu_admin(Username, cursor)

def menu_admin(Username, cursor):
    while True:
        clear()
        print(f"~~Selamat datang {Username}~~")
        print('╔═════ Pilih Opsi Yang Anda Inginkan ═════╗')
        print('| [1] Laporan                             |')
        print('|                                         |')
        print('| [2] Kegiatan                            |')
        print('|                                         |')
        print('| [3] Lihat Komunitas                     |')
        print('|                                         |')
        print('| [4] Kembali                             |')
        print('╚═════════════════════════════════════════╝')
        pilih = int(input("Masukkan pilihan Anda (1-4): "))
        if pilih == 1:
            laporan(Username, cursor)
        elif pilih == 2:
            kegiatan(Username, cursor)
        elif pilih == 3:
            admin.MelihatKomunitas()
        elif pilih == 4:
            AwalAdmin()
```
---

Kode diatas adalah bagian dari program Python yang menyediakan antarmuka untuk administrasi. Ini mulai dengan mengimpor modul dan objek yang diperlukan, terhubung ke database MySQL, dan kemudian menawarkan menu-menu kepada admin, seperti mengelola laporan dan kegiatan. Setiap opsi dalam menu diproses dengan memanggil fungsi-fungsi terkait yang telah didefinisikan sebelumnya. Program ini terus berjalan dalam loop hingga admin memilih untuk keluar.

- View - Tampilan_Main.py
```

from View import Tampilan_Pelapor as pelapor
from View import Tampilan_Admin as adminn
from View import Tampilan_Pengguna as pengguna
from Controller import Admin_Controller as admin
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    while True:
        clear()
        print("╔═══════════════════════════════════════════╗")
        print("|            Selamat datang di              |")
        print("|               EcoSamarinda                |")
        print('╠═══════════════════════════════════════════╣')
        print("|[1] Pelapor                                |")
        print('|                                           |')
        print("|[2] Pengguna                               |")
        print('|                                           |')
        print("|[3] Admin                                  |")
        print('|                                           |')
        print("|[4] Keluar                                 |")
        print('╚═══════════════════════════════════════════╝')
        try:
            pilihan = int(input("Silakan pilih menu yang ingin Anda akses:"))
            if pilihan == 1:
                pelapor.menuPelapor()
            
            elif pilihan == 2:
                pengguna.menuPengguna()

            elif pilihan == 3:
                adminn.AwalAdmin()

            elif pilihan == 4:
                print("Anda telah keluar dari EcoSamarinda, terima kasih!")
                break

            else:
                print("Pilihan tidak valid.")
                main_menu()

        except ValueError:
            print("Pilihan harus berupa angka.")
            main_menu()


if __name__ == "__main__":
    main_menu()
```
Kode diatas merupakan program utama yang menyediakan menu utama untuk pengguna EcoSamarinda. Setelah membersihkan layar, program akan menampilkan menu dengan opsi untuk masuk sebagai pelapor, pengguna, atau admin. Setiap opsi memiliki fungsi yang berbeda untuk menangani permintaan pengguna. Program juga menangani input pengguna yang tidak valid dengan mencetak pesan kesalahan. Jika pengguna memilih untuk keluar, program akan berhenti.

- View - Tampilan_Pelapor.py
```
from Controller import Pelapor_Controller as pelapor
from View import Tampilan_Main as Main
import os
from Model.Database import connect_database
mydb, cursor = connect_database()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menuPelapor():
    clear()
    print('╔═════ Pilih Opsi Yang Anda Inginkan ═════╗')
    print('| [1] Registrasi                          |')
    print('| [2] Lapor                               |')
    print('| [3] Kembali                             |')
    print('╚══════════════════════════════════════════╝')
    pilihan = int(input('Masukkan Pilihan Anda: '))
    if pilihan == 1:
        pelapor.RegisPelapor(cursor, mydb)
    elif pilihan == 2:
        pelapor.LoginPelapor()
    elif pilihan == 3:
        Main.main_menu()

def menu_admin(nama_admin):
    while True:
        print("╔══════════════════════════════════════════════════════╗")
        print("║                    Memilih Menu                      ║")
        print("╠------------------------------------------------------╣")
        print("║  1. Laporan                                          ║")
        print("║  2. Kegiatan                                         ║")
        print("║  3. Keluar                                           ║")
        print("╚══════════════════════════════════════════════════════╝")
        pilih = input("Masukkan pilihan Anda (1-3): ")

        if pilih == '1':
            print(f"Selamat datang {nama_admin}")
            print("+-------------------------------+")
            print("|1.| Melihat Laporan Pengguna   |")
            print("|2.| Menghapus Laporan Pengguna |")
            print("|3.| Tanggapi Laporan Pengguna  |")
            print("+-------------------------------+")
            admin = input("Apa yang ingin Anda lakukan?: ")
            if admin == '1':
                # Proses melihat laporan pengguna
                pass
```

Kode diatas merupakan bagian dari program yang menangani interaksi antara pelapor dan admin. Fungsi menuPelapor() menampilkan opsi untuk pelapor, seperti registrasi dan login. Fungsi menu_admin(nama_admin) menampilkan opsi untuk admin, tetapi implementasi aksi belum diberikan. Kedua fungsi memanfaatkan koneksi database yang sudah dibuat sebelumnya.

- View - Tampilan_Pengguna.py
```
from Controller import Pengguna_Controller as pengguna
from View import Tampilan_Main as Main
import os
from Model.Database import connect_database
mydb, cursor = connect_database()

def clear():
    os.system("cls" if os.name == "nt" else "clear")
print('Selamat datang, pengguna!')

def menuPengguna():
    clear()
    print('╔══════Pilih Opsi Yang Anda Inginkan═══════╗')
    print('| [1].Registrasi                           |')
    print('| [2].Lihat Kegiatan/Lihat Komunitas       |')
    print('| [3].Kembali                              |')
    print('╚══════════════════════════════════════════╝')
    pilihan = input('Masukkan Pilihan Anda: ')
    if pilihan == '1':
        pengguna.RegisPengguna(cursor, mydb)
    elif pilihan == '2':
        pengguna.LoginPengguna(cursor, mydb)
    elif pilihan == '3':
        Main.main_menu()

def UtamaPengguna():
    clear()
    print('Selamat datang, pengguna!')
    print('╔══════Pilih Opsi Yang Anda Inginkan═══════╗')
    print('| [1].Lihat Kegiatan                       |')
    print('|                                          |')
    print('| [2].Lihat Komunitas                      |')
    print('|                                          |')
    print('| [3].Lihat Komentar                       |')
    print('|                                          |')
    print('| [4].Kembali                              |')
    print('╚══════════════════════════════════════════╝')
    pilihan = int(input('Masukkan Pilihan Anda: '))
    if pilihan == 1:
        pengguna.LihatKegiatan(cursor, mydb)
    elif pilihan == 2:
        pengguna.LihatKomunitas(cursor, mydb)
    elif pilihan == 3:
        pengguna.MelihatKomentar()

def KomentarPengguna(cursor, ID, mydb):
    print('╔══════════════════════════════════════════╗')
    print('|     INGIN MEMBERIKAN KOMENTAR (Y/T)      |')
    print('╚══════════════════════════════════════════╝')
    pilihan = str(input('Masukkan Pilihan Anda: '))
    if pilihan == 'Y':
        pengguna.BerikanKomentar(cursor, ID, mydb)
    elif pilihan == 'T':
        UtamaPengguna()
```
Kode diatas merupakan bagian yang menangani interaksi pengguna dengan sistem. Fungsi menuPengguna() menampilkan opsi untuk pengguna, seperti registrasi atau login, dan memanggil fungsi terkait dari modul Pengguna_Controller. Setelah login, fungsi UtamaPengguna() menampilkan opsi tambahan, seperti melihat kegiatan atau komunitas. Fungsi KomentarPengguna() meminta pengguna untuk memberikan komentar terkait kegiatan atau topik tertentu.

---

### Controller
- Controller - Admin_Controller.py
```
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
        Username = input('Masukkan Username Anda:')
        if len(Username) <= 15:
            Password = input('Masukkan Password Anda:')
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
```
Fungsi LoginAdmin() memungkinkan admin untuk masuk ke sistem EcoSamarinda dengan memvalidasi username dan password yang dimasukkan. Setelah meminta masukan username dan password, fungsi memeriksa panjang karakter keduanya. Jika melebihi batas, admin diminta memasukkan kembali. Selanjutnya, fungsi memeriksa kecocokan kredensial dengan yang ada di database. Jika kredensial valid, admin diarahkan ke menu admin; jika tidak, pesan kesalahan ditampilkan, dan admin diminta untuk mencoba lagi.

```
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
```
Fungsi MelihatLaporan() digunakan untuk menampilkan data laporan dari database. Pertama, fungsi membersihkan layar dengan clear(), kemudian mengambil data laporan dari database menggunakan query SQL. Data tersebut ditampilkan dalam bentuk tabel menggunakan pustaka PrettyTable. Setiap baris dari data laporan ditambahkan ke tabel, dan tabel tersebut kemudian dicetak ke layar. Setelah itu, fungsi menunggu pengguna menekan tombol enter sebelum kembali ke menu sebelumnya
```
def MengeditLaporan():
    clear()
    print('╔══════════════════════════════════════════╗')
    print('|          -- MENGEDIT LAPORAN --          |')
    print('╚══════════════════════════════════════════╝')
    id_laporan = int(input("Masukkan ID laporan yang ingin diedit: "))
```
Fungsi MengeditLaporan() memungkinkan admin untuk mengedit laporan yang sudah ada dalam database. Setelah membersihkan layar, fungsi mencetak header untuk menu pengeditan laporan. Kemudian, admin diminta untuk memasukkan ID laporan yang ingin diedit. Ini memulai proses pengeditan.

```
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
```
Kode tersebut mendefinisikan kelas LaporanManager, yang mengelola operasi terkait laporan dalam sistem EcoSamarinda. Fungsi jump_search_laporan_by_id() mengimplementasikan algoritma pencarian langkah melompat untuk mencari laporan berdasarkan ID. Fungsi menyorting_laporan_by_title_ascending() dan menyorting_laporan_by_title_descending() menggunakan algoritma quicksort untuk mengurutkan data laporan berdasarkan judul informasi secara naik dan turun. Ini memastikan pengguna dapat mencari dan mengurutkan laporan dengan mudah.


```
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
```
Fungsi MelihatKomunitas() digunakan untuk menampilkan data komunitas dari database. Pertama, fungsi membersihkan layar dengan clear(). Kemudian, query SQL digunakan untuk mengambil data komunitas dari tabel komunitas dalam database. Hasil query disimpan dalam variabel komunitas_data menggunakan metode cursor.fetchall(). Data komunitas kemudian ditampilkan dalam bentuk tabel menggunakan pustaka PrettyTable. Setiap baris dari data komunitas ditambahkan ke tabel menggunakan loop for. Terakhir, fungsi menunggu pengguna menekan tombol enter sebelum kembali ke menu sebelumnya. Dengan demikian, fungsi ini memungkinkan admin untuk melihat data komunitas secara terstruktur dan mudah dibaca.

```
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
```
Fungsi MelihatKegiatan() mengambil data kegiatan dari database, menampilkannya dalam tabel menggunakan PrettyTable, dan menunggu input dari pengguna sebelum kembali ke menu sebelumnya. Ini memungkinkan admin untuk dengan mudah melihat data kegiatan yang tersimpan dalam sistem.

```
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
```

Fungsi MengeditKegiatan(cursor) memungkinkan admin untuk mengedit informasi kegiatan yang sudah ada dalam database. Admin diminta untuk memasukkan ID kegiatan yang ingin diubah, kemudian memasukkan informasi baru tentang judul dan deskripsi kegiatan. Informasi yang baru dimasukkan akan diupdate dalam database. Jika kegiatan tidak ditemukan, pesan yang sesuai akan dicetak, dan admin diminta untuk menekan tombol enter sebelum kembali ke menu sebelumnya.

```
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
```

Fungsi MenghapusKegiatan(cursor) memungkinkan admin untuk menghapus kegiatan dari database. Admin diminta untuk memasukkan ID kegiatan yang ingin dihapus. Jika kegiatan tidak ditemukan, pesan yang sesuai dicetak, dan admin diminta untuk menekan tombol enter sebelum kembali ke menu sebelumnya. Jika kegiatan ditemukan, semua komentar terkait dihapus terlebih dahulu, kemudian kegiatan itu sendiri dihapus. Setelah kegiatan berhasil dihapus, pesan sukses dicetak, dan admin diminta untuk menekan tombol enter sebelum kembali ke menu sebelumnya.

```
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
```
Fungsi TambahKegiatan(cursor, mydb, Username) digunakan untuk menambahkan kegiatan baru ke dalam database. Admin diminta untuk memasukkan judul, deskripsi, dan lokasi kegiatan. Setiap input diperiksa untuk memastikan bahwa panjangnya sesuai dengan batasan yang ditetapkan dalam skema basis data. Jika panjang input melebihi batas, pesan kesalahan akan dicetak, dan admin diminta untuk menekan tombol enter sebelum kembali ke menu sebelumnya.

- Controller - Pelapor_Controller.py

```
from Model.Database import connect_database
from View import Tampilan_Pelapor as pelapor
from View import Tampilan_Main as Main
import os
from prettytable import PrettyTable

#CLASS UNTUK PELAPOR

class PelaporNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class PelaporLinkedList:
    def __init__(self):
        self.head = None

    def add_pelapor(self, pelapor_data):
        new_node = PelaporNode(pelapor_data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


def clear():
    os.system("cls" if os.name == "nt" else "clear")

mydb, cursor = connect_database()



def RegisPelapor(cursor, mydb):
    linked_list = PelaporLinkedList()  # Membuat objek linked list di dalam fungsi
    try:
        nama_pelapor = str(input('Masukkan Nama Anda: '))
        if len(nama_pelapor) <= 30:
            alamat_pelapor = input('Masukkan Alamat Anda: ')
            if len(alamat_pelapor) <= 50:
                kontak_pelapor = input('Masukkan Kontak Anda: ')
                if len(kontak_pelapor) <= 13:
                    clear()
                    # Periksa apakah nomor HP sudah terdaftar di database
                    query_check_hp = "SELECT * FROM pelapor WHERE No_HP = %s"
                    cursor.execute(query_check_hp, (kontak_pelapor,))
                    existing_hp = cursor.fetchone()

                    if existing_hp:
                        print('╔═══════════════════════════════════════════╗')
                        print("|       -- NOMOR HP SUDAH TERDAFTAR --       |")
                        print('╚═══════════════════════════════════════════╝')
                        input('Tekan enter untuk kembali...')
                        pelapor.menuPelapor()
                        return

                    # Jika nomor HP belum terdaftar, lakukan registrasi
                    query = "INSERT INTO pelapor (Nama_Pelapor, No_HP, Alamat) VALUES (%s, %s, %s)"
                    cursor.execute(query, (nama_pelapor, kontak_pelapor, alamat_pelapor))
                    mydb.commit()

                    # Menampilkan akun pelapor yang baru diregistrasi beserta ID pelapornya
                    query_id = "SELECT * FROM pelapor WHERE Nama_Pelapor = %s AND No_HP = %s AND Alamat = %s"
                    cursor.execute(query_id, (nama_pelapor, kontak_pelapor, alamat_pelapor))
                    pelapor_baru = cursor.fetchone()

                    # Menambahkan data pelapor baru ke dalam linked list
                    linked_list.add_pelapor(pelapor_baru)

                    # Menampilkan hasil dengan PrettyTable
                    table = PrettyTable()
                    table.field_names = ["ID Pelapor", "Nama", "No HP", "Alamat"]
                    table.add_row([pelapor_baru[0], pelapor_baru[1], pelapor_baru[2], pelapor_baru[3]])
                    print(table)

                    input('Tekan enter untuk kembali...')
                    pelapor.menuPelapor()
                else:
                    print('Nomor HP tidak boleh lebih dari 13...')
                    input('Tekan enter untuk kembali..')
                    Main.main_menu()
            else:
                print('Alamat tidak boleh lebih dari 50...')
                input('Tekan enter untuk kembali..')
                Main.main_menu()
        else:
            print('Nama tidak boleh lebih dari 30...')
            input('Tekan enter untuk kembali..')
            Main.main_menu()
    except KeyboardInterrupt:
        print("\nRegistrasi dibatalkan. Tekan Ctrl + Z atau input exit untuk kembali ke menu.")
        return
    except ValueError:
        print("Harap masukkan angka!")
        return
    except Exception as e:
        print(f"Error: {e}")
        return
    except:
        clear()
        print('╔═══════════════════════════════════════════╗')
        print("|              KESALAHAN INPUT              |")
        print("|       MOHON PERHATIKAN INPUTAN ANDA       |")
        print('╚═══════════════════════════════════════════╝')
        input('Tekan enter untuk kembali...')
        pelapor.menuPelapor()
```
Fungsi RegisPelapor(cursor, mydb) digunakan untuk melakukan registrasi pelapor baru. Pelapor diminta untuk memasukkan nama, alamat, dan nomor kontaknya. Setiap input diperiksa untuk memastikan bahwa panjangnya sesuai dengan batasan yang ditetapkan dalam skema basis data. Jika panjang input melebihi batas, pesan kesalahan akan dicetak, dan pelapor diminta untuk menekan tombol enter sebelum kembali ke menu sebelumnya.

Jika nomor kontak pelapor sudah terdaftar dalam database, pesan yang sesuai akan dicetak, dan registrasi akan dibatalkan. Jika registrasi berhasil, informasi akun pelapor baru akan dicetak menggunakan PrettyTable, dan pelapor akan kembali ke menu utama setelah menekan tombol enter. Dalam kasus terjadi kesalahan, pesan error akan dicetak bersama dengan informasi yang spesifik tentang kesalahan yang terjadi.

```
def LoginPelapor():
    try:
        id_pelapor = int(input('Masukkan ID Anda: '))
        if len(str(id_pelapor)) <= 5:
            nama_pelapor = (input('Masukkan Nama Anda:'))
            if len(nama_pelapor) <= 30:
                query = "SELECT * FROM pelapor WHERE Id_Pelapor = %s AND Nama_Pelapor = %s"
                cursor.execute(query, (id_pelapor, nama_pelapor))
                hasil = cursor.fetchone()
                if hasil:
                    InputInformasi(cursor, mydb, id_pelapor)
                else:
                    clear()
                    print('╔═══════════════════════════════════════════╗')
                    print("|       DATA YANG ANDA MASUKKAN SALAH       |")
                    print('╚═══════════════════════════════════════════╝')
                    input('Tekan enter untuk kembali...')
                    pelapor.menuPelapor()
            else:
                print('Nama tidak boleh lebih dari 30...')
                input('Tekan enter untuk kembali..')
                Main.main_menu()
        else:
            print('ID tidak boleh lebih dari 4...')
            input('Tekan enter untuk kembali..')
            Main.main_menu()
    except ValueError:
            print("Harap masukkan angka untuk ID Anda!")
    except KeyboardInterrupt:
        print("Proses login dibatalkan oleh pengguna.")
    except Exception as e:
        print(f"Error: {e}")
```

Fungsi LoginPelapor() digunakan untuk memungkinkan pelapor masuk ke akun mereka. Pertama-tama, mereka diminta memasukkan ID dan nama mereka. Panjang input ID dan nama diperiksa untuk memastikan bahwa sesuai dengan batasan yang ditetapkan dalam skema basis data. Jika panjang input melebihi batas, pesan kesalahan sesuai akan dicetak, dan pelapor diminta untuk menekan tombol enter sebelum kembali ke menu sebelumnya.

```
import random

def InputInformasi(cursor, mydb, id_pelapor):
    try:
        clear()
        print('╔════════════════════════════════╗')
        print("|      -- INPUT INFORMASI --     |")
        print('╚════════════════════════════════╝')
        tanggal = input("Masukkan tanggal Laporan (YYYY-MM-DD): ")
        if len(tanggal) == 10:
            JudulInformasi = input('Masukkan Judul Laporan Anda:')
            if len(JudulInformasi) <= 200:
                DeskripsiInformasi = input('Masukkan Deskripsi Laporan Anda:')
                if len(DeskripsiInformasi) <= 500:
                    # Mendapatkan ID admin secara acak dari database
                    query_get_admin_ids = "SELECT ID_Admin FROM admin"
                    cursor.execute(query_get_admin_ids)
                    admin_ids = cursor.fetchall()

                    # Memilih secara acak ID admin dari daftar
                    random_admin_id = random.choice(admin_ids)[0]

                    F_ID_Pelapor = id_pelapor
                    query = "INSERT INTO informasi (F_ID_Pelapor, F_ID_Admin, Tanggal_Waktu, Judul_Informasi, Deskripsi_Informasi) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(query, (F_ID_Pelapor, random_admin_id, tanggal, JudulInformasi, DeskripsiInformasi))
                    mydb.commit()
                    input('Informasi berhasil dimasukkan. Tekan enter untuk kembali...')
                    Main.main_menu()  # Kembali ke menu utama
                else:
                    print('Deskripsi tidak boleh lebih dari 500...')
                    input('Tekan enter untuk kembali..')
                    Main.main_menu()  # Kembali ke menu utama
            else:
                print('Judul tidak boleh lebih dari 200...')
                input('Tekan enter untuk kembali..')
                Main.main_menu()  # Kembali ke menu utama
        else:
            print('Format tanggal salah. Masukkan tanggal dengan format YYYY-MM-DD...')
            input('Tekan enter untuk kembali..')
            Main.main_menu()  # Kembali ke menu utama
    except KeyboardInterrupt:
        print("\nInput dibatalkan. Tekan Ctrl + Z atau input 'exit' untuk kembali ke menu.")
        Main.main_menu()
    except ValueError as ve:
        print(f"Error: {ve}")
        input('Tekan enter untuk kembali..')
        Main.main_menu()  # Kembali ke menu utama
    except Exception as e:
        print(f"Error: {e}")
        input('Tekan enter untuk kembali..')
        Main.main_menu()  # Kembali ke menu utama
```
Fungsi InputInformasi digunakan untuk memungkinkan pengguna (dalam hal ini, pelapor) memasukkan informasi baru ke dalam sistem. Prosesnya dimulai dengan membersihkan layar dan mencetak header untuk input informasi. Kemudian, pengguna diminta memasukkan tanggal laporan, judul informasi, dan deskripsi informasi.

Setelah validasi input, fungsi memilih secara acak ID admin dari database untuk mengasumsikan bahwa informasi akan ditinjau oleh admin yang berbeda secara acak. Kemudian, informasi yang dimasukkan oleh pelapor disimpan dalam tabel informasi basis data.

Jika pengguna membatalkan input dengan menekan Ctrl + Z atau memasukkan 'exit', mereka akan diarahkan kembali ke menu utama. Dalam kasus terjadi kesalahan lain, pesan error akan dicetak, dan pengguna akan diminta menekan tombol enter sebelum kembali ke menu utama.

- Controller - Admin_Controller.py

```
from View import Tampilan_Pengguna as pengguna
from View import Tampilan_Main as Main
from Model.Database import connect_database
from prettytable import PrettyTable
from datetime import datetime
import os

mydb, cursor = connect_database()

def clear():
    os.system("cls" if os.name == "nt" else "clear")


class PenggunaNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class PenggunaLinkedList:
    def __init__(self):
        self.head = None

    def add_pengguna(self, pengguna_data):
        new_node = PenggunaNode(pengguna_data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

## REGISPENGGUNA ##

def RegisPengguna(cursor, mydb):
    linked_list = PenggunaLinkedList()  # Membuat objek linked list di dalam fungsi
    Username = input('Masukkan Username yang anda inginkan:')
    if len(Username) <= 15:
        Password = input('Masukkan Password yang anda inginkan:')
        if len(Password) <= 20:
            email = input('Masukkan Email yang anda inginkan:')
            if len(email) <= 40:
                clear()
                
                # Periksa apakah email sudah terdaftar di database
                query_check_email = "SELECT * FROM pengguna WHERE email = %s"
                cursor.execute(query_check_email, (email,))
                existing_email = cursor.fetchone()
                
                if existing_email:
                    print('╔══════════════════════════════════════════╗')
                    print("|        -- EMAIL SUDAH TERDAFTAR --       |")
                    print('╚══════════════════════════════════════════╝')
                    input('Tekan enter untuk kembali...')
                    cursor.fetchall()
                    pengguna.menuPengguna()
                    return
                
                # Jika email belum terdaftar, lakukan registrasi
                query_insert_pengguna = "INSERT INTO pengguna (Username, Password, email) VALUES (%s, %s, %s)"
                cursor.execute(query_insert_pengguna, (Username, Password, email))
                mydb.commit()

                # Menampilkan akun pengguna yang baru diregistrasi beserta ID penggunanya
                query_id = "SELECT * FROM pengguna WHERE Username = %s AND Password = %s AND Email = %s"
                cursor.execute(query_id, (Username, Password, email))
                pengguna_baru = cursor.fetchone()

                # Menambahkan data pengguna baru ke dalam linked list
                linked_list.add_pengguna(pengguna_baru)

                # Menampilkan hasil dengan PrettyTable
                table = PrettyTable()
                table.field_names = ["ID Pengguna", "Username", "Password", "Email"]
                table.add_row([pengguna_baru[0], pengguna_baru[1], pengguna_baru[2], pengguna_baru[3]])
                print(table)

                input('Tekan enter untuk kembali...')
                cursor.fetchall()
                pengguna.menuPengguna()
            else:
                print('Email tidak boleh lebih dari 40 karakter...')
                input('Tekan enter untuk kembali..')
                pengguna.menuPengguna()
        else:
            print('Password tidak boleh lebih dari 20 karakter...')
            input('Tekan enter untuk kembali..')
            pengguna.menuPengguna()
    else:
        print('Username tidak boleh lebih dari 15 karakter...')
        input('Tekan enter untuk kembali..')
        pengguna.menuPengguna()
```
Fungsi RegisPengguna adalah fungsi untuk mendaftarkan pengguna baru. Ini meminta pengguna memasukkan username, password, dan email, kemudian memvalidasi panjang masing-masing. Jika email belum terdaftar, pengguna akan didaftarkan dan informasinya ditampilkan menggunakan PrettyTable. Jika email sudah terdaftar, pesan kesalahan akan ditampilkan. Setelah itu, pengguna diminta untuk menekan tombol enter untuk kembali ke menu pengguna.

```
## LOGIN PENGGUNA ##

def LoginPengguna(cursor, mydb):
    # try:
        ID = int(input('Masukkan ID Anda: '))
        if len(str(ID)) <= 11:
            password = input('Masukkan Password Anda: ')
            if len(password) <= 20:
                query = "SELECT * FROM pengguna WHERE ID_Pengguna = %s AND Password = %s"
                cursor.execute(query, (ID, password))
                hasil = cursor.fetchone()
                if hasil:
                    pengguna.UtamaPengguna()
                    # Lakukan sesuatu setelah pengguna berhasil login
                else:
                    clear()
                    print('╔═══════════════════════════════════════════╗')
                    print("|       DATA YANG ANDA MASUKKAN SALAH       |")
                    print('╚═══════════════════════════════════════════╝')
                    input('Tekan enter untuk kembali...')
                    pengguna.menuPengguna()
            else:
                print('Password tidak boleh lebih dari 20 karakter...')
                input('Tekan enter untuk kembali..')
                pengguna.menuPengguna()
        else:
            print('Username tidak boleh lebih dari 15 karakter...')
            input('Tekan enter untuk kembali..')
            pengguna.menuPengguna()
    # except Exception as e:
    #     print(e)
        # clear()
        # print('╔═══════════════════════════════════════════╗')
        # print("|              KESALAHAN INPUT              |")
        # print("|       MOHON PERHATIKAN INPUTAN ANDA       |")
        # print('╚═══════════════════════════════════════════╝')
        # input('Tekan enter untuk kembali...')
        # pengguna.menuPengguna()
```
Fungsi LoginPengguna meminta pengguna untuk memasukkan ID dan password, kemudian memeriksa apakah kredensial tersebut cocok dengan data yang ada di database pengguna. Jika cocok, fungsi UtamaPengguna dari modul pengguna dipanggil, yang kemungkinan menampilkan menu utama atau melakukan tindakan lain setelah login berhasil. Jika tidak cocok, pesan kesalahan ditampilkan, dan pengguna diminta untuk menekan tombol enter untuk kembali ke menu pengguna.

```
class KegiatanNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class KegiatanLinkedList:
    def __init__(self):
        self.head = None

    def add_kegiatan(self, kegiatan_data):
        new_node = KegiatanNode(kegiatan_data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get_kegiatan_list(self):
        kegiatan_list = []
        current = self.head
        while current:
            kegiatan_list.append(current.data)
            current = current.next
        return kegiatan_list

def LihatKegiatan(cursor, ID):
    clear()

    # Membuat objek linked list
    kegiatan_list = KegiatanLinkedList()

    # Mendapatkan data kegiatan dari database
    query_get_kegiatan = "SELECT ID_Kegiatan, Judul_Kegiatan, Deskripsi_Kegiatan, Lokasi_Kegiatan FROM kegiatan"
    cursor.execute(query_get_kegiatan)
    kegiatan_data = cursor.fetchall()

    # Menambahkan data kegiatan ke dalam linked list
    for kegiatan in kegiatan_data:
        kegiatan_list.add_kegiatan(kegiatan)

    # Menampilkan data kegiatan dengan PrettyTable
    table = PrettyTable()
    table.field_names = ["ID Kegiatan", "Judul Kegiatan", "Deskripsi Kegiatan", "Lokasi Kegiatan"]
    for kegiatan in kegiatan_list.get_kegiatan_list():
        table.add_row(kegiatan)
    
    print(table)
    pengguna.KomentarPengguna(cursor, ID, mydb)
```
Fungsi LihatKegiatan bertanggung jawab untuk menampilkan kegiatan dari database. Pertama, ia mengambil data kegiatan dari database dan menambahkannya ke dalam linked list menggunakan objek KegiatanLinkedList. Kemudian, menggunakan PrettyTable, data kegiatan tersebut ditampilkan dalam bentuk tabel. Setelah itu, fungsi KomentarPengguna dari modul pengguna dipanggil dengan menyediakan kursor, ID pengguna, dan koneksi database untuk memberikan opsi kepada pengguna untuk memberikan komentar pada kegiatan tersebut.


```
## LIHAT KOMUNITAS ##


def LihatKomunitas(cursor, mydb):
    clear()

    # Mendapatkan data komunitas dari database
    query_get_komunitas = "SELECT Nama_Komunitas, Email, Narahubung FROM komunitas"
    cursor.execute(query_get_komunitas)
    komunitas_data = cursor.fetchall()

    # Menampilkan data komunitas dengan PrettyTable
    table = PrettyTable()
    table.field_names = ["Nama Komunitas", "Email", "Narahubung"]
    for komunitas in komunitas_data:
        table.add_row([komunitas[0], komunitas[1], komunitas[2]])

    print(table)
    input('Tekan enter untuk kembali...')
    pengguna.UtamaPengguna()  # Kembali ke menu utama
```
Fungsi LihatKomunitas bertujuan untuk menampilkan data komunitas dari database. Pertama, ia mengambil data komunitas dari database menggunakan query SQL yang sesuai. Setelah mendapatkan data, ia menggunakan objek PrettyTable untuk memformat data dalam bentuk tabel. Setelah tabel dibuat, fungsi mencetaknya ke layar. Ketika pengguna menekan tombol enter, ia akan kembali ke menu utama dengan memanggil fungsi UtamaPengguna dari modul pengguna.

```
# def BerikanKomentar(cursor, mydb, ID):
#     try:
#         # Mendapatkan tanggal dan waktu saat ini
#         tanggal_sekarang = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#         clear()
#         id_pengguna = ID
#         tanggal_sekarang = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         id_kegiatan = int(input("Masukkan ID Kegiatan: "))
#         isi_komentar = input("Masukkan isi komentar Anda: ")
#         hashtag = input("Masukkan hashtag (opsional): ")

#         # Menambahkan komentar ke dalam database
#         query_add_komentar = "INSERT INTO komentar (F_ID_Pengguna, F_ID_Kegiatan, Tanggal, Isi_Komentar, Hashtag) VALUES (%s, %s, %s, %s, %s)"
#         cursor.execute(query_add_komentar, (id_pengguna, id_kegiatan, tanggal_sekarang, isi_komentar, hashtag))
#         mydb.commit()

#         print("Komentar berhasil ditambahkan!")
#     except Exception as e:
#         print(f"Error: {e}")
#         mydb.rollback()


# test
def BerikanKomentar(cursor, ID,mydb):
    clear()
    try:
        id_kegiatan = int(input("Masukkan ID Kegiatan: "))
        isi_komentar = input("Masukkan isi komentar Anda: ")
        hashtag = input("Masukkan hashtag (opsional): ")

        # Mengambil tanggal dan waktu saat ini
        tanggal_sekarang = datetime.now()

        # Menambahkan komentar ke dalam database
        F_ID_Pengguna = ID
        query_add_komentar = "INSERT INTO komentar (F_ID_Pengguna, F_ID_Kegiatan, Tanggal, Isi_Komentar, Hashtag) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query_add_komentar, (F_ID_Pengguna, id_kegiatan, tanggal_sekarang, isi_komentar, hashtag))
        mydb.commit()

        print("Komentar berhasil ditambahkan!")
        print("Timestamp:", tanggal_sekarang)
    
    except ValueError:
        print("ID Kegiatan harus berupa bilangan bulat!")
    except Exception as e:
        print("Terjadi kesalahan:", e)

        

# def BerikanKomentar(cursor, ID, mydb):
#     clear()
#     id_kegiatan = int(input("Masukkan ID Kegiatan: "))
#     isi_komentar = input("Masukkan isi komentar Anda: ")
#     hashtag = input("Masukkan hashtag (opsional): ")
    
#     # Mengambil tanggal dan waktu saat ini
#     tanggal_sekarang = datetime.now()
#     # date_string = tanggal_sekarang.strftime('%Y-%m-%d %H:%M:%S')

#     # Mengonversi date string ke objek datetime
#     date_object = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

#     # Mengonversi objek datetime ke timestamp
#     timestamp = date_object.timestamp()

#     # Menambahkan komentar ke dalam database
#     F_ID_Pengguna = ID
#     query_add_komentar = "INSERT INTO komentar (F_ID_Pengguna, F_ID_Kegiatan, Tanggal, Isi_Komentar, Hashtag) VALUES (%s, %s, %s, %s, %s)"
#     cursor.execute(query_add_komentar, (F_ID_Pengguna, id_kegiatan, timestamp, isi_komentar, hashtag))
#     mydb.commit()

#     print("Komentar berhasil ditambahkan!")
#     print("Timestamp:", timestamp)
```
Fungsi BerikanKomentar memungkinkan pengguna untuk menambahkan komentar pada suatu kegiatan. Pengguna diminta untuk memasukkan ID kegiatan, isi komentar, dan hashtag (opsional). Setelah menerima input, fungsi menambahkan komentar ke database bersama dengan timestamp yang menunjukkan waktu komentar dibuat.

```
def MelihatKomentar():
    clear()
    # Mendapatkan data kegiatan dari database
    query_get_kegiatan = "SELECT INTO komentar (F_ID_Pengguna, F_ID_Kegiatan, Isi_Komentar, Hashtag)"
    table = PrettyTable()
    table.field_names = ["ID Kegiatan", "Judul Kegiatan", "Deskripsi Kegiatan", "Lokasi Kegiatan"]
    for kegiatan in query_get_kegiatan:
        table.add_row(kegiatan)
    print(table)
    input('Tekan enter untuk kembali...')
```
Fungsi MelihatKomentar adalah untuk melihat komentar dalam sebuah kegiatan. Pertama, kode membersihkan layar konsol. Kemudian, melakukan query untuk mendapatkan data komentar dari database. Data komentar yang diperoleh kemudian ditampilkan dalam bentuk tabel menggunakan PrettyTable. Setelah menampilkan data, program akan menunggu input dari pengguna sebelum melanjutkan.









