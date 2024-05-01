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
        pengguna.MelihatKomentar(cursor)

def KomentarPengguna(cursor, ID, mydb):
    print('╔══════════════════════════════════════════╗')
    print('|     INGIN MEMBERIKAN KOMENTAR (Y/T)      |')
    print('╚══════════════════════════════════════════╝')
    pilihan = str(input('Masukkan Pilihan Anda: '))
    if pilihan == 'Y':
        pengguna.BerikanKomentar(cursor, ID, mydb)
    elif pilihan == 'T':
        UtamaPengguna()