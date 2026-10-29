import os

print ("================================")
print ("          TOP UP STORE          ")
print ("================================")

katalog = {
    "Mobile Legends": {
         86 : {"harga": 20000, "status": "tersedia"},
        172 : {"harga": 40000, "status": "tersedia"},
        257 : {"harga": 60000, "status": "tersedia"},
        344 : {"harga": 80000, "status": "tersedia"},
        429 : {"harga": 100000, "status": "tersedia"},
    },

    "Free Fire": {
        70 : {"harga":10000, "status": "tersedia"},
        140 : {"harga": 20000, "status": "tersedia"},
        355 : {"harga": 50000, "status": "tersedia"},
        720 : {"harga": 100000, "status": "tersedia"},
        1450 : {"harga": 200000, "status": "tersedia"},
    },

    "PUBG": {
        60 : {"harga": 15000, "status": "tersedia"},
        325 : {"harga": 75000, "status": "tersedia"},
        660 : {"harga": 150000, "status": "tersedia"},
        1800 : {"harga": 375000, "status": "tersedia"},
        3850 : {"harga": 750000, "status": "tersedia"},
    },

    "Genshin Impact": {
        60 : {"harga": 16000, "status": "teresdia"},
        300 : {"harga": 79000, "status": "tersedia"},
        980 : {"harga": 249000, "status": "tersedia"},
        1980 : {"harga": 479000, "status": "tersedia"},
        3850 : {"harga": 799000, "status": "tersedia"},
    },

    "Roblox" : {
        80 : {"harga": 15000, "status": "tersedia"},
        400 : {"harga": 75000, "status": "tersedia"},
        800 : {"harga": 150000, "status": "tersedia"},
        1700 : {"harga": 300000, "status": "tersedia"},
        4500 : {"harga": 750000, "status": "tersedia"},
    },
}

mata_uang = {
    "Mobile Legends" : "Diamond",
    "Free Fire" : "Diamond",
    "PUBG" : "UC",
    "Genshin Impact" : "Genesis Crystal",
    "Roblox" : "Robux"
}

daftar_game = {
    1 : "Mobile Legends",
    2 : "Free Fire",
    3 : "PUBG",
    4 : "Genshin Impact",
    5 : "Roblox",
}

akun_player = {}
transaksi = {}
nomor_transaksi = 1

def hitung_total(harga, jumlah):
    total_harga = int(harga) * int(jumlah)
    return total_harga

def hitung_item(item, jumlah):
    total_item = int(item) * int(jumlah)
    return total_item

def ambil_nomor_transaksi():
    global nomor_transaksi

    nomor_baru = nomor_transaksi
    nomor_transaksi += 1

    return nomor_baru

def jumlah_semua_paket():
    jumlah_paket = 0

    for paket_game in katalog.values():
        jumlah_paket += len(paket_game)

    return jumlah_paket

def tampilkan_header ():
    print("===============================")
    print("         TOP UP STORE          ")
    print("===============================")

def tampilkan_menu_utama():
    print("\n===== SISTEM TOP UP GAME =====")
    print("1. Login Admin / Sistem")
    print("2. Register Player")
    print("3. Login Pengguna")
    print("4. Logout")

os.system("cls" if os.name == "nt" else "clear")

tampilkan_header()

