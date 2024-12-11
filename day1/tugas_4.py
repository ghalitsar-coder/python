def menghitung_rata2(jml_mhs):
    total = 0;
    for i in range(jml_mhs):
        nilai_mhs = float(input(f"Masukkan nilai mahasiswa yang ke {i +1} : "))
        total += nilai_mhs
        
    return total/jml_mhs

jml = int(input("Masukkan jumlah mahasiswa "))
print(f"Hasil rata2 dari {jml} orang mahasiswa adalah {menghitung_rata2(jml)}")