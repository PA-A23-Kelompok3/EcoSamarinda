-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 24, 2024 at 05:23 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ecosamarinda`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `ID_Admin` int(4) NOT NULL,
  `Nama_Admin` varchar(30) NOT NULL,
  `Username` varchar(15) NOT NULL,
  `Password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`ID_Admin`, `Nama_Admin`, `Username`, `Password`) VALUES
(1, 'Muhamad Nur Fadilah', 'muhamad_fadilah', 'password1'),
(2, 'Nyoman Arini Trirahayu', 'nyoman_arini', 'password2'),
(3, 'Anita Resky Ananda', 'anita_resky', 'password3'),
(4, 'Tri Rahayu Septiyani', 'tri_septiyani', 'password4'),
(5, 'Lisa Nafrathiloya', 'lisa_nafrathilo', 'password5'),
(6, 'Reyfaldho Alfarazel', 'reyfaldho_alfar', 'password6'),
(7, 'Alya Rizqi Ramadhani', 'alya_ramadhani', 'password7'),
(8, 'Alyssa Dwiana Mulia', 'alyssa_mulia', 'password8'),
(9, 'Athira Fahmi', 'athira_fahmi', 'password9'),
(10, 'Diva Tri Andini', 'diva_andini', 'password10'),
(11, 'Hana Anastasya Wardah', 'hana_wardah', 'password11'),
(12, 'Siti Annida Adzra', 'siti_annida', 'password12'),
(13, 'Aidhil Saputra', 'aidhil_saputra', 'password13'),
(14, 'Irene Miraj Nur Sari', 'irene_sari', 'password14'),
(15, 'Fitri Yanti', 'fitri_yanti', 'password15'),
(16, 'Nazwa Tri Ananda', 'nazwa_ananda', 'password16'),
(17, 'Widia Saputri', 'widia_saputri', 'password17'),
(18, 'Muhammad Hisyam Nugroho', 'muhammad_nugroh', 'password18'),
(19, 'Fitriani', 'fitriani', 'password19'),
(20, 'Mohammad Imam Farizy', 'imam_farizy', 'password20'),
(21, 'Adinda Salsabilla Naura', 'adinda_naura', 'password21'),
(22, 'Nely Oktavia Redeca', 'nely_redeca', 'password22'),
(23, 'Muhammad Khairu Fadilah', 'muhammad_khairu', 'password23'),
(24, 'ROFI HANIF FAUZAN', 'rofi_fauzan', 'password24'),
(25, 'Muhammad Aryaputra Wirawan', 'muhammad_wirawa', 'password25'),
(26, 'Farhan Imannudin', 'farhan_imannudi', 'password26'),
(27, 'MUHAMMAD ROFIIF TAQIYYUDDIN NA', 'muhammad_rofiif', 'password27'),
(28, 'Noor Lintang Bhaskara', 'noor_bhaskara', 'password28'),
(29, 'Muhammad Dzaky Irawan', 'muhammad_dzaky', 'password29'),
(30, 'Naura Syawal Athallah Putri', 'naura_syawal', 'password30'),
(31, 'Muhammad Pidha Iqbal Fadillah', 'muhammad_pidha', 'password31'),
(32, 'Muhammad Alfian Adien', 'muhammad_alfian', 'password32'),
(33, 'Muhammad Nabil Maruf', 'muhammad_nabil', 'password33'),
(34, 'Yasmin Alya Aziza', 'yasmin_aziza', 'password34'),
(35, 'Dhea Amalia Putri', 'dhea_amalia', 'password35'),
(36, 'Andromeda Hibnu Darmawi', 'andromeda_darma', 'password36'),
(37, 'Muhammad Rizky Setiawan', 'muhammad_setiaw', 'password37'),
(38, 'Muhammad Aidil Mirza', 'muhammad_aidil', 'password38'),
(39, 'David Sebastian Sutandy', 'david_sutandy', 'password39'),
(40, 'Muhammad Rizky Setiawan', 'muhammad_setiaw', 'password40');

-- --------------------------------------------------------

--
-- Table structure for table `informasi`
--

