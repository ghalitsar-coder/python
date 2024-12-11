
def patients_shelter(num_patient):
    arr = []
    current_patient = 1
    while num_patient > 0 :
        nama = input(f"Masukkan nama pasien ke {current_patient} : ")
        suhu= float(input("Masukkan suhu tubuh pasien : "))
        arr.append({"nama":nama, "suhu":suhu})
        num_patient -= 1
        current_patient += 1
    return arr


def patients_temp_calculation(patients):
    temperatures = [patient["suhu"] for patient in patients]
    return sum(temperatures) / len(temperatures)


def patients_conditional_calculation(patients):
    normal_patients = [patient for patient in patients if patient["suhu"] < 37.5]
    unormal_patients = [patient for patient in patients if  37.5 <= patient["suhu"] < 45 ]
    hyperpyrexia_patients = [patient for patient in patients if patient["suhu"] >= 45]
    
    return unormal_patients , hyperpyrexia_patients , normal_patients

num_patient = int(input("Masukkan jumlah pasien yang ingin diobati... : ")) 

patients = patients_shelter(num_patient)

average_temperature = patients_temp_calculation(patients)

unormal_patients, hyperpyrexia_patients, normal_patients = patients_conditional_calculation(patients)

print("normal patient",)

print("\nRata-rata suhu tubuh pasien adalah : ", average_temperature)

print("\nPasien yang normal : ", len(normal_patients))
for patient in normal_patients:
    print(f"Nama : {patient["nama"]} , Suhu  : {patient["suhu"]}")

print("\nPasien yang mengalami hyperpyrexia : ", len(hyperpyrexia_patients))
for patient in hyperpyrexia_patients:
    print(f"Nama : {patient["nama"]} , Suhu  : {patient["suhu"]}")

print("\nPasien yang mengalami tidak normal : ", len(unormal_patients))
for patient in unormal_patients:
    print(f"Nama : {patient["nama"]} , Suhu  : {patient["suhu"]}")
    
    

