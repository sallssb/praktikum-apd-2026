from prettytable import PrettyTable
import data

def tapilkan_katalog():

    tabel = PrettyTable()

    tabel.field_names = [
        "No",
        "Game",
        "Item",
        "Harga",
        "Status"
    ]
    
    nomor = 1

    for game, paket in data.katalog.items():

        for item, info in paket.items():

            tabel.add_row([
                nomor,
                game,
                str(item) + " " + data.mata_uang[game],
                "Rp " + str(info["harga"]),
                info["status"]
            ])
            nomor += 1

    print("\n===== KATALOG TO UP =====")
    print("Jumlah Paket:", len(tabel.rows))
    print(tabel)

def tampilkan_transaksi():

    tabel = PrettyTable()

    tabel.field_names = [
        "Nomor Transaksi",
        "Username",
        "ID Player",
        "Game",
        "Item",
        "Jumlah Paket",
        "Total Harga",
        "Status"
    ]

    for nomor_transaksi, info in data.transaksi.items():
        
        tabel.add_row([
            nomor_transaksi,
            info["username"],
            info["player"],
            info["game"],
            info["item"],
            info["jumlah_paket"],
            "Rp{:,.0f} ". format(info["total"]),
            info["status"]
        ])

    print("\n===== DATA TRANSAKSI =====")

    if len(data.transaksi) == 0:
        print("Belum ada transaksi")

    else:
        print(tabel)

def create_paket():

    while True:

        print("\n===== CREATE PAKET =====")
        print("0. Kembali ke menu Admin")

        for nomor, game in data.daftar_game.items():
            print(nomor, ".", game)

        pilih = input("Pilih game: ")


        if pilih == "0":
            break

        elif not pilih.isdigit():
            print("Error! Pilihan harus berupa angka!")

        elif int(pilih) not in data.daftar_game:
            print("Error! Game tidak tersedia!")

        else:

            game = data.daftar_game[int(pilih)]

            item = input("Masukkan jumlah item: ")
            harga = input("Masukkan harga paket: Rp")

            if not item.isdigit() or not harga.isdigit():
                print("Item dan Harga harus berupa angka!")
                continue

            item = int(item)
            harga = int(harga)

            if item <= 0 or harga <= 0:
                print("Error! Nilai harus lebih dari 0!")
                continue
            
            elif item in data.katalog[game]:
                print("Error! Paket sudah tersedia!")
                continue

            else:

                data.katalog[game][item] = {
                    "harga": harga,
                    "status": "tersedia"
                }

                print("Paket berhasil ditambahkan!")
                print("Game:", game)
                print("Item:", item, data.mata_uang[game])
                print("Harga: Rp", harga)

def read_data():

    while True:

        print("\n===== READ DATA =====")
        print("1. Lihat Katalog")
        print("2. Lihat Transaksi")
        print("0. Kembali ke menu Admin")

        pilih = input("Pilih menu: ")

        if pilih == "0":
            break

        elif pilih == "1":
            tapilkan_katalog()

        elif pilih == "2":
            tampilkan_transaksi()

        else:
            print("Error! Pilihan tidak tersedia!")

