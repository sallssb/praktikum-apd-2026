print ("================================")
print ("          TOP UP STORE          ")
print ("================================")

katalog = [
    {"game": "Mobile Legends", "item": 86, "harga": 20000, "status": "tersedia"},
    {"game": "Mobile Legends", "item": 172, "harga": 40000, "status": "tersedia"},
    {"game": "Mobile Legends", "item": 257, "harga": 60000, "status": "tersedia"},
    {"game": "Mobile Legends", "item": 344, "harga": 80000, "status": "tersedia"},
    {"game": "Mobile Legends", "item": 429, "harga": 100000, "status": "tersedia"},

    {"game": "Free Fire", "item": 70, "harga":10000, "status": "tersedia"},
    {"game": "Free Fire", "item": 140, "harga": 20000, "status": "tersedia"},
    {"game": "Free Fire", "item": 355, "harga": 50000, "status": "tersedia"},
    {"game": "Free Fire", "item": 720, "harga": 100000, "status": "tersedia"},
    {"game": "Free Fire", "item": 1450, "harga": 200000, "status": "tersedia"},

    {"game": "PUBG", "item": 60, "harga": 15000, "status": "tersedia"},
    {"game": "PUBG", "item": 325, "harga": 75000, "status": "tersedia"},
    {"game": "PUBG", "item": 660, "harga": 150000, "status": "tersedia"},
    {"game": "PUBG", "item": 1800, "harga": 375000, "status": "tersedia"},
    {"game": "PUBG", "item": 3850, "harga": 750000, "status": "tersedia"},

    {"game": "Genshin Impact", "item": 60, "harga": 16000, "status": "teresdia"},
    {"game": "Genshin Impact", "item": 300, "harga": 79000, "status": "tersedia"},
    {"game": "Genshin Impact", "item": 980, "harga": 249000, "status": "tersedia"},
    {"game": "Genshin Impact", "item": 1980, "harga": 479000, "status": "tersedia"},
    {"game": "Genshin Impact", "item": 3850, "harga": 799000, "status": "tersedia"},

    {"game": "Roblox", "item": 80, "harga": 15000, "status": "tersedia"},
    {"game": "Roblox", "item": 400, "harga": 75000, "status": "tersedia"},
    {"game": "Roblox", "item": 800, "harga": 150000, "status": "tersedia"},
    {"game": "Roblox", "item": 1700, "harga": 300000, "status": "tersedia"},
    {"game": "Roblox", "item": 4500, "harga": 750000, "status": "tersedia"},

]

daftar_game = [
    "Mobile Legends",
    "Free Fire",
    "PUBG",
    "Genshin Impact",
    "Roblox"
 ]

mata_uang = [
    "Diamond",
    "Diamond",
    "UC",
    "Genesis Crystal",
    "Robux" 
]

transaksi = []
nomor_transaksi = 1

