import os
from colorama import Fore, init

import data
import admin
import player

from fungsi import (
    tampilkan_header,
    tampilkan_menu_utama
)

init(autoreset=True)

username_admin = "salwa"
password_admin = "65"

def bersihkan_terminal():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    
    tampilkan_header()
    tampilkan_menu_utama()

    menu = input("\nPilih menu: ")

    if menu == "1":

        print("\n===== Login Admin =====")

        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username == username_admin and password == password_admin:

            print(Fore.GREEN + "\nLogin berhasil!")
            
            admin.menu_admin()

        else:
            print(Fore.RED + "\nUsername atau password salah!")

    elif menu == "2":
        
        player.register_player()

    elif menu == "3":

        username = player.login_player()

        if username is not None:
            player.menu_player(username)

    elif menu == "4":
        
        print(
            Fore.CYAN + "\nTerima kasih telah menggunakan TOP UP STORE!"
        )

        break

    else:
        print(Fore.RED + "\nMenu tidak valid. Silakan pilih menu yang tersedia.")
        