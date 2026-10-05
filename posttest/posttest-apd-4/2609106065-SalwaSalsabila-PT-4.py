print ("===============================")
print ("   Program Distribusi Makanan  ")
print ("===============================")

username = "salwa"
password = "65"

percobaan = 0
login_berhasil = False

while percobaan < 3:
    username = input("masukkan username:")
    password = input("masukkan password:")
    if username == "salwa" and password == "65":
        print("login berhasil")
        login_berhasil = True
        break

    elif username == "" and password == "":
        print("Username dan Password tidak boleh kosong")
        percobaan += 1
        continue

    elif username != "salwa" and password == "65":
        print("Username salah")
        percobaan += 1

    elif username == "salwa" and password != "65":
        print("Password salah")
        percobaan += 1

    else:
        print("username dan password salah")
        percobaan += 1
        print("sisa percobaan login:", 3 - percobaan)
        
if not login_berhasil:
    print("\nlogin gagal 3 kali")
    print("program dihentikan")

else:
    total_porsi = 0
    penerima_manfaat = 0
    paket_reguler = 0
    paket_anak = 0
    paket_keluarga = 0

    while True:
        print("\n================================")
        print("     Menu Distribusi Paket        ")
        print("================================")
        print("1. Paket Reguler, 1 porsi makanan")
        print("2. Paket Anak, 1 porsi makanan")
        print("3. Paket Keluarga, 4 porsi makanan")
        print("4. Keluar dari program")
        print("================================")

        pilihan_paket = input("masukkan pilihan paket (1-4): ")

        if pilihan_paket == "":
            print("input tidak boleh kosong")
            continue

        if not pilihan_paket.isdigit():
            print("input harus berupa angka")
            continue

        pilihan = int(pilihan_paket)

        if pilihan == 4:
            print("program dihentikan")
            break
        elif pilihan < 1 or pilihan > 4:
            print("\nPilihan tidak valid")
            continue

        while True:
            jumlah_paket = input("masukkan jumlah paket: ")

            if jumlah_paket == "":
                print("input tidak boleh kosong")
                continue

            if not jumlah_paket.isdigit():
                print("input harus berupa angka")
                continue

            jumlah_porsi = int(jumlah_paket)

            if jumlah_porsi <= 0:
                print("\njumlah paket harus lebih dari 1")
                continue
            break

        if pilihan == 3:
            porsi_makanan = 4
        
        else:
            porsi_makanan = 1

        for i in range(jumlah_porsi):
            total_porsi += porsi_makanan

        if pilihan == 1:
            paket_reguler += porsi_makanan
            penerima_manfaat += porsi_makanan * 1
            print(f"\nmenambah {porsi_makanan} paket reguler")
        elif pilihan == 2:
            paket_anak += porsi_makanan
            penerima_manfaat += porsi_makanan * 1
            print(f"\nmenambah {porsi_makanan} paket anak")
        elif pilihan == 3:
            paket_keluarga += porsi_makanan
            penerima_manfaat += porsi_makanan * 4
            print(f"\nmenambah {porsi_makanan} paket keluarga")
            
        if total_porsi >= 20:
            bonus = "5 paket buah"
        elif total_porsi >= 10:
            bonus = "3 botol susu"
        elif total_porsi >= 5:
            bonus = "1 paket vitamin"
        else:
            bonus = "tidak ada bonus"
            
        print("\n================================")
        print("     Hasil Distribusi Paket      ")
        print("================================")
        print(f"paket reguler:{paket_reguler} paket")
        print(f"paket anak:{paket_anak} paket")
        print(f"paket keluarga:{paket_keluarga} paket")
        print(f"Jumlah Paket: {jumlah_paket}")
        print(f"Total Porsi Distribusi: {total_porsi}")
        print(f"Jumlah Penerima Manfaat: {penerima_manfaat} orang")
        print(f"Bonus: {bonus}")
        print("================================")
