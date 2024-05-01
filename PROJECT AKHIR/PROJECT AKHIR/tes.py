import os
import math

class Batik:
    class Node:
        def __init__(self, produk=None, motif=None, harga=None, ukuran=None, stok=None):
            self.produk = produk
            self.motif = motif
            self.harga = harga
            self.ukuran = ukuran
            self.stok = stok
            self.next = None

    def __init__(self):
        self.head = None

    def periksa_produk(self, produk):
        current = self.head
        while current:
            if current.produk == produk:
                return True
            current = current.next
        return False

    def tambah_di_awal(self, produk, motif, harga, ukuran, stok):
        new_node = self.Node(produk, motif, harga, ukuran, stok)
        new_node.next = self.head
        self.head = new_node

    def tambah_di_tengah(self, produk_sebelumnya, produk_baru, motif, harga, ukuran, stok):
        if not self.head:
            print("Tidak ada produk.")
            return
        current = self.head
        while current:
            if current.produk == produk_sebelumnya:
                new_node = self.Node(produk_baru, motif, harga, ukuran, stok)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Tidak dapat menambahkan {produk_baru}. Produk {produk_sebelumnya} tidak ditemukan.")

    def tambah_di_akhir(self, produk, motif, harga, ukuran, stok):
        new_node = self.Node(produk, motif, harga, ukuran, stok)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def hapus_produk(self, produk):
        if not self.head:
            print("Tidak ada produk.")
            return
        if self.head.produk == produk:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.produk == produk:
                current.next = current.next.next
                return
            current = current.next

    def tampilkan(self):
        current = self.head
        while current:
            print(f"Produk: {current.produk}, Motif: {current.motif}")
            current = current.next

    def merge_sort(self, arr, key, ascending=True):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            self.merge_sort(L, key, ascending)
            self.merge_sort(R, key, ascending)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if ascending:
                    if getattr(L[i], key) < getattr(R[j], key):
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                else: 
                    if getattr(L[i], key) > getattr(R[j], key):
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    def sort_and_display(self, key, ascending=True):
        temp_list = []
        current = self.head
        while current:
            temp_list.append(current)
            current = current.next
        self.merge_sort(temp_list, key, ascending)
        if ascending:
            print("Hasil Sorting (Ascending):")
        else:
            print("Hasil Sorting (Descending):")
        sorted_nodes = []
        for node in temp_list:
            sorted_nodes.append(node)
            print(f"Produk: {node.produk}, {key}: {getattr(node, key)}")
        self.head = sorted_nodes[0]
        for i in range(len(sorted_nodes) - 1):
            sorted_nodes[i].next = sorted_nodes[i + 1]
        sorted_nodes[-1].next = None
        return sorted_nodes

    def jump_search(self, arr, x, key):
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        while arr[min(step, n) - 1].produk < x:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1
        while arr[prev].produk < x:
            prev += 1
            if prev == min(step, n):
                return -1
        if arr[prev].produk == x:
            return prev
        return -1

    def search_and_display(self, key, value, sorted_nodes):
        found = False
        current = self.head
        while current:
            if getattr(current, key) == value:
                found = True
                print("Produk ditemukan:")
                print(f"Produk: {current.produk}, Motif: {current.motif}")
            current = current.next
        if not found:
            print("Produk tidak ditemukan.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_input(prompt, choices):
    while True:
        user_input = input(prompt)
        if user_input in choices:
            return user_input
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def tampilkan_menu():
    clear_screen()
    print('╔══════Pilih Opsi Yang Anda Inginkan═══════╗')
    print('| [1].Tampilkan Semua Produk Batik         |')
    print('| [2].Tambahkan Produk Batik               |')
    print('| [3].Hapus Produk Batik                   |')
    print('| [4].Sorting                              |')
    print('| [5].Cari Produk                          |')
    print('| [6].Keluar                               |')
    print('╚══════════════════════════════════════════╝')

def menu(batik_list):
    while True:
        tampilkan_menu()
        try:
            pilihan = int(input('Silahkan masukkan pilihan anda (1/2/3/4/5/6): '))
        except ValueError:
            print('Masukkan opsi menggunakan angka!(1/2/3/4/5/6)')
            input('Tekan enter untuk kembali...')
            continue

        if pilihan == 1:
            clear_screen()
            batik_list.tampilkan()
            input('Tekan enter untuk kembali ke menu...')

        elif pilihan == 2:
            clear_screen()
            batik_list.tampilkan()
            print('╔════Pilih Opsi Yang Anda Inginkan════╗')
            print('| [1].Tambahkan di awal               |')
            print('| [2].Tambahkan di akhir              |')
            print('| [3].Tambahkan di tengah             |')
            print('| [4].Keluar                          |')
            print('╚═════════════════════════════════════╝')
            masukan = int(input('Silahkan masukkan pilihan anda (1/2/3/4): '))
            if masukan == 1:
                produk = input('Masukkan produk: ')
                motif = input('Masukkan motif Batik: ')
                harga = int(input('Masukkan harga(berupa angka): '))
                ukuran = input('Masukkan Ukuran(XL/L/M): ')
                stok = int(input('Masukkan Stok: '))
                batik_list.tambah_di_awal(produk, motif, harga, ukuran, stok)
            elif masukan == 2:
                produk = input('Masukkan produk: ')
                motif = input('Masukkan motif Batik: ')
                harga = int(input('Masukkan harga(berupa angka): '))
                ukuran = input('Masukkan Ukuran(XL/L/M): ')
                stok = int(input('Masukkan Stok: '))
                batik_list.tambah_di_akhir(produk, motif, harga, ukuran, stok)
            elif masukan == 3:
                produk_sebelumnya = input('Masukkan nama produk sebelumnya: ')
                produk_baru = input('Masukkan produk baru: ')
                motif = input('Masukkan motif Batik: ')
                harga = int(input('Masukkan harga(berupa angka): '))
                ukuran = input('Masukkan Ukuran(XL/L/M): ')
                stok = int(input('Masukkan Stok: '))
                batik_list.tambah_di_tengah(produk_sebelumnya, produk_baru, motif, harga, ukuran, stok)
            elif masukan == 4:
                break
            else:
                print('Pilihan tidak valid.')
                input('Tekan enter untuk kembali...')
                break

        elif pilihan == 3:
            produk = input("Masukkan Produk yang ingin di hapus: ")
            if batik_list.periksa_produk(produk):
                batik_list.hapus_produk(produk)
                input("Tekan enter untuk melanjutkan...")
            else:
                print(f"Produk {produk} tidak ada.")
                input("Tekan enter untuk melanjutkan...")

        elif pilihan == 4:
            clear_screen()
            print('╔════Pilih Opsi Yang Anda Inginkan══════════╗')
            print('| [1].Sorting berdasarkan Produk            |')
            print('| [2].Sorting berdasarkan Harga             |')
            print('| [3].Keluar                                |')
            print('╚═══════════════════════════════════════════╝')
            sorting_choice = int(input('Silahkan masukkan pilihan anda (1/2/3): '))
            if sorting_choice == 1 or sorting_choice == 2:
                ascending_input = validate_input("Urutkan secara ascending? (y/n): ", ["y", "n"])
                ascending = ascending_input == 'y'
                key = 'produk' if sorting_choice == 1 else 'harga'
                sorted_nodes = batik_list.sort_and_display(key, ascending)  # Untuk menyimpan hasil sorting
                input('Tekan enter untuk kembali...')
            elif sorting_choice == 3:
                continue

        elif pilihan == 5:
            clear_screen()
            print('╔════Pilih Attribut Pencarian════╗')
            print('| [1].Cari berdasarkan Produk   |')
            print('| [2].Cari berdasarkan Motif    |')
            print('| [3].Keluar                     |')
            print('╚══════════════════════════════╝')
            search_choice = int(input('Silahkan masukkan pilihan anda (1/2/3): '))
            if search_choice == 1:
                produk = input("Masukkan Produk yang ingin dicari: ")
                sorted_nodes = batik_list.sort_and_display('produk')
                batik_list.search_and_display('produk', produk, sorted_nodes)
                input('Tekan enter untuk kembali...')
            elif search_choice == 2:
                motif = input("Masukkan Motif yang ingin dicari: ")
                sorted_nodes = batik_list.sort_and_display('motif')
                batik_list.search_and_display('motif', motif, sorted_nodes)
                input('Tekan enter untuk kembali...')
            elif search_choice == 3:
                continue
            else:
                print('Pilihan tidak valid.')
                input('Tekan enter untuk kembali...')
                break

        elif pilihan == 6:
            print('Terima kasih telah menggunakan program ini.')
            break

        else:
            print('Pilihan tidak valid.')

def pembukaan():
    clear_screen()
    print('!!!Hai selamat datang di RufBatik!!!')
    input('Tekan enter untuk melanjutkan...')

    # DATA yang telah tersedia
    batik_list = Batik()
    batik_list.tambah_di_awal("Batik Tulis Jogja", "Parang Kusumo", 350000, "XL", 50)
    batik_list.tambah_di_akhir("Batik Cap Solo", "Sido Mukti", 250000, "L", 30)
    batik_list.tambah_di_akhir("Batik Print Pekalongan", "Liris Cirebon", 150000, "M", 20)
    menu(batik_list)

if __name__ == "__main__":
    pembukaan()