while True :
    tampilkan_menu_utama()
    role = input ("Pilih menu: ")
    
    if role == "1":

        os.system("cls") if os.name == "nt" else "clear"

        print("===== LOGIN SEBAGAI ADMIN =====")

        username = input ("username: ")
        password = input ("password: ")

        if username == "" or password == "":
            print("Error! Data tidak boleh kosong!")
            continue

        elif username != "salwa" or password != "65":
            print ("Error! username dan password salah!")
            continue

        else:
            print("Login berhasil!")

            while True:

                print("===== MENU ADMIN =====")
                print("1. Create - Tambah Paket")
                print("2. Read - Lihat Data")
                print("3. Update - Ubah Data")
                print("4. Delete - Hapus Paket")
                print("5. Kembali")

                menu = input ("Pilih menu: ")

                if menu == "1":
                    
                    while True:

                        print("\n===== CREATE PAKET =====")
                        print("0. Kembali ke Menu Admin")

                        for nomor, game in daftar_game.items():
                            print(nomor, ".", game)

                        pilih = input("Pilih game: ")

                        if pilih == "0":
                            break

                        elif not pilih.isdigit():
                            print("Error! Pilihan harus berupa angka!")

                        elif int(pilih) not in daftar_game:
                            print("Error! Game tidak tersedia!")

                        else:
                            game = daftar_game[int(pilih)]
                            
                            print("\nGame terpilih:", game)
                            print("Masukkan 0 untuk kembali.")

                            item = input("Jumlah item: ")

                            if item == "0":
                                continue

                            harga = input("Harga Paket: Rp")

                            if harga == "0":
                                continue

                            if not item.isdigit():
                                print("Error! Item harus berupa angka!")

                            elif not harga.isdigit():
                                print("Error! Harga harus berupa angka!")

                            elif int(item) <= 0 or int(harga) <= 0:
                                print("Error! Nilai harus lebih dari 0!")

                            elif int(item) in katalog[game]:
                                print("Error! Paket sudah tersedia!")

                            else:
                                item : int(item)
                                harga : int(harga)

                                katalog[game][item] = {
                                    "harga": harga,
                                    "status": "tersedia"
                                }                                    
                                
                                print("\nPaket berhasil ditambahkan!")
                                print("Game", game)
                                print("Item", item, mata_uang[game])
                                print("Harga", harga)
                                print("Status : tersedia")

                elif menu == "2":

                    print("\n===== KATALOG TOP UP =====")

                    print(
                        "Jumlah seluruh paket:",
                        jumlah_semua_paket()
                    )

                    for game, paket_game in katalog.items():

                        print("\nGame: ", game)

                        if len(paket_game) == 0:
                            print("Belum ada paket!")

                        else:
                            nomor = 1

                            for item, data in paket_game.items():

                                print(
                                    nomor, ".",
                                    item, mata_uang[game]
                                )

                                print("Harga: Rp", data["harga"])
                                print("Status: ", data["status"])

                                nomor+=1

                    print("\n===== DATA TRANSAKSI =====")

                    if len(transaksi) == 0:
                        print("Belum ada transaksi!")

                    else:
                        for nomor, data in transaksi.items():

                            print("\n-------------------------")
                            print("No Transaksi: ", nomor)
                            print("Username: ", data["username"])
                            print("ID Player: ", data["player"])
                            print("Game: ", data["game"])
                            print(
                                "Paket: ",
                                data["paket"],
                                data["satuan"]
                            )
                            print(
                                "Harga Satuan: Rp",
                                data["harga_satuan"]
                            )
                            print(
                                "Jumlah Paket: ",
                                data["jumlah_paket"]
                            )
                            print(
                                "Total Item: ",
                                data["item"],
                                data["satuan"]
                            )
                            print("Total Harga: Rp", data["total"])
                            print("Status: ", data["status"])

                elif menu == "3":

                    while True:

                        print("\n===== UPDATE DATA =====")
                        print("1. Ubah harga paket")
                        print("2. Ubah ketersediaan paket")
                        print("3. Ubah Status Transaksi")
                        print("0. Kembali ke menu admin")

                        pilih = input("Pilih menu: ")

                        if pilih == "0":
                            break

                        elif pilih == "1" or pilih == "2":

                            print("\n===== PILIH GAME =====")
                            print("0. Kembali")

                            for nomor, game in daftar_game.items():
                                print(nomor, ".", game)

                            pilih_game = input(
                                "Pilih game: "
                            )

                            if pilih_game == "0":
                                continue

                            elif not pilih_game.isdigit():
                                print("Error! Pilihan harus berupa angka!")
                                continue

                            elif int(pilih_game) not in daftar_game:
                                print("Error! Game tidak tersedia!")
                                continue

                            game_dipilih = daftar_game[int(pilih_game)]

                            paket_game = katalog[game_dipilih]

                            print(
                                "\n===== PAKET",
                                game_dipilih,
                                "====="
                            )

                            nomor = 1

                            for item, data in paket_game.items():

                                print(
                                    nomor, ".",
                                    item, mata_uang[game_dipilih],
                                    "- Rp", data["harga"],
                                    "-", data["status"]
                                )

                                nomor += 1

                            if len(paket_game) == 0:
                                print("Belum ada paket!")
                                continue

                            print("0. Kembali")

                            pilih_paket = input(
                                "Pilih nomor paket: "
                            )

                            if pilih_paket == "0":
                                continue

                            elif not pilih_paket.isdigit():
                                print("Error! Pilihan haus berupa angka!")
                                continue

                            elif not 1 <= int(pilih_paket) <= len(paket_game):
                                print("Error! Paket tidak ditemukan!")
                                continue

                            item = tuple(paket_game)[
                                int(pilih_paket) - 1
                            ]

                            if pilih == "1":

                                harga = input(
                                    "Masukkan harga baru: Rp"
                                )

                                if not harga.isdigit():
                                    print("Error! harga harus berupa angka!")

                                elif int(harga) <= 0:
                                    print("Error! Harga harus lebih dari nol!")

                                else:
                                    katalog[game_dipilih][item]["harga"] = int(harga)

                                    print("\nHarga berhasil diperbarui!")
                                    print("Harga baru: Rp", harga)

                            elif pilih == "2":

                                print("\n===== UBAH STATUS =====")
                                print("1. Tersedia")
                                print("2. Tidak tersedia")
                                print("0. Kembali")

                                status = input(
                                    "Pilih status: "
                                )

                                if status == "0":
                                    continue

                                elif status == "1":

                                    katalog[game_dipilih][item]["status"] = "tersedia"
                                        
                                    print("Status berhasil diperbarui!")
                                    print("Status: tersedia")

                                elif status == "2":

                                    katalog[game_dipilih][item]["status"] = "tidak tersedia"

                                    print("Status berhasil diperbarui!")
                                    print("Status: tidak tersedia")

                                else:
                                    print("Error! Status tidak valid!")

                        elif pilih == "3":

                            print("\n===== UPDATE TRANSAKSI =====")

                            if len(transaksi) == 0:
                                print("Belum ada transaksi!")
                                continue

                            for nomor, data in transaksi.items():

                                print(
                                    "No: ", nomor,
                                    "| Game: ", data["game"],
                                    "| Status: ", data["status"]
                                )

                            print("0. kembali")

                            cari = input(
                                "Masukkan nomor transaksi: "
                            )

                            if cari == "0":
                                continue

                            elif not cari.isdigit():
                                print("Error! Nomor harus berupa angka!")
                                continue

                            cari = int(cari)

                            print(
                                "\nStatus saat ini:",
                                transaksi[cari]["status"]
                            )

                            print("1. Menunggu")
                            print("2. Diproses")
                            print("3. Berhasil")
                            print("0. Kembali")

                            status = input(
                                "Pilih status baru: "
                            )

                            if status == "0":
                                continue

                            elif status == "1":
                                transaksi[cari]["status"] = "Menunggu"

                            elif status == "2":
                                transaksi[cari]["status"] = "Diproses"

                            elif status == "3":
                                transaksi[cari]["status"] = "Berhasil"

                            else:
                                print("Error! Pilihan tidak valid!")
                                continue

                            print("\nStatus transaksi berhasil diperbarui!")

                            print(
                                "Status baru: ",
                                transaksi[cari]["status"]
                            )

                        else:
                            print("Error! Menu tidak tersedia!")

                elif menu == "4":

                    while True:

                        print("\n===== DELETE PAKET =====")
                        print("0. Kembali ke menu admin")

                        for nomor, game in daftar_game.items():
                            print(nomor, ".", game)

                        pilih_game = input(
                            "Pilih game:"
                        )

                        if pilih_game == "0":
                            break

                        elif not pilih_game.isdigit():
                            print("Error! Pilihsn hsrus berupa angka!")

                        elif int(pilih_game) not in daftar_game:
                            print("Error! Game tidak tersedia!")
                            continue

                        game_dipilih = daftar_game[int(pilih_game)]

                        paket_game = katalog[game_dipilih]

                        print(
                            "\n===== PAKET",
                            game_dipilih,
                            "====="
                        )

                        nomor = 1

                        for item, data in paket_game.items():

                            print(
                                nomor, ".",
                                item, mata_uang[game_dipilih],
                                "- Rp", data["harga"],
                                "-", data["status"]
                            )

                            nomor += 1

                        if len(paket_game) == 0:
                            print("Belum ada paket!")
                            continue

                        print("0. Kembali")

                        pilih_paket = input(
                            "Pilih nomor paket: "
                        )
                        
                        if pilih_paket == "0":
                            continue

                        elif not pilih_paket.isdigit():
                            print("Error! Pilihan harus berupa angka!")

                        elif not 1 <= int(pilih_paket) <= len(paket_game):
                            print("Error! Paket tidak ditemukan!")
                            continue

                        item = tuple(paket_game)[
                            int(pilih_paket) - 1
                        ]

                        print(
                            "Paket dipilih: ",
                            item, mata_uang[game_dipilih]
                        )

                        yakin = input(
                            "Yakin ingin menghapus paket? (y/n): "
                        )

                        if yakin == "y":

                            del katalog[game_dipilih][item]

                            print("Paket berhasil dihapus!")

                        elif yakin == "n":
                            print("Penghapusan dibatalkan!")

                        else:
                            print("Error! Konfirmasi tidak valid!")

                elif menu == "5":
                    print("Logout Admin Berhasil!")
                    break

                else:
                    print("Error! Menu tidak tersedia!")

    elif role == "2":

        print("\n===== REGISTER PLAYER =====")

        username = input("Buat username: ")
        password = input("Buat password: ")
        konfirmasi = input("Konfirmasi password: ")

        if username == "" or password == "":
            print("Error! Data tidak boleh kosong!")

        elif username in akun_player:
            print("Error! Username sudah terdaftar!")

        elif len(password) < 6:
            print("Error! Password minimal terdiri dari 6 karakter!")

        elif password != konfirmasi:
            print("Error! Konfirmasi password tidak cocok!")

        else:
            akun_player[username] = password

            print("\nRegistrasi berhasil!")
            print("Username: ", username)
            print("Silahkan login untuk melakukan top up!")

    elif role == "3":

        print("\n===== LOGIN PLAYER =====")

        username = input("Username: ")
        password = input("Password: ")

        if username == "" or password == "":
            print("Error! Data tidak boleh kosong!")

        elif username not in akun_player:
            print("Error! Username belum terdaftar!")
            continue

        elif akun_player[username] != password:
            print("Error! Password salah!")
            continue

        else:
            print("Login Player berhasil!")

        while True:

            print("\n===== MENU PLAYER =====")
            print("1. Lihat Katalog")
            print("2. Top Up Game")
            print("3. Cek Status Pembayaran")
            print("4. Keluar")

            menu_player = input(
                "Pilih menu: "
            )

            if menu_player == "1":

                print("\n===== KATALOG TOP UP =====")

                for game, paket_game in katalog.items():

                    print("\n=====", game, "=====")

                    nomor = 1

                    for item, data in paket_game.items():

                        if data["status"] == "tersedia":

                            print(
                                nomor, ".",
                                item, mata_uang[game],
                                "- Rp", data["harga"]
                            )

                            nomor += 1

                    if nomor == 1:
                        print("Belum ada paket tersedia!")

            elif menu_player == "2":

                print ("\n===== PILIH GAME =====")

                for nomor, game in daftar_game.items():
                    print(nomor, ".", game)

                print("0. Kembali")

                pilih_game = input(
                    "Pilih game: "
                )

                if pilih_game == "0":
                    continue

                elif not pilih_game.isdigit():
                    print("Error! Pilihan harus berupa angka!")
                    continue

                elif int(pilih_game) not in daftar_game:
                    print("Error! Game tidak tersedia!")
                    continue
                
                game = daftar_game[int(pilih_game)]

                satuan = mata_uang[game]

                paket_tersedia = {}

                for item, data in katalog[game].items():

                    if data["status"] == "tersedia":
                        paket_tersedia[item] = data

                print("\n===== PAKET", game, "=====")

                nomor = 1

                for item, data in paket_tersedia.items():

                    print(
                        nomor, ".",
                        item, satuan,
                        "- Rp", data["harga"]
                    )

                    nomor += 1

                if len(paket_tersedia) == 0:
                    print("Belum ada paket tersedia!")
                    continue

                print("0. Kembali")

                pilih_paket = input(
                    "Pilih nomor paket: "
                )

                if pilih_paket == "0":
                    continue

                elif not pilih_paket.isdigit():
                    print("Error! Nomor paket harus berupa angka!")
                    continue

                elif not 1 <= int(pilih_paket) <= len(paket_tersedia):
                    print("Error! Paket tidak ditemukan!")
                    continue

                item = tuple(paket_tersedia)[
                    int(pilih_paket) - 1
                ]

                paket = paket_tersedia[item]

                print("\nPaket dipilih: ")
                print(item, satuan)
                print("Harga: Rp", paket["harga"])

                id_player = input(
                    "Masukkan ID Player: "
                )

                jumlah = input(
                    "Masukkan jumlah paket: "
                )

                if id_player == "":
                    print("Error! ID Player tidak boleh kosong!")

                elif not jumlah.isdigit():
                    print("Error! Jumlah harus berupa angka!")

                elif int(jumlah) <= 0:
                    print("Error! Jumlah harus lebih dari nol!")
                
                else:
                    jumlahn = int(jumlah)

                    total = hitung_total(
                        paket["harga"], jumlah
                    )

                    total_item = hitung_item(
                        item, jumlah
                    )

                    print("\n===== KONFIRMASI PESANAN =====")
                    print("Username: ", username)
                    print("Game: ", game)
                    print("ID Player: ", id_player)
                    print("Paket: ", item, satuan)
                    print("Harga Satuan: Rp", paket["harga"])
                    print("Jumlah Paket: ", jumlah)
                    print("Total Item: ", total_item, satuan)
                    print("Total Harga: Rp", total)

                    konfirmasi = input(
                        "Lanjutkan transaksi? (y/n): "
                    )

                    if konfirmasi == "y":

                        nomor_baru = ambil_nomor_transaksi()

                        transaksi[nomor_baru] = {
                            "username": username,
                            "player": id_player,
                            "game": game,
                            "paket": item,
                            "harga_satuan": paket["harga"],
                            "item": total_item,
                            "satuan": satuan,
                            "jumlah_paket": jumlah,
                            "total": total,
                            "status": "Menunggu"
                        }

                        print("\n===== STRUK TOP UP =====")
                        print("No Transaksi:", nomor_baru)
                        print("Username:", username)
                        print("Game:", game)
                        print("ID Player:", id_player)
                        print("Paket:", item, satuan)
                        print("Harga Satuan:", paket["harga"])
                        print("Jumlah Paket:", jumlah)
                        print("Total Item:", total_item, satuan)
                        print("Total Harga: Rp", total)
                        print("Status : Menunggu")
                        print("\nTransaksi berhasil dibuat!")

                    elif konfirmasi == "n":
                        print("Transaksi dibatalkan!")

                    else:
                        print("Error! Konfirmasi tidaak valid!")
                        print("Transaksi dibatalkan!")

            elif menu_player == "3":

                print("\n===== CEK STATUS TRANSAKSI =====")

                cari = input(
                    "Masukkan nomor transaksi: "
                )

                if not cari.isdigit():
                    print("Error! Nomor transaksi harus berupa angka!")

                elif int(cari) not in transaksi:
                    print("Error! Transaksi tidak ditemukan!")

                else:
                    cari = int(cari)
                    data = transaksi[cari]

                    if data["username"] != username:
                        print("Error! Transaksi bukan milik akun ini!")

                    else:
                        print("\n===== DETAIL TRANSAKSI =====")
                        print("No Transaksi:", cari)
                        print("Username:", data["username"])
                        print("Game:", data["game"])
                        print("ID Player:", data["player"])
                        print(
                            "Paket:",
                            data["paket"],
                            data["satuan"]
                        )
                        
                        print(
                            "Harga Satuan: Rp",
                            data["harga_satuan"]
                        )

                        print(
                            "Jumlah Paket:",
                            data["jumlah_paket"]
                        )

                        print(
                            "Total Item: ",
                            data["item"],
                            data["satuan"]
                        )

                        print("Total Harga: Rp", data["total"])
                        print("Status:", data["status"])

            elif menu_player == "4":
                print("Logout Player berhasil!")
                break

            else:
                print("Error! Pilihan menu tidak valid!")

    elif role == "4":

        print("\nTerimakasih telah menggunakan TOP UP STORE!")
        print("\nJangan lupa mampir lagi yaw~")
        break

    else:
        print("Error! Pilihan tidak tersedia!")