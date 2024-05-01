
from View import Tampilan_Pelapor as pelapor
from View import Tampilan_Admin as adminn
from View import Tampilan_Pengguna as pengguna
from Controller import Admin_Controller as admin
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    while True:
        try:
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
                pilihan = int(input("Silakan pilih menu yang ingin Anda akses: "))
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
                    break

            except ValueError:
                print("Pilihan harus berupa angka.")
                input("Tekan enter untuk melanjutkan...")
            
        except KeyboardInterrupt:
            print("\nProses telah dihentikan oleh pengguna.")
            input("Tekan enter untuk melanjutkan...")

        except EOFError:
            print("\nProses telah dihentikan oleh pengguna.")
            input("Tekan enter untuk melanjutkan...")
        

if __name__ == "__main__":
    main_menu()


