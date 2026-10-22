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

while True: 


    print ("\n===== SISTEM TOP UP GAME =====")

    print ("1. Login Admin / Sistem")
    print ("2. Register Player")
    print ("3. Login Player")
    print ("4. Logout")

    role = input("Pilih menu: ")

    #===============
    #     ADMIN
    #===============

    if role == "1":

        os.system("cls" if os.name == "nt" else "clear")

        print ("\n===== LOGIN ADMIN =====")

        username = input ("Username: ")
        password = input ("Password: ")

        if username == "" and password == "":
            print("Error! Data tidak boleh kosong!")
            continue

        elif username != "salwa" or password != "65":
            print ("Error! Username atau password salah!")
            continue

        else : 
            print ("Login Berhasil!")

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

                    for nomor, game in daftar_game.items():
                        print (nomor, ".", game)
                        
                    pilih = input("Pilih game: ")

                    if not pilih.isdigit() :
                        print ("Error! Pilihan harus berupa angka!")

                    elif int(pilih) not in daftar_game :
                        print ("Error! Game tidak terrsedia!")

                    else :
                        game = daftar_game[int(pilih)]

                        item = input ("Jumlah item: ")
                        harga = input ("Harga paket : Rp")

                        if not item.isdigit():
                            print ("Error! Item harus berupa angka!")

                        elif not harga.isdigit():
                            print ("Error! Harga harus berupa angka!")

                        elif int(item) <= 0 or int(harga) <= 0:
                            print ("Error! nilai harus lebih dari nol!")

                        elif int(item) in katalog [game]:
                            print ("Error! Paket sudah tersedia!")

                        else :
                            item = int(item)
                            harga = int (harga)

                            katalog [game] [item] = {
                                "harga": harga,
                                "status": "Tersedia"
                            }                              

                            
                            print ("Paket berhasil ditambahkan!")
                            print ("Game:", game)
                            print ("Item:", item, mata_uang [game])
                            print ("Harga: Rp", harga)



                elif menu == "2":

                    print ("\n===== KATALOG TOP UP=====")

                    for game, paket_game in katalog.items ():

                        print ("\ngame: ", game)
                        

                        if len(paket_game) == 0:
                            print ("Belum ada paket.")

                        else :
                            nomor = 1

                            for item, data in paket_game.items():

                                print (
                                    nomor, ".",
                                    item, mata_uang[game]
                                )
                                print("Harga: Rp", data ["harga"])
                                print("Status:", data["status"])

                                nomor +=1

                    print("\n===== DATA TRANSAKSI =====")

                    if len(transaksi) == 0:
                        print ("Belum ada transaksi.")
                    else: 
                        for nomor, data in transaksi.items():
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

                    for nomor, game in daftar_game.items():
                        print(nomor, ".", game)

                    pilih = input ("Pilih menu: ")

                    if pilih == "1" or pilih == "2":

                        print ("\n===== PILIH GAME =====")

                        pilih_game = input ("Pilih game (1-5):")

                        if pilih_game == "1":
                            game_dipilih = "Mobile Legends"

                        elif pilih_game == "2":
                            game_dipilih = "Free Fire"

                        elif pilih_game == "3":
                            game_dipilih = "PUBG"

                        elif pilih_game == "4":
                            game_dipilih = "Genshin Impact"

                        elif pilih_game == "5":
                            game_dipilih = "Roblox"

                        else:
                            game_dipilih = ""

                        if game_dipilih == "":
                            print("Error! Game tidak tersedia!")


                        if not pilih.isdigit():
                            print("Error! Pilihan harus berupa angka!")

                        elif int(pilih) not in daftar_game:
                            print ("Error! game tidak tersedia!")

                        else:
                            game = daftar_game[int(pilih)]

                            print("Game terpilih: ", game_dipilih)
                            paket_game = katalog[game_dipilih]

                            print ("\n===== DAFTAR PAKET", game_dipilih, "=====")

                            nomor = 1

                            for item, data in paket_game.items():

                                print (
                                    nomor, ".",
                                    item, mata_uang[game_dipilih],
                                    "- Rp", data ["harga"],
                                    "-", data ["status"]
                                )

                                nomor += 1

                            if len(paket_game) == 0:
                                print("Paket game belum tersedia!")

                            else:
                                pilih_paket = input (
                                    "\Pilih nomor paket: "
                                )   

                                if not pilih_paket.isdigit():
                                    print ("Error! Harus memasukkan angka! ")

                                elif not 1 <= int(pilih_paket) <= len (paket_game):
                                    print ("Error! Paket tidak ditemukan!")

                                else:
                                    item = tuple(paket_game) [int(pilih_paket) -1]

                                    if pilih == "1":
                                        harga = input (
                                            "Masukkan harga baru: Rp"
                                        )

                                        if not harga.isdigit():
                                            print("Error! Harga harus berupa angka!")

                                        elif int(harga) <= 0:
                                            print ("Error! Harga harus lebih dari 0!")

                                        else:
                                            katalog[game_dipilih][item]["harga"] = int(harga)

                                            print ("Harga berhasil diperbarui!")

                                    elif pilih == "2":

                                        print("\n1. Tersedia")
                                        print("2. Tidak tersedia")

                                        status = input(
                                            "Pilih status: "
                                        )

                                        if status == 1 :
                                            katalog[game_dipilih][item]["status"] = "Tersedia"

                                        elif status == "2":
                                            katalog[game_dipilih][item]["status"] = "Tidak tersedia"

                                        else:
                                            print ("Error! pilihan tidak valid!")

                    elif pilih == "3":
                        
                        print ("\n===== UPDATE TRANSAKSI =====")
                        
                        if len(transaksi) == 0:
                            print("Belum ada transaksi!")

                        else:
                            for nomor, data in transaksi.items():
                                print(
                                    "No: ", nomor,
                                    "| Game: ", data ["game"],
                                    "| Status: ", data ["status"]
                                )

                            cari == input (
                                "\nMasukkan nomor transaksi: "
                            )

                            if not cari.isdigit():
                                print("Error! Nomor harus berupa angka!")

                            elif int(cari) not in transaksi:
                                print("Error! Transaksi tidak ditemukan!")

                            else:
                                cari = int(cari)

                                print("1. Menunggu")
                                print("2. Diproses")
                                print("3. Berhasil")

                                status = input("Pilih status baru: ")

                                if status == "1":
                                    transaksi[cari]["status"] = "Menunggu"
                                    print("Status berhasil diperbarui!")

                                elif status == "2":
                                    transaksi[cari]["status"] = "Diproses"
                                    print("Status berhasil diperbarui!")

                                elif status == "3":
                                    transaksi [cari]["status"] = "Berhasil"
                                    print("Status berhasil diperbarui!")

                                else:
                                    print("Pilihan tidak valid!")
                                    break

                    else :
                        print ("Error! Pilihan tidak tersedia!")

                elif menu == "4":
                    print("\n===== HAPUS PAKET ======")

                    for nomor, game in daftar_game.items():
                        print(nomor, ".", game)

                    pilih_game = input("Pilih game: ")

                    if pilih_game == "1":
                        game_dipilih = "Mobile Legends"

                    elif pilih_game == "2":
                        game_dipilih = "Free Fire"

                    elif pilih_game == "3":
                        game_dipilih = "PUBG"

                    elif pilih_game == "4":
                        game_dipilih = "Genshin Impact"

                    elif pilih_game == "5":
                        game_dipilih = "Roblox"

                    else:
                        game_dipilih = ""

                    if game_dipilih == "":
                        print("Error! Game tidak tersedia!")
                    
                    if not pilih_game.isdigit():
                        print("Error! Nomor harus berupa angka!")

                    elif int(pilih_game) not in daftar_game:
                        print("Error! Game tidak tersedia!")

                    else:
                        game = daftar_game[int(pilih_game)]

                        print("Game terpilih: ", game_dipilih)
                        paket_game = katalog[game_dipilih]

                        print ("\n===== DAFTAR GAME", game_dipilih, "=====")

                        nomor = 1

                        for item, data in paket_game.items():

                            print(
                                nomor, ".",
                                item, mata_uang[game_dipilih],
                                "- Rp", data["harga"]
                            )

                            nomor += 1

                        if len(paket_game) == 0:
                            print("Paket belum tersedia!")

                        else:
                            pilih_paket = input (
                                "\Pilih nomor paket: "
                            )

                            if not pilih_paket.isdigit():
                                print("Error! Nomor harus berupa angka!")

                            elif not 1 <= int(pilih_paket) <= len(paket_game):
                                print("Error! Paket tidak ditemukan!")

                            else:
                                item = tuple(paket_game) [int(pilih_paket) -1]

                                yakin = input (
                                    "Yakin ingin menghapus paket? (y/n) : "
                                )

                                if yakin == "y":

                                    del katalog[game_dipilih][item]

                                    print("Paket berhasil dihapus!")

                                elif yakin == "n":
                                    print ("Penghapusan dibatalkan!")

                                else:
                                    print("Error! Konfirmasi tidak valid!")

                elif menu == "5":
                    print("Logout berhasil!")
                    break
                else:
                    print("Menu tidak tersedia!")

