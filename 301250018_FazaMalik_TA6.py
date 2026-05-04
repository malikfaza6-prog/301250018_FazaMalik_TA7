# Nama Program : Bubble dan Insertion Sort
# Nama Pembuat: Faza Malik Al Hakim
# NIM : 301250018
# Tanggal Pembuatan : 05042026
# Nama file : 301250018_FazaMalik_TA6

data = [3, 5, 8, 12, 15, 18, 21, 25, 30, 34, 
        40, 45, 50, 55, 60, 65, 70, 75, 80, 85]


target = int(input("Masukkan data yang ingin dicari: "))


def hitung_bubble(data_input):
    arr = data_input.copy()
    n = len(arr)
    perbandingan = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            perbandingan += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped: break
    return perbandingan


def hitung_insertion(data_input):
    arr = data_input.copy()
    n = len(arr)
    perbandingan = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            perbandingan += 1
            if key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return perbandingan

def binary_search(data_list, target):
    kiri = 0
    kanan = len(data_list) - 1
    langkah = 0
    
    while kiri <= kanan:
        langkah += 1
        tengah = (kiri + kanan) // 2
        
        if data_list[tengah] == target:
            return tengah, langkah
        elif data_list[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
            
    return -1, langkah

hasil_cari, langkah_cari = binary_search(data, target)
comp_bubble = hitung_bubble(data)
comp_insertion = hitung_insertion(data)

print("\n" + "="*35)
print(f"HASIL ANALISIS ALGORITMA")
print("="*35)

if hasil_cari != -1:
    print(f"Status Pencarian      : Data {target} ditemukan di indeks {hasil_cari}")
else:
    print(f"Status Pencarian      : Data {target} TIDAK ditemukan")

print(f"Langkah Binary Search : {langkah_cari} kali")
print("-" * 35)
print(f"Perbandingan Sort (Jika data diproses ulang):")
print(f"- Bubble Sort         : {comp_bubble} kali")
print(f"- Insertion Sort      : {comp_insertion} kali")
print("="*35)