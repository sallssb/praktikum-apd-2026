import data

def hitung_total(harga, jumlah):
    total_harga = int(harga) * int(jumlah)
    return total_harga

def hitung_item(item, jumlah):
    total_item = int(item) * int(jumlah)
    return total_item

def ambil_nomor_transaksi():
    nomor_baru = data.nomor_transaksi
    data.nomor_transaksi += 1

    return nomor_baru

def jumlah_semua_paket():
    jumlah = 0

    for paket in data.katalog.values():
        jumlah += len(paket)

    return jumlah

def tampilkan_header():
    print("===============================================")
    print("                 TOP UP STORE                  ")
    print("===============================================")

def tampilkan_menu_utama():

    print("\n===== Menu Utama =====")
    print("1. Login Admin")
    print("2. Registrasi Player")
    print("3. Login Player")
    print("4. Keluar")