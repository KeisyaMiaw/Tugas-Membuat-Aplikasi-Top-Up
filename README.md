# Tugas-Membuat-Aplikasi-Top-Up
![1](https://github.com/user-attachments/assets/47484522-d058-4027-9b04-a0dc777605cf)
![2](https://github.com/user-attachments/assets/665cf9c0-a50d-4308-a739-23b7abcd1f0b)

Kelas Toko
Kelas Toko ini dirancang untuk mengelola saldo dan gems dalam aplikasi.
Konstruktor __init__:
self.user: Dictionary yang menyimpan informasi pengguna:
"saldo": Saldo awal sebesar 300.000 rupiah.
"gems": Jumlah gems yang dimiliki, diatur awalnya 0.
self.kurs: Kurs konversi, diatur sebesar 1 gem = 1.000 rupiah. Catatan: Ada ketidaksesuaian antara komentar dan nilai, yang seharusnya 1 gem = 10.000 saldo.
Metode saldo_ke_gems:

Menerima parameter jumlah_saldo, yang merupakan jumlah saldo yang ingin diubah menjadi gems.
Memeriksa apakah jumlah_saldo melebihi saldo yang tersedia. Jika iya, mencetak pesan bahwa saldo tidak cukup dan mengembalikan False.
Menghitung jumlah gems yang didapat dengan membagi jumlah_saldo dengan self.kurs.
Mengupdate jumlah gems dan saldo pengguna.
Mencetak pesan konfirmasi jika berhasil.
Metode buy_barang:

Menerima parameter nama_barang dan gems_prices.
Memeriksa apakah gems_prices lebih besar dari jumlah gems yang dimiliki. Jika tidak cukup, mencetak pesan dan mengembalikan False.
Jika cukup, mengurangi jumlah gems yang dimiliki dan mencetak pesan bahwa pembelian berhasil.
Metode status:
Mencetak saldo dan jumlah gems pengguna saat ini.
Fungsi main
Fungsi ini bertanggung jawab untuk interaksi pengguna melalui antarmuka berbasis teks:

Loop Utama:
Menggunakan while True untuk membuat program terus berjalan hingga pengguna memilih untuk keluar.
Menampilkan menu pilihan untuk top-up, membeli barang, cek status, dan keluar.
Pengolahan Pilihan Pengguna:
Jika opsi '1' (Top Up):
Meminta pengguna memasukkan jumlah saldo yang ingin di-top up.
Memanggil metode saldo_ke_gems untuk mengonversi saldo menjadi gems. Catatan: Ada pemanggilan ganda toko.saldo_ke_gems(jumlah_saldo) yang seharusnya dihapus.
Jika opsi '2' (Beli Barang):
Meminta pengguna memasukkan nama barang dan harga barang dalam gems. Namun, metode buy_barang tidak dipanggil, sehingga pembelian tidak akan dilakukan.
Jika opsi '3' (Cek Status):
Memanggil metode status untuk menampilkan informasi saldo dan gems, tetapi tidak menggunakan tanda kurung. Seharusnya toko.status().
Jika opsi '4' (Keluar):
Mencetak pesan terima kasih dan keluar dari loop.
Jika opsi tidak valid: Mencetak pesan bahwa opsi tidak valid.
Perbaikan yang Diperlukan
Menghapus Pemanggilan Ganda: Hapus pemanggilan kedua dari toko.saldo_ke_gems(jumlah_saldo) pada opsi '1'.
Menambahkan Pemanggilan untuk Pembelian Barang: Di opsi '2', tambahkan toko.buy_barang(nama_barang, gems_prices) agar pembelian dapat dilakukan.
Memperbaiki Pemanggilan Status: Ubah toko.status menjadi toko.status() agar metode benar-benar dipanggil.
Penanganan Kesalahan: Tambahkan penanganan kesalahan untuk input yang tidak valid, seperti jika pengguna memasukkan karakter alih-alih angka.
