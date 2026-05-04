# Nama Program : Linear dan Binary Search
# Nama Pembuat: Faza Malik Al Hakim
# NIM : 301250018
# Tanggal Pembuatan : 05042026
# Nama file : 301250018_FazaMalik_TA5
data = [3, 5, 8, 12, 15, 18, 21, 25, 30, 34,
        40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

target = int(input("Masukkan angka yang dicari: "))


# Linear Search

def linear_search(data, target):
    langkah = 0
    for i in range(len(data)):
        langkah += 1
        if data[i] == target:
            return i, langkah
    return -1, langkah


# Binary Search

def binary_search(data, target):
    kiri = 0
    kanan = len(data) - 1
    langkah = 0

    while kiri <= kanan:
        langkah += 1
        tengah = (kiri + kanan) // 2

        if data[tengah] == target:
            return tengah, langkah
        elif data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return -1, langkah


index_linear, langkah_linear = linear_search(data, target)
index_binary, langkah_binary = binary_search(data, target)


print("\n=== HASIL ===")

# Linear Search
if index_linear != -1:
    print(f"Linear Search: ditemukan di index {index_linear}")
else:
    print("Linear Search: tidak ditemukan")
print(f"Jumlah langkah Linear: {langkah_linear}")

# Binary Search
if index_binary != -1:
    print(f"Binary Search: ditemukan di index {index_binary}")
else:
    print("Binary Search: tidak ditemukan")
print(f"Jumlah langkah Binary: {langkah_binary}")