while True: 
    print ("\n===== SISTEM TOP UP GAME =====")
    print ("1. Admin/ Sistem")
    print ("2. Player")
    print ("3. Logout")

    role = input("Pilih menu: ")

    #===============
    #     ADMIN
    #===============

    if role == "1":
        print ("\n===== LOGIN ADMIN =====")

        username = input ("Username: ")
        password = input ("Password: ")

        if username == "salwa" and password == "65":
            print ("Login Berhasil")

            while True:
                print ("\n===== MENU ADMIN =====")
                print ("1. Create - Tambah Paket")
                print ("2. Read - Lihat Data")
                print ("3. Update - Perbarui Data")
                print ("4. Delete - Hapus Paket")
                print ("5. Kembali")
                
                menu = input ("Pilih menu: ")

                if menu == "1":
                    print ("\n===== TAMBAH PAKET =====")

                    for i in range(len(daftar_game)):
                        print (i + 1, ".", daftar_game[i])
                        
                    pilih = input("Pilih game: ")

                    if pilih in ["1", "2", "3", "4", "5"]:
                        game = daftar_game[int(pilih)-1]
                        item = int (input("Jumlah item: "))
                        harga = int (input("Harga: Rp "))

                        if item > 0 and harga > 0:
                            data = {
                                "game": game,
                                "item": item,
                                "harga": harga,
                                "status": "Tersedia"
                            }

                            katalog.append (data)
                            print ("Paket berhasil ditambahkan!")
                        else:
                            print ("Data tidak valid!")
                    else:
                        print ("Game tidak tersedia!")

                elif menu == "2":
                    print ("\n===== KATALOG TOP UP")

                    for game in daftar_game:
                        print ("\ngame: ", game)
                        nomor = 1

                        for data in katalog:
                            if data ["game"] == game:
                                print(
                                    nomor, ".",
                                    data["item"],
                                    "- Rp", data ["harga"],
                                    "-", data ["status"]
                                )
                                nomor +=1
                    print("\n===== DATA TRANSAKSI =====")

                    if len(transaksi) == 0:
                        print ("Belum ada transaksi.")
                    else: 
                        for data in transaksi:
                            print ("--------------------")
                            print ("No Transaksi:", data ["nomor"])
                            print ("ID Player:", data ["player"])
                            print ("Game:", data["item"])
                            print ("Total: Rp", data["total"])
                            print ("Status:", data["status"]) 

                elif menu == "3":
                    print ("\n===== UPDATE DATA =====")
                    print ("1. Ubah harga paket") 
                    print ("2. Ubah ketersediaan") 
                    print ("3. Ubah status transaksi")

                    pilih = input ("Pilih menu: ")

                    if pilih == "1" or pilih == "2":
                        print ("\n===== PILIH GAME =====")

                        for i in range(len(daftar_game)):
                            print(i + 1, ".", daftar_game[i])

                        pilih_game = input ("Pilih game:")

                        if pilih_game in ["1", "2", "3", "4", "5"]:
                            game = daftar_game[int(pilih_game)-1]
                            paket_game = []

                            for data in katalog:
                                if data ["game"] == game:
                                    paket_game.append(data)

                            for i in range(len(paket_game)):
                                print(
                                    i + 1, ".",
                                    paket_game[i]["item"],
                                    "- Rp",
                                    paket_game[i]["harga"],
                                    "-",
                                    paket_game[i]["status"]
                                )
                            nomor = int(input("Pilih nomor paket: "))

                            if 1 <= nomor <= len(paket_game):
                                data = paket_game[nomor - 1]

                                if pilih == "1":
                                    harga = int(input(
                                        "Harga baru: Rp"
                                    ))

                                    if harga > 0:
                                        data ["Harga"] = harga
                                        print ("Harga diperbarui")
                                    else:
                                        print("Harga tidak valid")
                                    
                                elif pilih == "2":
                                    print("1. tersedia")
                                    print("2. tidak tersedia")
                                    status = input("Pilih: ")

                                    if status =="1":
                                        data ["status"] = "tersedia"
                                        print("Status diperbarui!")
                                    elif status == "2":
                                        data ["status"] = "tersedia"
                                        print("Status diperbarui!")
                                    else:
                                        print("Pilihan tidak valid!")

                            else:
                                print("Paket tidak ditemukan!")
                        else:
                            print("Game tidak tersedia!")

                    elif pilih == "3":
                        cari = int(input("Nomor transaksi:")) 
                        ditemukan = False

                        for data in transaksi:
                            if data ["nomor"] == cari:
                                ditemukan = True

                                print("1. Menunggu")
                                print("2. Diproses")
                                print("3. Berhasil")
                                status = input("Pilih: ")

                                if status == "1":
                                    data["status"] = "Menunggu"
                                elif status == "2":
                                    data["status"] = "Diproses"
                                elif status == "3":
                                    data["status"] = "Berhasil"
                                else:
                                    print("Pilihan tidak valid!")
                                    break
                                
                                print ("Status diperbarui!")
                                break

                        if not ditemukan:
                            print("Transaksi tidak ditemukan!")

                    else:
                        print("Pilih tidak tersedia!")

                elif menu == "4":
                    print("\n===== HAPUS PAKET ======")

                    for i in range(len(daftar_game)):
                        print(i + 1, ".", daftar_game[i])

                    pilih_game = input("Pilih game: ")

                    if pilih_game in ["1", "2", "3", "4", "5"]:
                        game = daftar_game[int(pilih_game) -1]
                        paket_game = []

                        for data in katalog:
                            if data ["game"] == game:
                                paket_game.append(data)

                        for i in range(len(paket_game)):
                            print(
                                i + 1, ".",
                                paket_game[i]["item"],
                                "- Rp",
                                paket_game[i]["harga"]
                            )

                        if len(paket_game) > 0:
                            nomor = int(input("Pilih nomor: "))

                            if 1 <= nomor <= len(paket_game):
                                data = paket_game[nomor -1]

                                yakin = input(
                                    "Yakin hapus paket? (y/n)"
                                )

                                if yakin.lower() == "y":
                                    katalog.remove(data)
                                    print("Paket berhasil dihapus!")
                                else:
                                    print("Penghapusan dibatalkan!")
                            else:
                                print("Paket tidak ditemukan!")
                        else:
                            print("Belum ada paket!")
                    else:
                        print("Game tidak tersedia!")

                elif menu == "5":
                    print("Logout berhasil!")
                    break
                else:
                    print("Menu tidak tersedia!")

        else:
            print("Username atau password salah!")