#================
#     PLAYER
#================

    elif role == "2":

        print("===== REGISTER PLAYER =====")
        
        username = input ("Buat username: ")
        password = input ("Buat password: ")
        konfirmasi = input ("Konfirmasi password: ")

        if username == "" or "" :
            print ("Error! Username dan password tidak boleh kosong!")

        elif username in akun_player :
            print ("Error! Username sudah terdaftar!")

        elif len(password) < 6 :
            print ("Error! Password minimal 6 karakter")

        elif password != konfirmasi :
            print ("Error! Konfirmasi password tidak cocok!")

        else:

            akun_player[username] = password

            print ("\nRegistrasi berhasil!")
            print ("Username: ", username)
            print ("Silahkan login untuk melakukan top up: ")

    elif role == "3":

        print ("===== LOGIN PLAYER =====")

        username = input ("Username: ")
        password = input ("Password: ")

        if username == "" or password == "" :
            print ("Error! Data tidak boleh kosong!")
            continue

        elif username not in akun_player:
            print ("Error! Username belum terdaftar!")
            continue

        elif akun_player[username] != password:
            print ("Error! Password salah!")
            continue

        else:
            print("Login berhasil!")

        while True:

            print("\n===== MENU PLAYER =====")

            print("1. Lihat katalog")
            print("2. Top up game")
            print("3. Cek status transaksi")
            print("4. Kembali")

            menu_player = input("Pilih menu: ")

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
                print("\n===== PILIH GAME =====")

                for nomor, game in daftar_game.items():
                    print(nomor, ".", game)

                pilih_game = input("Pilih game (1-5): ")

                if not pilih_game.isdigit():
                    print("Error! Pilihan harus berupa angka!")

                elif int(pilih_game) not in daftar_game:
                    print("Error! Game tidak tersedia!")

                else:
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
                        print("Maaf, belum ada paket tersedia!")

                    else:
                        pilih_paket = input(
                            "\nPilih nomor paket: "
                        )

                        if not pilih_paket.isdigit():
                            print("Error! Nomor paket harus angka!")

                        elif not 1 <= int(pilih_paket) <= len(paket_tersedia):
                            print("Error! Paket tidak ditemukan!")

                        else:

                            item = tuple(paket_tersedia)[int(pilih_paket) - 1]

                            paket = paket_tersedia[item]

                            print("\nPaket dipilih:")
                            print(item, satuan)
                            print("Harga: Rp", paket["harga"])

                            id_player = input(
                                "\nMasukkan ID Player: "
                            )

                            jumlah = input(
                                "Masukkan jumlah paket: "
                            )

                            if id_player == "":
                                print("Error! ID Player tidak boleh kosong!")

                            elif not jumlah.isdigit():
                                print("Error! Jumlah paket harus angka!")

                            elif int(jumlah) <= 0:
                                print("Error! Jumlah harus lebih dari nol!")

                            else:
                                jumlah = int(jumlah)

                                total = paket["harga"] * jumlah
                                total_item = item * jumlah

                                print("\n===== KONFIRMASI PESANAN =====")
                                print("Game:", game)
                                print("ID Player:", id_player)
                                print("Paket:", item, satuan)
                                print("Jumlah Paket:", jumlah)
                                print("Total Item:", total_item, satuan)
                                print("Total Harga: Rp", total)

                                konfirmasi = input(
                                    "\nLanjutkan transaksi? (y/n): "
                                )

                                if konfirmasi == "y":

                                    transaksi[nomor_transaksi] = {
                                        "username": username,
                                        "player": id_player,
                                        "game": game,
                                        "item": total_item,
                                        "satuan": satuan,
                                        "jumlah_paket": jumlah,
                                        "total": total,
                                        "status": "Menunggu"
                                    }

                                    print("\n===== STRUK TOP UP =====")
                                    print("No Transaksi:", nomor_transaksi)
                                    print("Username:", username)
                                    print("Game:", game)
                                    print("ID Player:", id_player)
                                    print("Jumlah:", total_item, satuan)
                                    print("Total: Rp", total)
                                    print("Status: Menunggu")
                                    print("\nTransaksi berhasil dibuat!")

                                    nomor_transaksi += 1

                                elif konfirmasi == "n":
                                    print("Transaksi dibatalkan!")

                                else:
                                    print("Error! Konfirmasi tidak valid!")
                                    print("Transaksi tidak dibuat.")

            elif menu_player == "3":

                print("\n===== CEK STATUS TRANSAKSI =====")

                cari = input(
                    "Masukkan nomor transaksi: "
                )

                if not cari.isdigit():
                    print("Error! Nomor transaksi harus angka!")

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
                            "Jumlah:",
                            data["item"],
                            data["satuan"]
                        )

                        print("Total: Rp", data["total"])
                        print("Status:", data["status"])

            elif menu_player == "4":
                print("Logout player berhasil!")
                break

            else:
                print("Error! Pilihan menu tidak valid!")

    elif role == "4":
        print("Terima kasih!")
        break

    else:
        print("Pilihan tidak tersedia!")