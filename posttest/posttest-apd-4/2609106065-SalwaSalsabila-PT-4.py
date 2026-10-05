print ("===============================")
print ("Program Distribusi Makanan")
print ("===============================")

username = "salwa"
password = "65"

percobaan = 0
login = False

while percobaan < 3:
    username = input("masukkan username:")
    password = input("masukkann password:")

    if username == "" or password == "":
        print("username dan password tidak boleh kosong!")
        percobaan += 1
        