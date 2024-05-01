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
        while True:  # Looping sampai registrasi berhasil
            # Input nama
            while True:
                nama_pelapor = input('Masukkan Nama Anda: ').strip()
                if not nama_pelapor:
                    print("Nama tidak boleh kosong.")
                elif len(nama_pelapor) > 30:
                    print('Nama tidak boleh lebih dari 30 karakter.')
                else:
                    break  # Keluar dari perulangan jika nama valid
            
            # Input alamat
            while True:
                alamat_pelapor = input('Masukkan Alamat Anda: ').strip()
                if not alamat_pelapor:
                    print("Alamat tidak boleh kosong.")
                elif len(alamat_pelapor) > 50:
                    print('Alamat tidak boleh lebih dari 50 karakter.')
                else:
                    break  # Keluar dari perulangan jika alamat valid
            
            # Input nomor HP
            while True:
                kontak_pelapor = input('Masukkan Kontak Anda (harus berupa angka): ').strip()
                if not kontak_pelapor.isdigit():
                    print('Nomor HP hanya boleh berisi angka.')
                elif len(kontak_pelapor) > 13:
                    print('Nomor HP tidak boleh lebih dari 13 digit.')
                else:
                    break  # Keluar dari perulangan jika nomor HP valid

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






def LoginPelapor():
    try:
        id_pelapor = int(input('Masukkan ID Anda: '))
        if len(str(id_pelapor)) <= 5:
            nama_pelapor = (input('Masukkan Nama Anda: '))
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



import random

def InputInformasi(cursor, mydb, id_pelapor):
    while True:
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
                        break  # Keluar dari loop input informasi
                    else:
                        print('Deskripsi tidak boleh lebih dari 500...')
                else:
                    print('Judul tidak boleh lebih dari 200...')
            else:
                print('Format tanggal salah. Masukkan tanggal dengan format YYYY-MM-DD...')
        except KeyboardInterrupt:
            print("\nInput dibatalkan. Tekan Ctrl + Z atau input 'exit' untuk kembali ke menu.")
            continue  # Mengulang loop input informasi
        except ValueError as ve:
            print(f"Error: {ve}")
            continue  # Mengulang loop input informasi
        except Exception as e:
            print(f"Error: {e}")
            continue  # Mengulang loop input informasi

