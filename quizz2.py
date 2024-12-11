def save_patients(n):
    alls = {"names": [], "kgdp": [], "kgdm": []}
    for i in range(n):
        name = input(f"Masukkan nama pasien ke {i+1}: ")
        kgdp = float(input(f"Masukkan kgdp pasien ke {i+1}: "))
        kgdm = float(input(f"Masukkan kgdm pasien ke {i+1}: "))
        alls["names"].append(name)
        alls["kgdp"].append(kgdp)
        alls["kgdm"].append(kgdm)

    avgKgdp = sum(alls["kgdp"]) / n
    avgKgdm = sum(alls["kgdm"]) / n
    print(f"AVG dari KGDP : {avgKgdp}")
    print(f"AVG dari KGDM : {avgKgdm}")
    overPatient = [
        {"name": alls["names"][i], "kgdm": alls["kgdm"][i], "kgdp": alls["kgdp"][i]}
        for i in range(n)
        if alls["kgdp"][i] > 100 or alls["kgdm"][i] > 140
    ]
    normalPatient = [
        {"name": alls["names"][i], "kgdm": alls["kgdm"][i], "kgdp": alls["kgdp"][i]}
        for i in range(n)
        if alls["kgdp"][i] < 100 or alls["kgdm"][i] < 140
    ]
    for item in overPatient:
        print(f"Nama pasien kelebihan gula : {item['name']}, KGDP : {item['kgdp']}, KGDM : {item['kgdm']}")
    for item in normalPatient:
        print(f"Nama normal pasien: {item['name']}, KGDP : {item['kgdp']}, KGDM : {item['kgdm']}")
    # for i in range(n):
    #     if alls["kgdp"][i] > 100 or alls["kgdm"][i] > 140:
    #         print(
    #             f"Pasien {alls['names'][i]} memiliki kgdp = {alls['kgdp'][i]}  dan kgdm = {alls['kgdm'][i]} yang lebih besar dari 100 dan 140, masing-masing."
    #         )

jml_pasien = int(input("Masukkan jumlah pasien yang akan diperiksa : "))
save_patients(jml_pasien)