#================
#     PLAYER
#================
    elif role == "2":

        while True:
            print("\n===== MENU PLAYER =====")
            print("1. Lihat katalog")
            print("2. Top up game")
            print("3. Cek status transaksi")
            print("4. Kembali")

            menu = input("Pilih menu: ")

            if menu == "1":
                print("\n===== KATALOG TOP UP =====")

                for i in range(len(daftar_game)):
                    game = daftar_game [i]
                    satuan = mata_uang [i]

                    print("\n=====", game, "=====")
                    nomor = 1

                    for data in katalog:
                        if (data["game"] == game and
                                data["status"] == "tersedia"):
                            print(
                                nomor,".",
                                data["item"], satuan,
                                "- Rp", data["harga"]
                            )
                            nomor += 1

            elif menu == "2":
                print("\n===== PILIH GAME =====")

                for i in range(len(daftar_game)):
                    print(i + 1, ".", daftar_game[i])

                pilih_game = input("Pilih game (1-5): ")

                if pilih_game in ["1", "2", "3", "4", "5"]:
                    indeks = int(pilih_game) -1
                    game = daftar_game[indeks]
                    satuan = mata_uang[indeks]

                    paket_tersedia = []

                    for data in katalog:
                        if (data["game"] == game and
                                data["status"] == "tersedia"):
                            paket_tersedia.append(data)

                    print("\n===== PAKET", game, "=====")

                    for i in range(len(paket_tersedia)):
                        data = paket_tersedia[i]
                        print(
                            i + 1, ".",
                            data["item"], satuan,
                            "- Rp", data["harga"]
                        )

                    if len(paket_tersedia) > 0:
                        pilihan = int(input("Pilih nomor paket: "))

                        if 1 <= pilihan <= len(paket_tersedia):
                            paket = paket_tersedia[pilihan - 1]

                            player = input("Masukkan ID Player: ")
                            jumlah = int(input("Jumlah paket: "))

                            if player != "" and jumlah > 0:
                                total = paket["harga"] * jumlah
                                total_item = paket["item"] * jumlah

                                pesanan = {
                                    "nomor": nomor_transaksi,
                                    "player": player,
                                    "game": game,
                                    "item": total_item,
                                    "satuan": satuan,
                                    "total": total,
                                    "status": "Menunggu"
                                } 

                                transaksi.append(pesanan)

                                print("\n===== DETAIL PESANAN =====")
                                print("No transaksi:", nomor_transaksi)
                                print("Game:", game)
                                print("ID player:", player)
                                print("Jumlah:", total_item, satuan)
                                print("Total harga: Rp", total)
                                print("Status: Menunggu")

                                nomor_transaksi += 1
                            else:
                                print("Data tidak valid!")
                        else:
                            print("Pilihan paket tidak tersedia!")
                    else:
                        print("Belum ada paket tersedia!")
                else:
                    print("Pilihan game tidak valid!")

            elif menu == "3":
                print("\n===== CEK STATUS TRANSAKSI =====")

                cari = int(input("Nomor transaksi: "))
                player = input("ID player:")
                ditemukan = False

                for data in transaksi:
                    if (data["nomor"] == cari and
                            data["player"] == player):
                        ditemukan = True

                        print("Game:", data["game"])
                        print("Jumlah:", data["item"],
                               data["satuan"])
                        print("Total: Rp", data ["total"])
                        print("Status:", data["status"])
                        break

                if not ditemukan:
                    print("Transaksi tidak ditemukan!")

            elif menu == "4":
                print("Kembali ke menu utama.")
                break

            else:
                print("Menu tidak tersedia!")

    elif role == "3":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak tersedia!")
