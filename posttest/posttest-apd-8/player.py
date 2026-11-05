from prettytable import PrettyTable
import data

from fungsi import (
    hitung_total,
    hitung_item,
    ambil_nomor_transaksi
)

def register_player():

    print("\n===== REGISTER PLAYER =====")

    username = input("Buat username: ")
    password = input("Buat password: ")
    konfirmasi = input("Konfirmasi password: ")

    if username == "" or password == "":
        print("\nUsername dan password tidak boleh kosong!")
        
    elif username in data.akun_player:
        print("Username sudah terdaftar!")

    elif len(password) < 6:
        print("Password minimal terdiri dari 6 karakter!")

    elif password != konfirmasi:
        print("Konfirmasi password tidak cocok!")

    else:

        data.akun_player[username] = password

        print("Regostrasi berhasil!")
        print("Silahkan login sebagai player.")

def login_player():

    print("\n===== LOGIN PLAYER =====")

    username = input("Username: ")
    password = input("Password: ")

    if username == "" or password == "":
        print("Data tidak boleh kosong!")
        return None

    elif username not in data.akun_player:
        print("Username belum terdaftar!")
        return None

    elif data.akun_player[username] != password:
        print("Password salah!")
        return None

    else:

        print("Login Player berhasil!")

        return username

def lihat_katalog():

    print("\n===== KATALOG TOP UP =====")

    tabel = PrettyTable()

    tabel.field_names =[
        "No",
        "Game",
        "Item",
        "Harga",
        "Status"
    ]

    nomor = 1

    for game, paket in data.katalog.items():

        for item, detail in paket.items():

            tabel.add_row([
                nomor,
                game,
                item,
                "Rp{:,}".format(detail["harga"]),
                detail["status"]
            ])

            nomor += 1

    print(tabel)

def proses_topup(username):

    while True:

        print("\n===== PILIH GAME =====")
        
        for nomor, game in data.daftar_game.items():
            print(nomor, ":", game)

        print("0 : Kembali ke menu player")

        pilih = input("\nPilih game: ")

        if pilih == "0":
            break

        if not pilih.isdigit():
            print("\nPilihan harus berupa angka!")
            continue

        if int(pilih) not in data.daftar_game:
            print("\nPilihan tidak tersedia!")
            continue

        game = data.daftar_game[int(pilih)]

        paket_tersedia = {}

        for item, detail in data.katalog[game].items():
            if detail["status"] == "tersedia":
                paket_tersedia[item] = detail

        if len(paket_tersedia) == 0:
            print("\nTidak ada paket yang tersedia!")
            continue

        print("\n===== PAKET", game.upper(), "=====")

        tabel = PrettyTable()
        tabel.field_names = [
            "No",
            "Item",
            "Satuan",
            "Status"
        ]

        daftar_item = list(paket_tersedia.keys())

        for nomor, item in enumerate(daftar_item, start=1):

            harga = paket_tersedia[item]["harga"]

            tabel.add_row([
                nomor,
                item,
                data.mata_uang[game],
                "Rp{:,.0f}".format(harga)
            ])
            
        print(tabel)

        nomor_paket = input("\nPilih nomor paket: ")

        if not nomor_paket.isdigit():
            print("\nPilihan harus berupa angka!")
            continue

        nomor_paket = int(nomor_paket)

        if nomor_paket < 1 or nomor_paket > len(daftar_item):
            print("\nPilihan paket tidak tersedia!")
            continue

        item = daftar_item[nomor_paket - 1]

        harga= int(paket_tersedia[item]["harga"])

        id_player = input("Masukkan ID player: ")

        jumlah = input("Masukkan jumlah paket: ")
        
        if not jumlah.isdigit() or int(jumlah) <= 0:
            print("\nJumlah paket tidak valid!")
            continue
        
        jumlah = int(jumlah)

        total = hitung_total(harga, jumlah)
        total_item = hitung_item(item, jumlah)

        satuan = data.mata_uang[game]

        print("\n===== KONFIRMASI TOP UP =====")
        print("Username: ", username)
        print("Game: ", game)
        print("Player ID: ", id_player)
        print("Item: ", total_item, satuan)
        print("Jumlah Paket: ", jumlah)
        print("Harga Satuan: Rp{:,.0f}".format(harga))
        print("Total Harga: Rp{:,.0f}".format(total))

        konfirmasi = input(
            "\nLanjutkan transaksi? (y/n): "
        )

        if konfirmasi == "y":

            nomor = ambil_nomor_transaksi()

            data.transaksi[nomor] = {
                "username": username,
                "player": id_player,
                "game": game,
                "item": total_item,
                "satuan": satuan,
                "harga_satuan": harga,
                "jumlah_paket": jumlah,
                "total": total,
                "status": "Menunggu"
            }

            print("\nTransaksi berhasil dibuat!")
            print("Nomor Transaksi: ", nomor)
            print("Status: Menunggu")

        elif konfirmasi == "n":

            print("\nTransaksi dibatalkan!")

        else:
            print("\nPilihan tidak tersedia!")

def cek_transaksi(username):

    print("\n===== RIWAYAT TRANSAKSI =====")

    tabel = PrettyTable()

    tabel.field_names = [
        "No Transaksi",
        "Game",
        "Player ID",
        "Item",
        "Jumlah",
        "Total Harga",
        "Status"
    ]

    ada_transaksi = False

    for nomor, detail in data.transaksi.items():

        if detail["username"] == username:

            ada_transaksi = True

            tabel.add_row([
                nomor,
                detail["game"],
                detail["player"],
                str(detail["item"]) + " " + detail ["satuan"],
                detail["jumlah_paket"],
                "Rp{:,.0f}".format(detail["total"]),
                detail["status"]
            ])

    if ada_transaksi:
        print(tabel)

    else:
        print("\nBelum ada transaksi!")

def menu_player(username):

    while True:

        print("\n====================")
        print("     MENU PLAYER      ")
        print("====================")
        print("1. Lihat Katalog")
        print("2. Top Up Game")
        print("3. Lihat Riwayat Transaksi")
        print("4. Logout")

        pilih = input("\nPilih menu: ")

        if pilih == "1":

            lihat_katalog()

        elif pilih == "2":

            proses_topup(username)

        elif pilih == "3":

            cek_transaksi(username)

        elif pilih == "4":

            print("\nLogout Player berhasil!")
            break

        else:

            print("\nPilihan menu tidak tersedia!")