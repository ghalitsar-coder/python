


num_pasient = int(input("Masukkan jumlah pasien : "))

def patients_shelter(num_pasient):
    arr_names = []
    arr_djs = []
    for i in range(num_pasient):
        name = input(f"Masukkan nama pasien ke {i+1}: ")
        dj = int(input(f"Masukkan  DJ pasien ke {i+1}: "))
        arr_names.append(name)
        arr_djs.append(dj)
    
    print(f"Rata rata detak jantung {sum(arr_djs) /len(arr_djs)}")
    
    for i in range(num_pasient):
        if arr_djs[i] > 120:
            print(f"Pasien yang memiliki detak jantung ke {i+1} bernama {arr_names[i]}")
    

patients_shelter(num_pasient)

