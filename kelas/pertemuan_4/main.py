for i in range(1, 10):
    print(i)

for i in range(1, 3):# Mengontrol baris dalam tabel perkalian 
    for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
        print(f'{i} x {j} = {i * j}')
    print('') #biar ada jarak tiap iterasi

jawab = "ya"
hitung = 0

while(jawab == "ya"):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")

print(f"Total Perulangan : {hitung}")

for i in range(10): #1, 2, 3, 4, 5, 6, 7, 8, 9
    if i == 5:
        break
    print(i)

for i in range(20):
    if i > 12 :
         print("perulangan ke", 1)

angka_benar = 7

while True:
    print("=== Game Tebak Angka ===")

    angka_input = int(input("Masukkan angka tebakan (1-10): "))
    
    if angka_benar == angka_input:
        print("Angka yang kamu masukkann benar")
        break
    else:
        print("Angka masih salah")

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