def update_data():
    
    while True:

        print("\n===== UPDATE DATA =====")
        print("1. Ubah Harga Paket")
        print("2. Ubah Ketersediaan Paket")
        print("3. Ubah Status Transaksi")
        print("0. Kembali ke menu Admin")

        pilih = input("Pilih menu: ")

        if pilih == "0":
            break

        elif pilih == "1" or pilih == "2":

            print("\n===== PILIH GAME =====")

            for nomor, game in data.daftar_game.items():
                print(nomor, ".", game)

            pilih_game = input("Pilih game: ")

            if pilih_game == "0":
                continue

            elif not pilih_game.isdigit():
                print("Error! Pilihan harus berupa angka!")
                continue

            elif int(pilih_game) not in data.daftar_game:
                print("Error! Game tidak tersedia!")
                continue

            game = data.daftar_game[int(pilih_game)]

            daftar_item = list(data.katalog[game])

            if len(daftar_item) == 0:
                print("Paket Belum Tersedia!")
                continue

            print("\n===== DAFTAR PAKET =====")

            for nomor, item in enumerate(daftar_item, start=1):

                detail = data.katalog[game][item]

                print(
                    nomor, ".", item,
                    "| Rp{:,.0f}".format(detail["harga"]),
                    "|", detail["status"]
                )

            nomor_paket = input("Pilih nomor paket: ")

            if not nomor_paket.isdigit():
                print("Error! Pilihan harus berupa angka!")
                continue

            nomor_paket = int(nomor_paket)

            if not 1 <= nomor_paket <= len(daftar_item):
                print("Error! Paket tidak ditemukan!")
                continue

            item = daftar_item[nomor_paket - 1]

            if pilih == "1":

                harga = input("Masukkan harga baru: Rp")

                if not harga.isdigit() or int(harga) <= 0:
                    print("Error! Harga harus berupa angka dan lebih dari 0!")
                    continue

                else:

                    data.katalog[game][item]['harga'] = int(harga)
                    print("Harga paket berhasil diubah!")
                    print("Game:", game)
                    print("Item:", item, data.mata_uang[game])
                    print("Harga baru: Rp", harga)

                    print("Harga berhasil diperbarui!")

            elif pilih == "2":

                print("1. Tersedia")
                print("2. Tidak Tersedia")
                print("0. Kembali")

                status = input("Pilih Status: ")

                if status == "0":
                    continue

                elif status == "1":
                    data.katalog[game][item]["status"] = "tersedia"
                    print("Paket berhasil diubah menjadi tersedia!")

                elif status == "2":
                    data.katalog[game][item]["status"] = "tidak tersedia"
                    print("Paket berhasil diubah menjadi tidak tersedia!")

                else:
                    print("Pilihan status tidak tersedia!")

        elif pilih == "3":

            tampilkan_transaksi()

            if len(data.transaksi) == 0:
                continue

            nomor = input(
                "Masukkan nomor transaksi: "
            )

            if not nomor.isdigit():
                print("Error! Pilihan harus berupa angka!")
                continue

            nomor = int(nomor)

            if nomor not in data.transaksi:
                print("Error! Transaksi tidak ditemukan!")
                continue

            print("\n===== STATUS TRANSAKSI =====")
            print("1. Menunggu")
            print("2. Diproses")
            print("3. Berhasil")
            print("0. Kembali")

            status = input("Pilih status baru: ")

            if status == "0":
                continue

            elif status == "1":
                data.transaksi[nomor]["status"] = "menunggu"
                print("Status transaksi berhasil diubah menjadi menunggu!")
            elif status == "2":
                data.transaksi[nomor]["status"] = "diproses"
                print("Status transaksi berhasil diubah menjadi diproses!")
            elif status == "3":
                data.transaksi[nomor]["status"] = "berhasil"
                print("Status transaksi berhasil diubah menjadi berhasil!")
            else:
                print("Pilihan status tidak tersedia!")
                continue

def delete_paket():

    while True:

        print("\n===== HAPUS PAKET =====")
        print("0. Kembali ke Menu Admin")

        for nomor, game in data.daftar_game.items():
            print(nomor, ".", game)

        pilih_game = input("Pilih game: ")
        
        if pilih_game == "0":
            break

        elif not pilih_game.isdigit():
            print("Error! Pilihan harus berupa angka!")
            continue

        elif int(pilih_game) not in data.daftar_game:
            print("Error! Game tidak tersedia!")
            continue

        game = data.daftar_game[int(pilih_game)]

        paket_game = data.katalog[game]

        if len(paket_game) == 0:
            print("Paket Belum Tersedia!")
            continue

        tabel = PrettyTable()

        tabel.field_names = [
            "No",
            "Item",
            "Harga",
            "Status"
        ]

        daftar_item = list(paket_game.keys())

        for nomor, item in enumerate(daftar_item, start=1):

            info = paket_game[item]

            tabel.add_row([
                nomor,
                str(item) + " " + data.mata_uang[game],
                "Rp{:,.0f}".format(info["harga"]),
                info["status"]
            ])

        print(tabel)

        nomor_paket = input("Pilih nomor paket: ")

        if not nomor_paket.isdigit():
            print("Nomor Paket harus berupa angka!")
            continue

        nomor_paket = int(nomor_paket)

        if not 1 <= nomor_paket <= len(daftar_item):
            print("Error! Paket tidak ditemukan!")
            continue

        item = daftar_item[nomor_paket - 1]

        yakin = input(
            "Yakin ingin menghapus paket? (y/n): "
        )

        if yakin == "y":

            del data.katalog[game][item]

            print("Paket berhasil dihapus!")

        elif yakin == "n":
            print("Paket batal dihapus!")

        else:
            print("Pilihan tidak tersedia!")

def menu_admin():

    while True:

        print("\n===== MENU ADMIN =====")
        print("1. Create - Tambah Paket")
        print("2. Read - Lihat Data")
        print("3. Update - Perbarui Data")
        print("4. Delete - Hapus Paket")
        print("5. Logout")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            create_paket()

        elif pilih == "2":
            read_data()

        elif pilih == "3":
            update_data()

        elif pilih == "4":
            delete_paket()

        elif pilih == "5":
            print("Logout Admin berhasil!")
            break

        else:
            print("Error! Pilihan tidak tersedia!")