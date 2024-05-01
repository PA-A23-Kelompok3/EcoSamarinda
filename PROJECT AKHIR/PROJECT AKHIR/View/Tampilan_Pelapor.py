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
    clear()
    if pilihan == 1:
        pelapor.RegisPelapor(cursor, mydb)
    elif pilihan == 2:
        pelapor.LoginPelapor()
    elif pilihan == 3:
        Main.main_menu()



