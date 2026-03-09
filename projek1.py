# ==============================
# TOKO SEMBAKO MANAGER APP
# LOGIN + CRUD BARANG
# ==============================

username_benar = "admin"
password_benar = "123"
data_barang = []

def login():
    print("=== LOGIN SISTEM TOKO SEMBAKO ===")
    while True:
        user = input("Username: ")
        pw = input("Password: ")

        if user == username_benar and pw == password_benar:
            print("Login berhasil!\n")
            break
        else:
            print("Username atau password salah!\n")

def tambah_barang():
    nama = input("Nama barang: ")
    harga = input("Harga barang: ")
    stok = input("Jumlah stok: ")

    barang = {
        "nama": nama,
        "harga": harga,
        "stok": stok
    }

    data_barang.append(barang)
    print("Barang berhasil ditambahkan!")

def lihat_barang():
    if len(data_barang) == 0:
        print("Belum ada data barang.")
    else:
        print("\n=== DATA BARANG TOKO ===")
        for i, b in enumerate(data_barang, start=1):
            print(f"{i}. {b['nama']} | Harga: {b['harga']} | Stok: {b['stok']}")

def edit_barang():
    lihat_barang()

    if len(data_barang) > 0:
        nomor = int(input("Pilih nomor barang: ")) - 1

        if nomor < len(data_barang):
            nama = input("Nama barang baru: ")
            harga = input("Harga baru: ")
            stok = input("Stok baru: ")

            data_barang[nomor]["nama"] = nama
            data_barang[nomor]["harga"] = harga
            data_barang[nomor]["stok"] = stok

            print("Data barang berhasil diupdate!")

def hapus_barang():
    lihat_barang()

    if len(data_barang) > 0:
        nomor = int(input("Pilih nomor barang yang dihapus: ")) - 1

        if nomor < len(data_barang):
            data_barang.pop(nomor)
            print("Barang berhasil dihapus!")

def menu():
    while True:
        print("\n===== MENU TOKO SEMBAKO =====")
        print("1. Tambah Barang")
        print("2. Lihat Barang")
        print("3. Edit Barang")
        print("4. Hapus Barang")
        print("5. Logout / Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_barang()
        elif pilih == "2":
            lihat_barang()
        elif pilih == "3":
            edit_barang()
        elif pilih == "4":
            hapus_barang()
        elif pilih == "5":
            print("Logout berhasil.")
            break
        else:
            print("Menu tidak tersedia!")

# ---------- PROGRAM UTAMA ----------
login()
menu()
print("Program selesai.")