print('=================================')
print('Nama  : Keisya Siti Nafisa Andini')
print('NIM   : 2409116115               ')
print('Kelas : Sistem Informasi C       ')
print('=================================')

import os
os.system('cls')

class Toko:
    os.system("cls")
    def __init__(self):
        # Penyelesaian saldo dan gems
        self.user = {
            "saldo": 300000, # saldo dalam bentuk rupiah
            "gems": 0        # gems awal
        }
        self.kurs = 1000  # 1 gems = 10000 saldo

    def saldo_ke_gems(self, jumlah_saldo):
        os.system("cls")
        if jumlah_saldo > self.user['saldo']:
            print('Maaf, Saldo Anda tidak mencukupi untuk melakukan top up.')
            return False
        
        gems_plus = jumlah_saldo // self.kurs
        self.user['gems'] += gems_plus
        self.user['saldo'] -= jumlah_saldo
        print(f'Anda Berhasil top up {jumlah_saldo} menjadi {gems_plus} gems.')
        return True
        
    def buy_barang(self, nama_barang, gems_prices):
        if gems_prices > self.user['gems']:
            print('Gems Anda tidak mencukui untuk melakukan transaksi, silahkan Anda top up terlebih dahulu.')
            return False
        
        self.user['gems'] -= gems_prices
        print(f'Pembelian {nama_barang} berhasil! Anda telah menghabiskan {gems_prices} gems.')
        return True
    
    def status(self):
        print(f"Saldo Anda: {self.user['saldo']} || Gems Anda: {self.user['gems']}")

# Fungsi untuk berinteraksi dengan user
def main():
    os.system("cls")
    toko = Toko()

    while True:
        print('\n1. Top up')
        print('2. Beli Barang')
        print('3. Cek Status')
        print('4. Keluar')
        opsi = input ('Silahkan masukkan opsi Anda: ')

        if opsi =='1':
            jumlah_saldo = int(input('Masukkan jumlah nominal top up: '))
            toko.saldo_ke_gems(jumlah_saldo)
            toko.saldo_ke_gems(jumlah_saldo)
        elif opsi == '2':
            nama_barang = input('Masukkan nama barang: ')
            gems_prices = int(input('Masukkan harga barang dalam gems: '))
        elif opsi == '3':
            toko.status
        elif opsi == '4':
            print("Terimakasih sudah melakukan Top up di aplikasi kami!")
            break
        else:
            print('Opsi tidak valid.')

if __name__ == "__main__":
    main()