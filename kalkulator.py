# === KALKULATOR SEDERHANA ===
# Kelompok J2R
# Reyna Maselina Manansal 250211060092
# Jesril Graciella Angela Mende 250211060017
# Jessica Marsha Sangki 250211060061

# Bagian Fungsi Operasi
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol!"
    return a / b
# Bagian Input User
def get_menu():
    print("=== Kalkulator Sederhana ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    return input("Pilih operasi (1/2/3/4): ")

def get_angka():
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    return angka1, angka2
# Bagian Utama Program
pilihan = get_menu()
angka1, angka2 = get_angka()

if pilihan == "1":
    print("Hasil:", tambah(angka1, angka2))

elif pilihan == "2":
    print("Hasil:", kurang(angka1, angka2))

elif pilihan == "3":
    print("Hasil:", kali(angka1, angka2))

elif pilihan == "4":
    print("Hasil:", bagi(angka1, angka2))

else:
    print("Pilihan tidak valid.")