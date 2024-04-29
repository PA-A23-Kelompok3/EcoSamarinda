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
