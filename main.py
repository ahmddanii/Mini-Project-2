from prettytable import PrettyTable
import pwinput

users = [ 
    {"username" : "Atmind", "password" : "Atmien123#", "role" : "admin"}, 
    {"username" : "Galih Wirayudha", "password" : "galih123", "role" : "user"} ,
    {"username" : "Vina Mulyana", "password" : "vina123", "role" : "user"} ,
    {"username" : "Alfiansyah Hutomo", "password" : "alfi123", "role" : "user"} 
]

data_karyawan = [
    {"id" : 1, "nama" : "Alfiansyah Hutomo", "jabatan" : "CTO", "alamat" : "Scott Street, 8", "status" : "Jomblo"},
    {"id" : 2, "nama" : "Galih Wirayudha", "jabatan" : "IT Technician", "alamat" : "Jalan Sendawar", "status" : "Menikah"},
    {"id" : 3, "nama" : "Vina Mulyana", "jabatan" : "HRD", "alamat" : "Jalan Sambaliung", "status" : "Jomblo"}
]

def login():
    try :
        username = input("Masukkan username: ")
        password = pwinput.pwinput("Masukkan password: ")

        for user in users:
            if user["username"] == username and user["password"] == password:
                print(f"Login berhasil, Selamat datang {user["username"]}")
                return user["role"], user["username"]
        print("Login gagal!")
    except Exception as e :
        print(f"Terdapat error, kode: {e}")

def create_karyawan() :
    try : 
        new_id = len(data_karyawan) + 1
        name = input("Masukkan Nama Karyawan: ")
        position = input("Masukkan Posisi Karyawan: ")
        address = input("Masukkan Alamat Karyawan: ")
        status = input("Masukkan Status Karyawan: ")

        data_karyawan.append({"id" : new_id, "nama" : name, "jabatan" : position, "alamat" : address, "status" : status})
        print("Berhasil Menambahkan Karyawan-----")
    except Exception as e :
        print(f"Terdapat error, kode: {e}")

def read_karyawan() :
    try : 
        table = PrettyTable()
        table.field_names = ["ID", "Nama", "Jabatan", "Alamat", "Status"]

        for karyawan in data_karyawan : 
            table.add_row([karyawan["id"], karyawan["nama"], karyawan["jabatan"], karyawan["alamat"], karyawan["status"]])
        print(table)
    except Exception as e : 
        print(f"Terdapat error, kode: {e}")

def update_karyawan() :
    try : 
        karyawan_id = int(input("Silahkan masukkan id karyawan yang akan di ubah: "))
        karyawan = next((d for d in data_karyawan if d["id"] == karyawan_id), None)
    
        print(f"Data karyawan yang akan di edit: Nama : {karyawan["nama"]}, Jabatan : {karyawan["jabatan"]}, Alamat : {karyawan["alamat"]}, Status : {karyawan["status"]}")
        
        karyawan["nama"] = input(f"Nama baru ({karyawan["nama"]}) : ")
        karyawan["jabatan"] = input(f"Jabatan baru ({karyawan["jabatan"]}) : ")
        karyawan["alamat"] = input(f"Alamat baru ({karyawan["alamat"]}) : ")
        karyawan["status"] = input(f"Status baru ({karyawan["status"]}) : ")

        print("Berhasil memperbarui data karyawan!")
    except StopIteration:
        print("ID tidak tersedia!") 
    except ValueError:
        print("Silahkan masukkan id yang benar!")

def delete_karyawan() :
    try :
        karyawan_id = int(input("Silahkan masukkan id karyawan yang akan dihapus: "))
        karyawan = next((d for d in data_karyawan if d["id"] == karyawan_id), None)

        data_karyawan.remove(karyawan)
        print("Data karyawan berhasil dihapus!")
    except StopIteration:
        print("Data tidak ditemukan!")
    except ValueError :
        print("Silahkan masukkan id yang benar")
        
def view_karyawan(username) :
    try:
        karyawan = next((d for d in data_karyawan if d["nama"] == username), None)
    
        table = PrettyTable()
        table.field_names = ["ID", "Nama", "Jabatan", "Alamat", "Status"]
        table.add_row([karyawan["id"], karyawan["nama"], karyawan["jabatan"], karyawan["alamat"], karyawan["status"]])
        print(table)
    except StopIteration : 
        print("Data karyawan tidak ditemukan!")
    except Exception as e:
        print(f"Terdapat error, kode: {e}")

def edit_karyawan(username) :
    try :
        karyawan = next((d for d in data_karyawan if d["nama"] == username), None)
        print(f"Data karyawan yang akan diubah: Nama: {karyawan["nama"]}, Jabatan: {karyawan["jabatan"]}, Alamat: {karyawan["alamat"]}, Status: {karyawan["status"]}")
        
        karyawan["nama"] = input(f"Nama baru ({karyawan["nama"]}): ") or karyawan["nama"]
        karyawan["jabatan"] = input(f"Jabatan baru ({karyawan["jabatan"]}): ") or karyawan["jabatan"]
        karyawan["alamat"] = input(f"Alamat baru ({karyawan["alamat"]}): ") or karyawan["alamat"]
        karyawan["status"] = input(f"Status baru ({karyawan["status"]}): ") or karyawan["status"]

        print("Berhasil memperbarui data karyawan!")
    except StopIteration :
        print("Data karyawan tidak ditemukan!")


def admin_menu() :
    while True:
        try :
            table = PrettyTable()

            table.field_names = ["No", "Menu Admin"]

            table.add_row(["1", "Tambah Data Karyawan"])
            table.add_row(["2", "Lihat Data Karyawan"])
            table.add_row(["3", "Update Data Karyawan"])
            table.add_row(["4", "Hapus Data Karyawan"])
            table.add_row(["5", "Logout"])

            print(table)

            choice = input("Pilih menu: ")

            if choice == "1":
                create_karyawan()
            elif choice == "2":
                read_karyawan()
            elif choice == "3":
                update_karyawan()
            elif choice == "4":
                delete_karyawan()
            elif choice == "5":
                break
            else:
                print("Pilihan tidak tersedia!")
        except ValueError: 
            print("Silahkan masukkan angka!")

def user_menu(username) :
    while True:
        try :
            table = PrettyTable()

            table.field_names = ["No", "Menu Admin"]

            table.add_row(["1", "Lihat Data"])
            table.add_row(["2", "Edit Data"])
            table.add_row(["3", "Logout"])

            print(table)
            choice = input("Pilih menu: ")

            if choice == "1":
                view_karyawan(username)
            elif choice == "2":
                edit_karyawan(username)
            elif choice == "3":
                break
            else:
                print("Pilihan tidak tersedia!")
        except ValueError: 
            print("Silahkan masukkan angka!")

try :
    role, username = login()
    if role == 'admin':
        admin_menu()
    elif role == 'user':
        user_menu(username)
    else:
        print("Username atau password tidak ada!")
except TypeError as t:
    print(f"Terdapat error, kode : {t} ")
