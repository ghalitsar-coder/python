name = input("Masukkan nama  ")
nilai = int(input("Masukkan nilai  "))
jurusan = input("Masukkan jurusan  ")

grade = ""

if 80 <= nilai <=100 :
    print("A")
    grade = "A"
elif 73 <= nilai <= 79:
    print("AB")
    grade = "AB"
elif 67 <= nilai <= 72:
    print("B")
    grade = "B"
    
elif 55 <= nilai <= 66:
    print("BC")
    grade = "BC"
    
elif 40 <= nilai <= 54:
    print("C")
    grade = "C"
 
else :
    print("F")
    grade = "F"
    
    
print(f"Nama {name}, memiliki nilai {nilai} dengan nilai akhir {grade} dengan jurusan {jurusan}")