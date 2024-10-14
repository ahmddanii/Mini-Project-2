# Mini-Project-2
#### Nama  : Ahmad Dani
#### Kelas : B
#### NIM   : 2409116074

## Flowchart
![Sistem Pengelolaan Data Karyawan drawio (1)](https://github.com/user-attachments/assets/dd8d7f20-ec51-4a88-8310-141cc9fe8978)

## Penjelasan baris program
![baris atas](https://github.com/user-attachments/assets/4141d878-d5cb-4ac2-bfe6-6fd19103ea0b)
Melakukan import prettytable untuk membuat tabel yang rapi dan pwinput agar ketika menginputkan password, yang diinput menjadi bintang. Lalu membuat data user dan data karyawan awal

![def login](https://github.com/user-attachments/assets/dfe3b76f-6f33-498d-8f24-17f79f9a945e)
Membuat fungsi untuk login dan menggunakan library pwinput untuk input 

![create](https://github.com/user-attachments/assets/652d069b-1851-4384-a132-5c70e02245e5)
Membuat fungsi untuk menambah data karyawan, dengan menggunakan append

![def read](https://github.com/user-attachments/assets/0a772515-4464-452d-85a9-70ed4262783e)
Menampilkan data karyawan dengan menggunakan library prettytable, mengunakan looping for untuk menampilkan baris tabel

![def update](https://github.com/user-attachments/assets/96cdc91b-2029-4331-8ef9-e2d15168b0fd)
Mengupdate data dari karyawan dan mencari data yang ingin di edit dengan menggunakan next() untuk mencari id yang ada di dalam dictionary sampai ketemu id yang diinput

![def delete](https://github.com/user-attachments/assets/c6aeb6a4-a91a-4a69-b842-3f499f12a966)
Menghapus data karyawan, dan cara mencari id yang ingin dihapus sama seperti cara pada update

![edit karyawan](https://github.com/user-attachments/assets/a98a0cb3-f8ea-4010-8a0d-1efe4d6e7226)
Fungsi untuk mengedit data karyawan, menu ini akan tampil ketika user biasa login

![admin menu](https://github.com/user-attachments/assets/1d4c323f-2678-402e-8fe2-57e87f5a9af9)
Menu admin, menggunakan pengulangan while. jika menu 1 maka akan masuk ke fungsi tambah, menu 2 akan masuk ke fungsi melihat data, menu 3 untuk masuk ke fungsi update data, menu 4 masuk ke fungsi hapus data, dan menu 5 akan menghentikan programmnya

![user menu](https://github.com/user-attachments/assets/3ebaa296-f75b-4681-ac5d-edda067b48cc)
Menu user, menggunakan perulangan while. jika menu 1 maka akan masuk ke fungsi liat data sesuai user yang login, menu 2 akan masuk ke fungsi liat data sesuai user yang login, dan menu 3 akan menghentikan programmnya.

![terakhirr](https://github.com/user-attachments/assets/c9218f9a-26db-48a7-8dfc-0f2d8baf6477)
Menu utama dari program ini, yaitu menu login, jika role = admin maka akan masuk ke menu admin. dan sebaliknya

## Output Program
![image](https://github.com/user-attachments/assets/c27eb79d-3c12-4783-be6d-13fa8380f5e3)

Bagian menu untuk melakukan CRUD, disini ada menu create dan menu read

![image](https://github.com/user-attachments/assets/d975f5ab-defd-47b8-b21e-a2d2237ebb46)
dan ini adalah menu edit, menu delete, dan menu logout

![image](https://github.com/user-attachments/assets/ba83e4a3-5c9c-4547-9737-1595d9860c18)
Lalu berikutnya ada menu untuk karyawan, disini karyawan hanya bisa melihat datanya sendiri dan mengedit datanya sendiri. Akses untuk karyawan hanya lihat dan edit datanya sendiri



