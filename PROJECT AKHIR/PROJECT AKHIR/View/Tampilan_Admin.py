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
    print("| [1] LOGIN                                   |")
    print('|                                             |')
    print("| [2] KELUAR                                  |")
    print('╚═════════════════════════════════════════════╝')
    pilih = int(input("Masukkan pilihan Anda (1-2): "))
    if pilih == 1:
        admin.LoginAdmin()
    elif pilih == 2:
        main.main_menu()

def laporan(Username, cursor):
    while True:
        try:
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
        except ValueError:
                print("Masukkan angka antara 1 hingga 5.")


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
