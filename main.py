
def display_menu():
    print("\nMenu:")
    print("1. register")
    print("2. Login")
    print("3. hapus data")
    print("4. Keluar")


def register(username, password):
    open("dataBase.txt", "a").close()

    with open("dataBase.txt", "r") as file:
        for garis in file:
            if garis.strip():
                akun_terdaftar , password_terdaftar = garis.strip().split(",")
                if username == akun_terdaftar:
                    print("username sudah terdaftar")
                    return
                if password == password_terdaftar:
                    print("password sudah terdaftar")
                    return

    with open("dataBase.txt", "a") as file:
        file.write(username + "," + password + "\n")
        print("registrasi berhasil")


def Login():
    open("dataBase.txt", "a").close()
    username = input("masukkan username: ")
    password = input("masukkan password: ")

    with open("dataBase.txt", "r") as file:
        for garis in file:
            if garis.strip():
                akun_terdaftar, password_tertaftar = garis.strip().split(",")
                if username == akun_terdaftar and password == password_tertaftar:
                    print("login berhasil")
                    return
    print("login gagal, password atau username salah")

def hapus():
    with open("dataBase.txt", "w") as file:
        file.write("")
        print("data berhasil dihapus")
    
        

def main():
    while True:
        display_menu()
        choise = input("Pilih menu (1-4): ")

        if choise == '1':
            username = input("masukkan username: ")
            password = input("masukkan password: ")
            register(username, password)
            print()
        elif choise == '2':
            Login()
        elif choise == '3':
            hapus()
        elif choise == '4':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

main()