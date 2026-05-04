# Nama Program : Sistem Inventory Barang
# Nama Pembuat: Faza Malik Al Hakim
# NIM : 301250018
# Tanggal Pembuatan : 05042026
# Nama file : 301250018_FazaMalik_TA7

data_barang = []


def tambah_barang():
    nama = input("Nama barang: ")
    jenis = input("Jenis barang: ")
    stok = int(input("Stok awal: "))

    # cek apakah barang sudah ada
    for barang in data_barang:
        if barang['nama'].lower() == nama.lower():
            print("Barang sudah ada!\n")
            return

    data_barang.append({
        "nama": nama,
        "jenis": jenis,
        "stok": stok
    })

    print(" Barang berhasil ditambahkan!\n")


def tampilkan_barang():
    print("\n=== DATA BARANG ===")
    for i, barang in enumerate(data_barang):
        print(f"{i}. {barang['nama']} | {barang['jenis']} | Stok: {barang['stok']}")
    print()



def linear_search_barang(nama):
    langkah = 0
    for i in range(len(data_barang)):
        langkah += 1
        if data_barang[i]['nama'].lower() == nama.lower():
            return i, langkah
    return -1, langkah


def binary_search_barang(nama):
    data_sorted = sorted(data_barang, key=lambda x: x['nama'].lower())

    kiri = 0
    kanan = len(data_sorted) - 1
    langkah = 0

    while kiri <= kanan:
        langkah += 1
        tengah = (kiri + kanan) // 2

        if data_sorted[tengah]['nama'].lower() == nama.lower():
            return data_sorted[tengah], langkah
        elif data_sorted[tengah]['nama'].lower() < nama.lower():
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return None, langkah

def barang_keluar():
    tampilkan_barang()

    nama = input("Masukkan nama barang: ")
    jumlah = int(input("Jumlah keluar: "))

    index, _ = linear_search_barang(nama)

    if index == -1:
        print(" Barang tidak ditemukan!\n")
        return

    # VALIDASI
    if jumlah > data_barang[index]['stok']:
        print(" Stok Kurang!\n")
        return

    # PROSES
    data_barang[index]['stok'] -= jumlah
    print(f" Berhasil! Stok sekarang: {data_barang[index]['stok']}\n")



def cari_barang():
    nama = input("Masukkan nama barang: ")

    print("\n1. Linear Search")
    print("2. Binary Search")
    pilih = input("Pilih metode: ")

    if pilih == "1":
        index, langkah = linear_search_barang(nama)

        if index != -1:
            barang = data_barang[index]
            print(f"\nDitemukan: {barang}")
        else:
            print("\nBarang tidak ditemukan")

        print(f"Langkah Linear: {langkah}\n")

    elif pilih == "2":
        barang, langkah = binary_search_barang(nama)

        if barang:
            print(f"\nDitemukan: {barang}")
        else:
            print("\nBarang tidak ditemukan")

        print(f"Langkah Binary: {langkah}\n")

    else:
        print("Pilihan tidak valid!\n")



while True:
    print("=== MENU INVENTORY ===")
    print("1. Tambah Barang")
    print("2. Tampilkan Barang")
    print("3. Cari Barang (Linear vs Binary)")
    print("4. Barang Keluar")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2":
        tampilkan_barang()
    elif pilihan == "3":
        cari_barang()
    elif pilihan == "4":
        barang_keluar()
    elif pilihan == "5":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak valid!\n")