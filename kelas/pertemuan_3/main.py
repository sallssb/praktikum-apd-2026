cuaca = "hujan"

if cuaca == "hujan":
    print("bawa payung/jas hujan")
    print("telat dikit")

    print("otw ke kampus")


budget = 60000
cuaca = "hujan"

if budget > 30000 or cuaca =="cerah":
    print("beli yoshinoya")
else:
    print("masak indomie aja")

kendaraan = input("masukkan jenis kendaraan: ").lower().strip()

if kendaraan == "mobil":
    tarif_parkir = 10_000
elif kendaraan == "motor":
    tarif_parkir = 5_000
elif kendaraan == "sepeda":
    tarif_parkir = 6_700
else:
    tarif_parkir = 15_000

print("tarif parkir yang harus dibayar :", tarif_parkir)


bilangan = -5

status = "bilangan negatif" if bilangan < 0 else "bilangan positif"

print("bilangan adalah", status)


username = input("masukkan username")
password = input("masukkan password")

if username == "salwa":
    if password == "065":
        print("login berhasil")
    else:
        print("password salah")
else:
    print("username salah")

angka = 10/6
print(f"angka {angka:.02f}")