CREATE TABLE `informasi` (
  `ID_Informasi` int(4) NOT NULL,
  `F_ID_Pelapor` int(11) NOT NULL,
  `F_ID_Admin` int(11) NOT NULL,
  `Tanggal_Waktu` datetime NOT NULL,
  `Judul_Informasi` varchar(200) NOT NULL,
  `Deskripsi_Informasi` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `informasi`
--

INSERT INTO `informasi` (`ID_Informasi`, `F_ID_Pelapor`, `F_ID_Admin`, `Tanggal_Waktu`, `Judul_Informasi`, `Deskripsi_Informasi`) VALUES
(82, 10002, 2, '2024-04-21 11:30:00', 'Penanaman Pohon di Taman Kota', 'Kegiatan penanaman pohon di taman kota untuk menyegarkan udara dan menciptakan lingkungan yang hijau.'),
(83, 10003, 3, '2024-04-21 12:45:00', 'Kampanye Pengurangan Penggunaan Plastik', 'Kampanye untuk mengurangi penggunaan plastik sekali pakai dalam kehidupan sehari-hari.'),
(84, 10004, 4, '2024-04-21 14:00:00', 'Penyuluhan Pengelolaan Sampah Organik', 'Penyuluhan tentang pengelolaan sampah organik untuk menghasilkan kompos yang berkualitas.'),
(85, 10005, 5, '2024-04-21 15:15:00', 'Kampanye Penyelamatan Hutan Mangrove', 'Kampanye untuk menyelamatkan hutan mangrove dari kerusakan akibat pembabatan ilegal.'),
(86, 10006, 6, '2024-04-22 10:15:00', 'Edukasi Penghematan Air Bersih', 'Edukasi tentang cara menghemat penggunaan air bersih dalam kehidupan sehari-hari.'),
(87, 10007, 7, '2024-04-22 11:30:00', 'Penyuluhan Penggunaan Transportasi Ramah Lingkungan', 'Penyuluhan tentang pentingnya menggunakan transportasi ramah lingkungan, seperti bersepeda atau menggunakan transportasi publik.'),
(88, 10008, 8, '2024-04-22 12:45:00', 'Kampanye Pencegahan Pencemaran Udara', 'Kampanye untuk mencegah pencemaran udara dengan mengurangi emisi gas rumah kaca dan polusi udara.'),
(89, 10009, 9, '2024-04-22 14:00:00', 'Penanaman Pohon di Sekitar Sungai', 'Kegiatan penanaman pohon di sepanjang sungai untuk mencegah erosi dan menjaga keberlangsungan ekosistem sungai.'),
(90, 10010, 10, '2024-04-22 15:15:00', 'Kampanye Penggunaan Energi Terbarukan', 'Kampanye untuk mendorong penggunaan energi terbarukan sebagai alternatif yang ramah lingkungan.'),
(91, 10011, 11, '2024-04-23 10:15:00', 'Penyuluhan Pengelolaan Limbah Elektronik', 'Penyuluhan tentang cara yang benar dalam mengelola limbah elektronik untuk mencegah pencemaran lingkungan.'),
(92, 10012, 12, '2024-04-23 11:30:00', 'Kampanye Penyelamatan Satwa Liar', 'Kampanye untuk melindungi satwa liar dari perburuan ilegal dan kerusakan habitat.'),
(93, 10013, 13, '2024-04-23 12:45:00', 'Penyuluhan Pengurangan Penggunaan Kantong Plastik', 'Penyuluhan tentang pentingnya mengurangi penggunaan kantong plastik sekali pakai untuk mengurangi sampah plastik.'),
(94, 10014, 14, '2024-04-23 14:00:00', 'Kampanye Penyelamatan Ekosistem Hutan', 'Kampanye untuk menyelamatkan ekosistem hutan dari deforestasi dan degradasi lahan.'),
(95, 10015, 15, '2024-04-23 15:15:00', 'Penyuluhan Pengelolaan Limbah B3', 'Penyuluhan tentang pengelolaan limbah berbahaya dan beracun (B3) secara aman dan bertanggung jawab.'),
(96, 10016, 16, '2024-04-24 10:15:00', 'Kampanye Penanaman Pohon Buah', 'Kampanye untuk mendorong penanaman pohon buah di lingkungan sekitar sebagai upaya meningkatkan kesadaran akan pentingnya menjaga keberagaman flora.'),
(97, 10017, 17, '2024-04-24 11:30:00', 'Penyuluhan Pengurangan Emisi Gas Rumah Kaca', 'Penyuluhan tentang cara-cara untuk mengurangi emisi gas rumah kaca dalam kehidupan sehari-hari.'),
(98, 10018, 18, '2024-04-24 12:45:00', 'Kampanye Penyelamatan Lingkungan Pantai', 'Kampanye untuk menyelamatkan lingkungan pantai dari kerusakan dan pencemaran.'),
(99, 10019, 19, '2024-04-24 14:00:00', 'Penyuluhan Pengelolaan Limbah Padat', 'Penyuluhan tentang pengelolaan limbah padat dengan cara yang ramah lingkungan.'),
(100, 10020, 20, '2024-04-24 15:15:00', 'Kampanye Penghijauan Kawasan Perkotaan', 'Kampanye untuk mendorong penghijauan kawasan perkotaan guna meningkatkan kualitas udara dan memperindah lingkungan.'),
(101, 10021, 21, '2024-04-25 10:15:00', 'Penyuluhan Pengelolaan Sampah Plastik', 'Penyuluhan tentang cara-cara mengelola sampah plastik agar tidak mencemari lingkungan.'),
(102, 10022, 22, '2024-04-25 11:30:00', 'Kampanye Penyelamatan Ekosistem Sungai', 'Kampanye untuk menyelamatkan ekosistem sungai dari pencemaran dan degradasi lingkungan.'),
(103, 10023, 23, '2024-04-25 12:45:00', 'Penyuluhan Penggunaan Transportasi Publik', 'Penyuluhan tentang manfaat penggunaan transportasi publik dalam mengurangi kemacetan dan polusi udara.'),
(104, 10024, 24, '2024-04-25 14:00:00', 'Kampanye Penanaman Pohon di Tepi Jalan', 'Kampanye untuk menanam pohon di tepi jalan guna memberikan teduh dan menyegarkan udara.'),
(105, 10025, 25, '2024-04-25 15:15:00', 'Penyuluhan Pengurangan Konsumsi Listrik', 'Penyuluhan tentang cara mengurangi konsumsi listrik dalam kehidupan sehari-hari.'),
(106, 10026, 26, '2024-04-26 10:15:00', 'Kampanye Penyelamatan Lahan Basah', 'Kampanye untuk melindungi lahan basah dari degradasi dan konversi lahan.'),
(107, 10027, 27, '2024-04-26 11:30:00', 'Penyuluhan Pengelolaan Limbah Cair', 'Penyuluhan tentang cara mengelola limbah cair secara efisien dan ramah lingkungan.'),
(108, 10028, 28, '2024-04-26 12:45:00', 'Kampanye Penyelamatan Lautan', 'Kampanye untuk menyelamatkan laut dari pencemaran dan overfishing.'),
(109, 10029, 29, '2024-04-26 14:00:00', 'Penyuluhan Penggunaan Transportasi Ramah Lingkungan', 'Penyuluhan tentang pentingnya menggunakan transportasi ramah lingkungan.'),
(110, 10030, 30, '2024-04-26 15:15:00', 'Kampanye Penyelamatan Satwa Liar', 'Kampanye untuk melindungi satwa liar dari perburuan ilegal.'),
(111, 10031, 31, '2024-04-27 10:15:00', 'Penyuluhan Pengelolaan Limbah B3', 'Penyuluhan tentang pengelolaan limbah berbahaya dan beracun.'),
(112, 10032, 32, '2024-04-27 11:30:00', 'Kampanye Penyelamatan Hutan Mangrove', 'Kampanye untuk menyelamatkan hutan mangrove dari perusakan.'),
(113, 10033, 33, '2024-04-27 12:45:00', 'Penyuluhan Pengurangan Emisi Gas Rumah Kaca', 'Penyuluhan tentang cara mengurangi emisi gas rumah kaca.'),
(114, 10034, 34, '2024-04-27 14:00:00', 'Kampanye Penyelamatan Lingkungan', 'Kampanye untuk menyelamatkan lingkungan dari kerusakan akibat aktivitas manusia.'),
(115, 10035, 35, '2024-04-27 15:15:00', 'Penyuluhan Penggunaan Energi Terbarukan', 'Penyuluhan tentang pemanfaatan energi terbarukan untuk lingkungan yang lebih bersih.'),
(116, 10036, 36, '2024-04-28 10:15:00', 'Kampanye Pencegahan Pencemaran Udara', 'Kampanye untuk mencegah pencemaran udara di lingkungan sekitar.'),
(117, 10037, 37, '2024-04-28 11:30:00', 'Penyuluhan Pengelolaan Sampah Organik', 'Penyuluhan tentang pengelolaan sampah organik untuk menghasilkan kompos.'),
(118, 10038, 38, '2024-04-28 12:45:00', 'Kampanye Penyelamatan Sungai', 'Kampanye untuk menyelamatkan sungai dari pencemaran dan degradasi lingkungan.'),
(119, 10039, 39, '2024-04-28 14:00:00', 'Penyuluhan Pengelolaan Limbah Elektronik', 'Penyuluhan tentang pengelolaan limbah elektronik secara aman dan bertanggung jawab.'),
(120, 10040, 40, '2024-04-28 15:15:00', 'Kampanye Penanaman Pohon di Sekitar Perumahan', 'Kampanye untuk menanam pohon di sekitar perumahan untuk menciptakan lingkungan yang hijau dan sehat.');

-- --------------------------------------------------------

--
-- Table structure for table `kegiatan`
--

CREATE TABLE `kegiatan` (
  `ID_Kegiatan` int(11) NOT NULL,
  `F_ID_Admin` int(11) NOT NULL,
  `Judul_Kegiatan` varchar(200) NOT NULL,
  `Deskripsi_Kegiatan` varchar(500) NOT NULL,
  `Lokasi_Kegiatan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kegiatan`
--

INSERT INTO `kegiatan` (`ID_Kegiatan`, `F_ID_Admin`, `Judul_Kegiatan`, `Deskripsi_Kegiatan`, `Lokasi_Kegiatan`) VALUES
(41, 1, 'Penanaman Pohon Bersama', 'Kegiatan ini merupakan acara penanaman pohon di sekitar kota untuk meningkatkan kepedulian terhadap lingkungan.', 'Taman Kota Samarinda'),
(42, 2, 'Pembersihan Sungai', 'Kegiatan membersihkan sampah di sepanjang sungai untuk menjaga kebersihan lingkungan dan kesehatan sungai.', 'Sungai Mahakam'),
(43, 3, 'Edukasi Pengelolaan Sampah', 'Kegiatan edukasi untuk memberikan pemahaman kepada masyarakat tentang pengelolaan sampah yang benar.', 'Balai Kota Samarinda'),
(44, 4, 'Pelatihan Pengolahan Limbah Organik', 'Pelatihan bagi masyarakat tentang pengolahan limbah organik menjadi pupuk kompos untuk mendukung pertanian organik.', 'Desa Mekar Jaya'),
(45, 5, 'Penyuluhan Penghematan Energi', 'Kegiatan penyuluhan kepada masyarakat tentang cara menghemat energi untuk mendukung keberlanjutan lingkungan.', 'Gedung Serba Guna Samarinda'),
(46, 6, 'Aksi Bersih Pantai', 'Kegiatan membersihkan pantai dari sampah plastik dan limbah lainnya untuk menjaga kebersihan pantai dan laut.', 'Pantai Amal'),
(47, 7, 'Penanaman Lahan Kosong', 'Kegiatan menanam tanaman hijau di lahan kosong untuk menjaga kelestarian alam dan memperindah lingkungan sekitar.', 'Perumahan Bukit Citra Indah'),
(48, 8, 'Kampanye Anti Pembakaran Hutan', 'Kampanye untuk mengedukasi masyarakat tentang bahaya pembakaran hutan dan pentingnya menjaga hutan lestari.', 'Pasar Segiri'),
(49, 9, 'Pelestarian Satwa Liar', 'Kegiatan pelestarian dan perlindungan satwa liar yang terancam punah di hutan-hutan sekitar.', 'Hutan Lindung Sungai Wain'),
(50, 10, 'Kunjungan Edukasi ke Taman Nasional', 'Kunjungan edukasi ke Taman Nasional Kutai untuk meningkatkan kesadaran akan pentingnya menjaga keanekaragaman hayati.', 'Taman Nasional Kutai'),
(51, 11, 'Penanaman Kebun Sayur Komunitas', 'Kegiatan menanam kebun sayur secara komunal untuk mendukung ketahanan pangan dan memperbaiki kualitas udara.', 'Perumahan Pesona Bahagia'),
(52, 12, 'Pelatihan Komposter Rumah Tangga', 'Pelatihan pembuatan komposter rumah tangga untuk mengelola sampah organik menjadi pupuk kompos.', 'Kantor Kelurahan Sidomulyo'),
(53, 13, 'Kampanye Reduksi Plastik', 'Kampanye untuk mengurangi penggunaan plastik sekali pakai dan mengedukasi masyarakat tentang bahaya plastik bagi lingkungan.', 'Pasar Pagi Sungai Pinang'),
(54, 14, 'Penyuluhan Penghijauan Kawasan Perkotaan', 'Penyuluhan tentang pentingnya penghijauan kawasan perkotaan untuk meningkatkan kualitas udara dan menurunkan suhu.', 'Kantor Pemerintah Kota Samarinda'),
(55, 15, 'Aksi Pemulihan Hutan Mangrove', 'Aksi pemulihan dan penanaman hutan mangrove sebagai bentuk menjaga ekosistem pantai dan perlindungan pesisir.', 'Pesisir Sungai Mahakam'),
(56, 16, 'Pelatihan Daur Ulang Kertas', 'Pelatihan pembuatan kertas daur ulang untuk mengurangi penebangan pohon dan meningkatkan penggunaan bahan daur ulang.', 'Kantor Desa Sempaja Utara'),
(57, 17, 'Pengadaan Tempat Sampah Terpisah', 'Pengadaan tempat sampah terpisah untuk mempermudah pengelolaan sampah dan meningkatkan tingkat daur ulang.', 'Sekolah Menengah Atas Negeri 1 Samarinda'),
(58, 18, 'Kampanye Konservasi Air', 'Kampanye untuk mengajak masyarakat melakukan konservasi air dan menghindari pemborosan sumber daya air.', 'Kantor Camat Samarinda Utara'),
(59, 19, 'Kunjungan Pendidikan Kebun Raya', 'Kunjungan ke Kebun Raya Balikpapan untuk mempelajari keanekaragaman tumbuhan dan ekosistem alami.', 'Kebun Raya Balikpapan'),
(60, 20, 'Penyuluhan Penggunaan Kendaraan Ramah Lingkungan', 'Penyuluhan tentang penggunaan kendaraan ramah lingkungan seperti sepeda dan kendaraan listrik.', 'Terminal Kota Samarinda'),
(61, 21, 'Kampanye Tanam Pohon Setiap Hari', 'Kampanye untuk mendorong masyarakat menanam setidaknya satu pohon setiap harinya untuk menjaga kelestarian alam.', 'Lapangan Tenggarong Seberang'),
(62, 22, 'Aksi Bersih Lingkungan Sekolah', 'Aksi membersihkan lingkungan sekolah dan menyadarkan siswa akan pentingnya menjaga kebersihan lingkungan.', 'Sekolah Dasar Negeri 1 Samarinda'),
(63, 23, 'Penghijauan Lahan Tersisa', 'Kegiatan penanaman pohon di lahan-lahan yang tersisa untuk menjaga keseimbangan ekosistem dan mengurangi efek pemanasan global.', 'Kawasan Industri Samarinda'),
(64, 24, 'Kampanye Hemat Listrik', 'Kampanye untuk mengajak masyarakat melakukan penghematan energi listrik di rumah-rumah mereka.', 'Perumahan Bumi Sejahtera'),
(65, 25, 'Pelatihan Pembuatan Tas Daur Ulang', 'Pelatihan pembuatan tas dari bahan daur ulang untuk mengurangi penggunaan kantong plastik.', 'Pasar Tradisional Samarinda Seberang'),
(66, 26, 'Kunjungan Edukasi ke Kebun Bibit', 'Kunjungan ke kebun bibit untuk mempelajari teknik penanaman dan perawatan tanaman secara benar.', 'Kebun Bibit Samarinda'),
(67, 27, 'Aksi Tanam Pohon Keliling Kota', 'Aksi menanam pohon di berbagai titik di sepanjang jalan kota untuk memperindah kota dan meningkatkan kualitas udara.', 'Taman Siring'),
(68, 28, 'Pembuatan Hutan Kota', 'Kegiatan penanaman pohon di kawasan terbuka kota untuk menciptakan hutan kota yang sejuk dan nyaman.', 'Kawasan Pemukiman Bukit Pinang Indah'),
(69, 29, 'Pengadaan Tempat Penyimpanan Sampah Organik', 'Pengadaan tempat penyimpanan sementara sampah organik di masyarakat untuk memudahkan pengolahan.', 'Kantor Desa Karang Anyar'),
(70, 30, 'Pelatihan Pembuatan Kerajinan Daur Ulang', 'Pelatihan membuat kerajinan tangan dari bahan daur ulang untuk mengurangi jumlah limbah plastik.', 'Sekolah Menengah Pertama Negeri 1 Samarinda'),
(71, 31, 'Kampanye Kurangi Penggunaan Kantong Plastik', 'Kampanye untuk mengurangi penggunaan kantong plastik dan menggantinya dengan tas belanja reusable.', 'Pasar Malam Sungai Kunjang'),
(72, 32, 'Aksi Penanaman Pohon Mangrove', 'Aksi penanaman pohon mangrove di sepanjang pesisir untuk melindungi pantai dari abrasi dan tsunami.', 'Pesisir Kampung Baru'),
(73, 33, 'Penyuluhan Penggunaan Bahan Ramah Lingkungan', 'Penyuluhan kepada masyarakat tentang penggunaan bahan ramah lingkungan dalam kehidupan sehari-hari.', 'Pasar Modern Samarinda'),
(74, 34, 'Kampanye Pengurangan Limbah Plastik', 'Kampanye untuk mengurangi produksi limbah plastik dan mendorong penggunaan alternatif ramah lingkungan.', 'Perumahan Bukit Alam Permai'),
(75, 35, 'Penghijauan Kawasan Industri', 'Kegiatan penanaman pohon di sekitar kawasan industri untuk mengurangi polusi udara dan meningkatkan keseimbangan ekosistem.', 'Kawasan Industri Kariangau'),
(76, 36, 'Kampanye Peduli Kebersihan Lingkungan', 'Kampanye untuk meningkatkan kesadaran masyarakat akan pentingnya menjaga kebersihan lingkungan sekitar.', 'Terminal Penumpang Kota Samarinda'),
(77, 37, 'Pelatihan Pembuatan Produk Ecobrick', 'Pelatihan membuat ecobrick dari botol plastik bekas sebagai solusi untuk mengurangi limbah plastik.', 'Sekolah Menengah Atas Negeri 2 Samarinda'),
(78, 38, 'Kampanye Hemat Air', 'Kampanye untuk mengajak masyarakat melakukan penghematan penggunaan air di rumah tangga dan tempat umum.', 'Perumahan Bukit Pelangi'),
(79, 39, 'Penanaman Pohon Peneduh', 'Kegiatan menanam pohon peneduh di sepanjang jalan kota untuk mengurangi suhu udara dan menciptakan kesejukan.', 'Jalan Pangeran Antasari'),
(80, 40, 'Aksi Bersih Drainase', 'Aksi pembersihan dan revitalisasi drainase di perkotaan untuk mencegah banjir dan meningkatkan kualitas lingkungan.', 'Kampung Baru Samarinda');

-- --------------------------------------------------------

--
-- Table structure for table `komentar`
--

CREATE TABLE `komentar` (
  `ID_komentar` int(11) NOT NULL,
  `F_ID_Pengguna` int(11) NOT NULL,
  `F_ID_Kegiatan` int(11) NOT NULL,
  `Tanggal` timestamp NOT NULL DEFAULT current_timestamp(),
  `Isi_Komentar` varchar(200) NOT NULL,
  `Hashtag` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `komentar`
--

INSERT INTO `komentar` (`ID_komentar`, `F_ID_Pengguna`, `F_ID_Kegiatan`, `Tanggal`, `Isi_Komentar`, `Hashtag`) VALUES
(241, 1, 41, '2024-04-22 01:32:24', 'Ayo berpartisipasi dalam kegiatan ini!', '#penanamanpohon #lingkunganhidup'),
(242, 2, 42, '2024-04-22 01:32:24', 'Sungai Mahakam harus tetap bersih!', '#pembersihansungai #pedulilingkungan'),
(243, 3, 43, '2024-04-22 01:32:24', 'Mari belajar tentang pengelolaan sampah!', '#edukasi #lingkunganbersih'),
(244, 4, 44, '2024-04-22 01:32:24', 'Pupuk kompos dapat mengurangi limbah organik.', '#pelatihan #pertanianorganik'),
(245, 5, 45, '2024-04-22 01:32:24', 'Hemat energi, jaga keberlanjutan lingkungan!', '#penyuluhan #hematenergi'),
(246, 6, 46, '2024-04-22 01:32:24', 'Bersihkan pantai, lindungi laut!', '#bersihpantai #pedulilaut'),
(247, 7, 47, '2024-04-22 01:32:24', 'Menanam pohon adalah investasi masa depan.', '#penanamanpohon #kelestarianalam'),
(248, 8, 48, '2024-04-22 01:32:24', 'Lindungi hutan, lindungi bumi!', '#kampanye #antipembakaranhutan'),
(249, 9, 49, '2024-04-22 01:32:24', 'Ayo lestarikan satwa liar!', '#pelestariansatwa #hutanlindung'),
(250, 10, 50, '2024-04-22 01:32:24', 'Keanekaragaman hayati harus dijaga!', '#edukasi #tamanNasional'),
(251, 11, 51, '2024-04-22 01:32:24', 'Menanam sayur untuk kehidupan sehat.', '#penanamankebun #sayurkomunal'),
(252, 12, 52, '2024-04-22 01:32:24', 'Komposter rumah tangga untuk lingkungan bersih.', '#pelatihan #komposter'),
(253, 13, 53, '2024-04-22 01:32:24', 'Kurangi plastik, selamatkan lingkungan!', '#reduksiplastik #lingkunganhidup'),
(254, 14, 54, '2024-04-22 01:32:24', 'Penghijauan kawasan perkotaan untuk kesehatan.', '#penghijauan #perkotaanbersih'),
(255, 15, 55, '2024-04-22 01:32:24', 'Hutan mangrove perlindungan pesisir.', '#pemulihan #hutanmangrove'),
(256, 16, 56, '2024-04-22 01:32:24', 'Daur ulang kertas, kurangi penebangan pohon.', '#pelatihan #daurulang'),
(257, 17, 57, '2024-04-22 01:32:24', 'Pisahkan sampah untuk lingkungan bersih.', '#pengelolaansampah #daurulang'),
(258, 18, 58, '2024-04-22 01:32:24', 'Air adalah sumber kehidupan.', '#konservasi #hematair'),
(259, 19, 59, '2024-04-22 01:32:24', 'Jelajahi keanekaragaman alam di Kebun Raya Balikpapan.', '#kebunraya #pendidikanlingkungan'),
(260, 20, 60, '2024-04-22 01:32:24', 'Gunakan kendaraan ramah lingkungan!', '#penyuluhan #kendaraanlistrik'),
(261, 21, 61, '2024-04-22 01:32:24', 'Tanam pohon, jaga alam!', '#kampanye #tanampohon'),
(262, 22, 62, '2024-04-22 01:32:24', 'Jaga kebersihan lingkungan sejak dini.', '#lingkungansekolah #aksiBersih'),
(263, 23, 63, '2024-04-22 01:32:24', 'Pohon adalah penyejuk bumi.', '#penghijauan #perubahaniklim'),
(264, 24, 64, '2024-04-22 01:32:24', 'Hemat listrik, jaga lingkungan.', '#kampanye #hematlistrik'),
(265, 25, 65, '2024-04-22 01:32:24', 'Tas dari bahan daur ulang untuk bumi lebih hijau.', '#tasdaurulang #kurangplastik'),
(266, 26, 66, '2024-04-22 01:32:24', 'Pelajari keindahan tanaman di kebun bibit.', '#pendidikan #tanaman'),
(267, 27, 67, '2024-04-22 01:32:24', 'Tanam pohon, beri nafas baru untuk kota!', '#pohonkota #udarabersih'),
(268, 28, 68, '2024-04-22 01:32:24', 'Hutan kota untuk lingkungan yang lebih baik.', '#pembuatanhutan #kotahijau'),
(269, 29, 69, '2024-04-22 01:32:24', 'Pengolahan sampah dimulai dari rumah.', '#pengelolaansampah #rumahbersih'),
(270, 30, 70, '2024-04-22 01:32:24', 'Kerajinan tangan ramah lingkungan.', '#kerajinan #daurulang'),
(271, 31, 71, '2024-04-22 01:32:24', 'Gunakan tas belanja reusable!', '#kurangplastik #penguranganplastik'),
(272, 32, 72, '2024-04-22 01:32:24', 'Mangrove untuk melindungi pantai.', '#mangrove #pesisiraman'),
(273, 33, 73, '2024-04-22 01:32:24', 'Gunakan bahan ramah lingkungan sehari-hari.', '#penyuluhan #ramahlingkungan'),
(274, 34, 74, '2024-04-22 01:32:24', 'Kurangi limbah plastik dengan tindakan nyata.', '#kampanye #kurangiplastik'),
(275, 35, 75, '2024-04-22 01:32:24', 'Pohon penyejuk di kawasan industri.', '#penghijauan #industribersih'),
(276, 36, 76, '2024-04-22 01:32:24', 'Jaga kebersihan lingkungan mulai dari terminal!', '#kampanye #pedulilngkungan'),
(277, 37, 77, '2024-04-22 01:32:24', 'Manfaatkan botol bekas untuk solusi lingkungan.', '#ecobrick #kurangplastik'),
(278, 38, 78, '2024-04-22 01:32:24', 'Hemat air untuk masa depan yang lebih baik.', '#hematair #konservasi'),
(279, 39, 79, '2024-04-22 01:32:24', 'Tanam pohon, berikan naungan untuk semua.', '#penanamanpohon #naungan'),
(280, 40, 80, '2024-04-22 01:32:24', 'Drainase bersih, lingkungan sehat!', '#bersihdrainase #banjirprventif');

-- --------------------------------------------------------

--
-- Table structure for table `komunitas`
--

CREATE TABLE `komunitas` (
  `ID_Komunitas` int(4) NOT NULL,
  `Nama_Komunitas` varchar(50) NOT NULL,
  `Email` varchar(40) NOT NULL,
  `F_ID_Admin` int(11) NOT NULL,
  `Narahubung` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `komunitas`
--

INSERT INTO `komunitas` (`ID_Komunitas`, `Nama_Komunitas`, `Email`, `F_ID_Admin`, `Narahubung`) VALUES
(41, 'Komunitas Peduli Lingkungan', 'pedulilingkungan@example.com', 1, 'Budi'),
(42, 'Komunitas Hijau Sejahtera', 'hijausejahtera@example.com', 2, 'Cindy'),
(43, 'Komunitas Pemuda Peduli Alam', 'pemudapemudaalam@example.com', 3, 'Dewi'),
(44, 'Komunitas Alam Lestari', 'alamestari@example.com', 4, 'Eka'),
(45, 'Komunitas Lingkungan Bersih', 'lingkunganbersih@example.com', 5, 'Fajar'),
(46, 'Komunitas Hijau Taman Kota', 'hijautamankota@example.com', 6, 'Gita'),
(47, 'Komunitas Peduli Sampah', 'pedulisampah@example.com', 7, 'Hadi'),
(48, 'Komunitas Hijau Peduli Lingkungan', 'hijaupedulilingkungan@example.com', 8, 'Indah'),
(49, 'Komunitas Peduli Sungai', 'pedulisungai@example.com', 9, 'Joko'),
(50, 'Komunitas Peduli Hutan', 'pedulihutan@example.com', 10, 'Kiki'),
(51, 'Komunitas Peduli Udara Bersih', 'peduliudarabersih@example.com', 11, 'Lia'),
(52, 'Komunitas Peduli Bumi', 'pedulibumi@example.com', 12, 'Mira'),
(53, 'Komunitas Pecinta Lingkungan', 'pecintalingkungan@example.com', 13, 'Nana'),
(54, 'Komunitas Lingkungan Hidup', 'lingkunganhidup@example.com', 14, 'Oscar'),
(55, 'Komunitas Hijau Lestari', 'hijaulestari@example.com', 15, 'Putri'),
(56, 'Komunitas Peduli Ekosistem', 'peduliekosistem@example.com', 16, 'Rudi'),
(57, 'Komunitas Hutan Sehat', 'hutansehat@example.com', 17, 'Sari'),
(58, 'Komunitas Peduli Pegunungan', 'pedulipegunungan@example.com', 18, 'Tono'),
(59, 'Komunitas Alam Tertata', 'alamtertata@example.com', 19, 'Umi'),
(60, 'Komunitas Peduli Air Bersih', 'peduliairbersih@example.com', 20, 'Vino'),
(61, 'Komunitas Hijau Ramah Lingkungan', 'hijauramahlingkungan@example.com', 21, 'Wulan'),
(62, 'Komunitas Peduli Tanah', 'pedulitanah@example.com', 22, 'Xavier'),
(63, 'Komunitas Peduli Lingkungan Sekitar', 'pedulilingkungansekitar@example.com', 23, 'Yuni'),
(64, 'Komunitas Pencinta Alam', 'pencintaalam@example.com', 24, 'Zacky'),
(65, 'Komunitas Peduli Kehutanan', 'pedulikehutanan@example.com', 25, 'Andi'),
(66, 'Komunitas Penjaga Laut', 'penjagalaut@example.com', 26, 'Bunga'),
(67, 'Komunitas Hijau Hijau', 'hijauhijau@example.com', 27, 'Citra'),
(68, 'Komunitas Pemuda Pemudi Peduli Lingkungan', 'pemudapemudipedulilingkungan@example.com', 28, 'Denny'),
(69, 'Komunitas Lingkungan Kreatif', 'lingkungankreatif@example.com', 29, 'Eko'),
(70, 'Komunitas Peduli Udara Segar', 'peduliudarasegar@example.com', 30, 'Firda'),
(71, 'Komunitas Hijau Alam', 'hijaualam@example.com', 31, 'Galih'),
(72, 'Komunitas Peduli Pesisir', 'pedulipesisir@example.com', 32, 'Hendra'),
(73, 'Komunitas Hutan Tropis', 'hutantropis@example.com', 33, 'Indra'),
(74, 'Komunitas Peduli Lahan Basah', 'pedulilahanbasah@example.com', 34, 'Jeni'),
(75, 'Komunitas Hijau Sejati', 'hijausejati@example.com', 35, 'Kurnia'),
(76, 'Komunitas Penjaga Ekosistem', 'penjagaekosistem@example.com', 36, 'Laras'),
(77, 'Komunitas Hijau Hidup', 'hijauhidup@example.com', 37, 'Maman'),
(78, 'Komunitas Peduli Bumi Kita', 'pedulibumikita@example.com', 38, 'Nani'),
(79, 'Komunitas Pecinta Lingkungan Hidup', 'pecintalingkunganhidup@example.com', 39, 'Opan'),
(80, 'Komunitas Lingkungan Makmur', 'lingkunganmakmur@example.com', 40, 'Pipit');

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pelapor`
--

CREATE TABLE `pelapor` (
  `ID_Pelapor` int(4) NOT NULL,
  `Nama_Pelapor` varchar(30) NOT NULL,
  `No_HP` varchar(13) NOT NULL,
  `Alamat` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pelapor`
--

INSERT INTO `pelapor` (`ID_Pelapor`, `Nama_Pelapor`, `No_HP`, `Alamat`) VALUES
(10001, 'Muhamad Nur Fadilah', '081234567890', 'Jl. Ahmad Yani No. 1'),
(10002, 'Nyoman Arini Trirahayu', '081098765432', 'Jl. Sudirman No. 2'),
(10003, 'Anita Resky Ananda', '081111222333', 'Jl. Diponegoro No. 3'),
(10004, 'Tri Rahayu Septiyani', '085556667778', 'Jl. Gajah Mada No. 4'),
(10005, 'Lisa Nafrathiloya', '089999888777', 'Jl. K.H. Hasyim Ashari No. 5'),
(10006, 'Reyfaldho Alfarazel', '083334445557', 'Jl. Pemuda No. 6'),
(10007, 'Alya Rizqi Ramadhani', '087778889990', 'Jl. Merdeka No. 7'),
(10008, 'Alyssa Dwiana Mulia', '084445556665', 'Jl. Imam Bonjol No. 8'),
(10009, 'Athira Fahmi', '086667778882', 'Jl. HR. Rasuna Said No. 9'),
(10010, 'Diva Tri Andini', '082223334449', 'Jl. Jenderal Sudirman No. 10'),
(10011, 'Hana Anastasya Wardah', '088899900011', 'Jl. Thamrin No. 11'),
(10012, 'Siti Annida Adzra', '081110009992', 'Jl. Majapahit No. 12'),
(10013, 'Aidhil Saputra', '084445556663', 'Jl. Gatot Subroto No. 13'),
(10014, 'Irene Miraj Nur Sari', '085554443335', 'Jl. Antasari No. 14'),
(10015, 'Fitri Yanti', '083332221111', 'Jl. Pahlawan No. 15'),
(10016, 'Nazwa Tri Ananda', '087778889994', 'Jl. Kalibata No. 16'),
(10017, 'Widia Saputri', '082223334447', 'Jl. Sudirman Kavling No. 17'),
(10018, 'Muhammad Hisyam Nugroho', '088877766665', 'Jl. Prof. Dr. Satrio No. 18'),
(10019, 'Fitriani', '081112223338', 'Jl. Fatmawati No. 19'),
(10020, 'Mohammad Imam Farizy', '089998887777', 'Jl. Jend. Gatot Subroto No. 20'),
(10021, 'Adinda Salsabilla Naura', '085554443336', 'Jl. Jend. Sudirman No. 21'),
(10022, 'Nely Oktavia Redeca', '083332221114', 'Jl. Jend. Ahmad Yani No. 22'),
(10023, 'Muhammad Khairu Fadilah', '087778889993', 'Jl. Pintu Besar Selatan No. 23'),
(10024, 'ROFI HANIF FAUZAN', '082223334445', 'Jl. Mangga Besar No. 24'),
(10025, 'Muhammad Aryaputra Wirawan', '088877766664', 'Jl. Juanda No. 25'),
(10026, 'Farhan Imannudin', '081112223330', 'Jl. Teuku Umar No. 26'),
(10027, 'Muhammad Hafidh Shovi', '089998887779', 'Jl. Tanah Abang No. 27'),
(10028, 'Noor Lintang Bhaskara', '085554443332', 'Jl. Kebon Sirih No. 28'),
(10029, 'Muhammad Dzaky Irawan', '083332221115', 'Jl. Menteng Raya No. 29'),
(10030, 'Naura Syawal Athallah Putri', '087778889996', 'Jl. Matraman No. 30'),
(10031, 'Muhammad Pidha Iqbal Fadillah', '082223334443', 'Jl. Panglima Polim No. 31'),
(10032, 'Muhammad Alfian Adien', '088877766661', 'Jl. Sudirman No. 32'),
(10033, 'Muhammad Nabil Maruf', '081112223332', 'Jl. Imam Bonjol No. 33'),
(10034, 'Yasmin Alya Aziza', '089998887774', 'Jl. Letjen S. Parman No. 34'),
(10035, 'Dhea Amalia Putri', '085554443331', 'Jl. Gajah Mada No. 35'),
(10036, 'Andromeda Hibnu Darmawi', '083332221113', 'Jl. Jend. Sudirman No. 36'),
(10037, 'Muhammad Rizky Setiawan', '087778889998', 'Jl. Hayam Wuruk No. 37'),
(10038, 'Muhammad Aidil Mirza', '082223334441', 'Jl. Pangeran Jayakarta No. 38'),
(10039, 'David Sebastian Sutandy', '088877766668', 'Jl. Raya Bogor No. 39'),
(10040, 'Rifqi Hadi Wijaya', '081112223336', 'Jl. Kebon Jeruk No. 40');

-- --------------------------------------------------------

--
-- Table structure for table `pengguna`
--

CREATE TABLE `pengguna` (
  `ID_pengguna` int(11) NOT NULL,
  `Username` varchar(15) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `Email` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pengguna`
--

INSERT INTO `pengguna` (`ID_pengguna`, `Username`, `Password`, `Email`) VALUES
(1, 'user1', 'password1', 'user1@example.com'),
(2, 'user2', 'password2', 'user2@example.com'),
(3, 'user3', 'password3', 'user3@example.com'),
(4, 'user4', 'password4', 'user4@example.com'),
(5, 'user5', 'LINTANG', 'user5@example.com'),
(6, 'user6', 'password6', 'user6@example.com'),
(7, 'user7', 'password7', 'user7@example.com'),
(8, 'user8', 'password8', 'user8@example.com'),
(9, 'user9', 'password9', 'user9@example.com'),
(10, 'user10', 'password10', 'user10@example.com'),
(11, 'user11', 'password11', 'user11@example.com'),
(12, 'user12', 'password12', 'user12@example.com'),
(13, 'user13', 'password13', 'user13@example.com'),
(14, 'user14', 'password14', 'user14@example.com'),
(15, 'user15', 'password15', 'user15@example.com'),
(16, 'user16', 'password16', 'user16@example.com'),
(17, 'user17', 'password17', 'user17@example.com'),
(18, 'user18', 'password18', 'user18@example.com'),
(19, 'user19', 'password19', 'user19@example.com'),
(20, 'user20', 'password20', 'user20@example.com'),
(21, 'user21', 'password21', 'user21@example.com'),
(22, 'user22', 'password22', 'user22@example.com'),
(23, 'user23', 'password23', 'user23@example.com'),
(24, 'user24', 'password24', 'user24@example.com'),
(25, 'user25', 'password25', 'user25@example.com'),
(26, 'user26', 'password26', 'user26@example.com'),
(27, 'user27', 'password27', 'user27@example.com'),
(28, 'user28', 'password28', 'user28@example.com'),
(29, 'user29', 'password29', 'user29@example.com'),
(30, 'user30', 'password30', 'user30@example.com'),
(31, 'user31', 'password31', 'user31@example.com'),
(32, 'user32', 'password32', 'user32@example.com'),
(33, 'user33', 'password33', 'user33@example.com'),
(34, 'user34', 'password34', 'user34@example.com'),
(35, 'user35', 'password35', 'user35@example.com'),
(36, 'user36', 'password36', 'user36@example.com'),
(37, 'user37', 'password37', 'user37@example.com'),
(38, 'user38', 'password38', 'user38@example.com'),
(39, 'user39', 'password39', 'user39@example.com'),
(40, 'user40', 'password40', 'user40@example.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`ID_Admin`);

--
-- Indexes for table `informasi`
--
ALTER TABLE `informasi`
  ADD PRIMARY KEY (`ID_Informasi`),
  ADD KEY `F_ID_Pelapor` (`F_ID_Pelapor`),
  ADD KEY `F_ID_Admin` (`F_ID_Admin`);

--
-- Indexes for table `kegiatan`
--
ALTER TABLE `kegiatan`
  ADD PRIMARY KEY (`ID_Kegiatan`),
  ADD KEY `F_ID_Admin` (`F_ID_Admin`);

--
-- Indexes for table `komentar`
--
ALTER TABLE `komentar`
  ADD PRIMARY KEY (`ID_komentar`),
  ADD KEY `F_ID_Pengguna` (`F_ID_Pengguna`),
  ADD KEY `F_ID_Kegiatan` (`F_ID_Kegiatan`);

--
-- Indexes for table `komunitas`
--
ALTER TABLE `komunitas`
  ADD PRIMARY KEY (`ID_Komunitas`),
  ADD KEY `F_ID_Admin` (`F_ID_Admin`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pelapor`
--
ALTER TABLE `pelapor`
  ADD PRIMARY KEY (`ID_Pelapor`),
  ADD UNIQUE KEY `No_HP` (`No_HP`);

--
-- Indexes for table `pengguna`
--
ALTER TABLE `pengguna`
  ADD PRIMARY KEY (`ID_pengguna`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `ID_Admin` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `informasi`
--
ALTER TABLE `informasi`
  MODIFY `ID_Informasi` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121;

--
-- AUTO_INCREMENT for table `kegiatan`
--
ALTER TABLE `kegiatan`
  MODIFY `ID_Kegiatan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `komentar`
--
ALTER TABLE `komentar`
  MODIFY `ID_komentar` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=281;

--
-- AUTO_INCREMENT for table `komunitas`
--
ALTER TABLE `komunitas`
  MODIFY `ID_Komunitas` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `menu`
--
ALTER TABLE `menu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pelapor`
--
ALTER TABLE `pelapor`
  MODIFY `ID_Pelapor` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10041;

--
-- AUTO_INCREMENT for table `pengguna`
--
ALTER TABLE `pengguna`
  MODIFY `ID_pengguna` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `informasi`
--
ALTER TABLE `informasi`
  ADD CONSTRAINT `informasi_ibfk_1` FOREIGN KEY (`F_ID_Pelapor`) REFERENCES `pelapor` (`ID_Pelapor`),
  ADD CONSTRAINT `informasi_ibfk_2` FOREIGN KEY (`F_ID_Admin`) REFERENCES `admin` (`ID_Admin`);

--
-- Constraints for table `kegiatan`
--
ALTER TABLE `kegiatan`
  ADD CONSTRAINT `kegiatan_ibfk_1` FOREIGN KEY (`F_ID_Admin`) REFERENCES `admin` (`ID_Admin`);

--
-- Constraints for table `komentar`
--
ALTER TABLE `komentar`
  ADD CONSTRAINT `komentar_ibfk_1` FOREIGN KEY (`F_ID_Pengguna`) REFERENCES `pengguna` (`ID_Pengguna`),
  ADD CONSTRAINT `komentar_ibfk_2` FOREIGN KEY (`F_ID_Kegiatan`) REFERENCES `kegiatan` (`ID_Kegiatan`);

--
-- Constraints for table `komunitas`
--
ALTER TABLE `komunitas`
  ADD CONSTRAINT `komunitas_ibfk_1` FOREIGN KEY (`F_ID_Admin`) REFERENCES `admin` (`ID_Admin`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
