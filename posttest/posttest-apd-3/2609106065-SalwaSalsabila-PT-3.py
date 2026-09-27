nama = input ("masukkan nama: ")

nim = input ("masukkan nim: ")

list_misi = {
    "1" : "misi standar dengan bonus 2% dari reward dasar",
    "2" : "misi sulit dengan bonus 5% dari reward dasar",
    "3" : "misi kritis dengan bonus 8% dari reward dasar",
    "4" : "misi penyelamat bumi dengan bonus 12% dari reward dasar"
}

misi_1 = "1. misi standar dengan bonus 2% dari reward dasar"
misi_2 = "2. misi sulit dengan bonus 5% dari reward dasar"
misi_3 = "3. misi kritis dengan bonus 8% dari reward dasar"
misi_4 = "4. misi peyelamat bumi dengan bonus 12% dari reward dasar"

if nama == "salwa" and nim == "65":
    print("green latern corps mission")
    print(misi_1)
    print(misi_2)
    print(misi_3)
    print(misi_4)

elif nama != "salwa" and nim !="65":
    print("nama dan nim salah")
elif nama !="salwa":
    print("nama salah")
elif nim !="65":
    print("nim salah")

reward_dasar = 1000
misi = input("pilih misi: ")

if misi == "1":
    reward_bonus = reward_dasar*0.02
    print("misi yang yang dipilih :", list_misi["1"])
elif misi == "2":
    reward_bonus = reward_dasar*0.05
    print("misi yang dipilih :", list_misi["2"])
elif misi == "3":
    reward_bonus = reward_dasar*0.08
    print("misi yang dipilih :", list_misi["3"])
elif misi == "4":
    reward_bonus = reward_dasar*0.12
    print("misi yang anda pilih :", list_misi["4"])
else: 
    print("misi tidak tersedia")
    reward_bonus = 0
    
if misi in {"1","2","3","4"}:
    print("reward bonus :", reward_bonus) 
    reward_akhir = reward_dasar + reward_bonus
    print("reward akhir :", reward_akhir)

