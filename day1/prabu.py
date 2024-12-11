# Menampilkan menu operasi
print("Pilih Operasi:")
print("1. Tambah (+)")
print("2. Kurang (-)")
print("3. Kali (*)")
print("4. Bagi (/)")

# Input pilihan operasi
operasi = input("Masukkan simbol operasi (+, -, *, /): ")

# Input angka pertama dan kedua
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Kalkulasi langsung berdasarkan simbol operasi
if operasi == '+':
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")
elif operasi == '-':
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")
elif operasi == '*':
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil}")
elif operasi == '/':
    if angka2 == 0:
        print("Error! Tidak bisa membagi dengan nol.")
    else:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
else:
    print("Simbol operasi tidak valid!")
