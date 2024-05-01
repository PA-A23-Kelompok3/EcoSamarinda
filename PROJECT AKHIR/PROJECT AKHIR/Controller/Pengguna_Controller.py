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
    try:
        while True:  # Looping sampai registrasi berhasil
            # Input username
            while True:
                Username = input('Masukkan Username yang Anda inginkan: ').strip()
                if not Username:
                    print("Username tidak boleh kosong.")
                elif len(Username) > 15:
                    print('Username tidak boleh lebih dari 15 karakter.')
                else:
                    break  # Keluar dari perulangan jika username valid
            
            # Input password
            while True:
                Password = input('Masukkan Password yang Anda inginkan: ').strip()
                if not Password:
                    print("Password tidak boleh kosong.")
                elif len(Password) > 20:
                    print('Password tidak boleh lebih dari 20 karakter.')
                else:
                    break  # Keluar dari perulangan jika password valid
            
            # Input email
            while True:
                email = input('Masukkan Email yang Anda inginkan: ').strip()
                if not email:
                    print("Email tidak boleh kosong.")
                elif len(email) > 40:
                    print('Email tidak boleh lebih dari 40 karakter.')
                else:
                    break  # Keluar dari perulangan jika email valid

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
            break  # Keluar dari loop setelah berhasil melakukan registrasi

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
        print('╔══════════════════════════════════════════╗')
        print("|              KESALAHAN INPUT              |")
        print("|       MOHON PERHATIKAN INPUTAN ANDA       |")
        print('╚══════════════════════════════════════════╝')
        input('Tekan enter untuk kembali...')
        pengguna.menuPengguna()



## LOGIN PENGGUNA ##

def LoginPengguna(cursor, mydb):
    try:
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
    except Exception as e:
        print(e)
        clear()
        print('╔═══════════════════════════════════════════╗')
        print("|              KESALAHAN INPUT              |")
        print("|       MOHON PERHATIKAN INPUTAN ANDA       |")
        print('╚═══════════════════════════════════════════╝')
        input('Tekan enter untuk kembali...')
        pengguna.menuPengguna()



## MELIHAT KEGIATAN ##

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


def BerikanKomentar(cursor, ID, mydb):
    clear()
    try:
        id_kegiatan = int(input("Masukkan ID Kegiatan: "))
        isi_komentar = input("Masukkan isi komentar Anda: ")
        hashtag = input("Masukkan hashtag (opsional): ")

        # Mengambil tanggal saat ini
        tanggal_sekarang = datetime.now().date()

        # Menambahkan komentar ke dalam database
        F_ID_Pengguna = ID
        query_add_komentar = "INSERT INTO komentar (F_ID_Pengguna, F_ID_Kegiatan, Tanggal, Isi_Komentar, Hashtag) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query_add_komentar, (F_ID_Pengguna, id_kegiatan, tanggal_sekarang, isi_komentar, hashtag))
        mydb.commit()

        print("Komentar berhasil ditambahkan!")
        print("Tanggal:", tanggal_sekarang)
    
    except ValueError:
        print("ID Kegiatan harus berupa bilangan bulat!")
    except Exception as e:
        print("Terjadi kesalahan:", e)


def MelihatKomentar(cursor):
    clear()
    try:
        # Mendapatkan data komentar dari database
        query_get_komentar = "SELECT F_ID_Kegiatan, Isi_Komentar, Hashtag FROM komentar"
        cursor.execute(query_get_komentar)
        komentar_data = cursor.fetchall()

        if not komentar_data:
            print("Belum ada komentar yang tersedia.")
            input('Tekan enter untuk kembali...')
            return

        # Menampilkan data komentar menggunakan PrettyTable
        table = PrettyTable()
        table.field_names = ["ID Kegiatan", "Isi Komentar", "Hashtag"]
        for komentar in komentar_data:
            table.add_row(komentar)
        print(table)

        input('Tekan enter untuk kembali...')
    except Exception as e:
        print("Terjadi kesalahan:", e)