data_panen = {
    "lokasi1": {
        "nama_lokasi": "Kebun A",
        "hasil_panen": {"padi": 1200, "jagung": 800, "kedelai": 500},
    },
    "lokasi2": {
        "nama_lokasi": "Kebun B",
        "hasil_panen": {"padi": 1500, "jagung": 900, "kedelai": 450},
    },
    "lokasi3": {
        "nama_lokasi": "Kebun C",
        "hasil_panen": {"padi": 1100, "jagung": 750, "kedelai": 600},
    },
    "lokasi4": {
        "nama_lokasi": "Kebun D",
        "hasil_panen": {"padi": 1300, "jagung": 850, "kedelai": 550},
    },
    "lokasi5": {
        "nama_lokasi": "Kebun E",
        "hasil_panen": {"padi": 1400, "jagung": 950, "kedelai": 480},
    },
}


def harvest_list(data):
    print("Nomor 1")
    [
        print(
            f"Lokasi {value['nama_lokasi']} Hasil panen\nJagung {value['hasil_panen']['jagung']}\nPadi {value['hasil_panen']['padi']}\nKedelai {value['hasil_panen']['kedelai']} {'\n'} "
        )
        for value in data.values()
    ]
    print("\nNomor 2")
    
    [
        print(
            f"Lokasi {value['nama_lokasi']} Hasil panen\nJagung {value['hasil_panen']['jagung']}{'\n'*2} "
        )
        for value in data.values()
    ]
    print("\nNomor 3")
    
    [
        print(f"Nama Lokasi dari {key} adalah {value['nama_lokasi']} \n\n")
        for key, value in data.items()
        if key == "lokasi3"
    ]
    print("Nomor 4")
    
    rice_fields_sum = sum(val["hasil_panen"]["padi"] for val in data.values())
    soybean_fields_sum = sum(val["hasil_panen"]["kedelai"] for val in data.values())
    print(f"Hasil panen Padi : {rice_fields_sum} , Kedelai : {soybean_fields_sum}")
    
    print("\nNomor 5")
    dataVar = [{key:{'padi':val['hasil_panen']['padi'],'kedelai':val['hasil_panen']['kedelai']}}  for key, val in data.items()]
    print(f"Variable Baru {dataVar}")

    print("\n\nNomor 6")
    [print(f"Lokasi {val['nama_lokasi']} memerlukan perhatian khusus") if val['hasil_panen']['padi'] > 1300 or val['hasil_panen']['jagung'] > 800 else print(f"Lokasi {val['nama_lokasi']} dalam kondisi baik ") for key, val in data.items()]


harvest_list(data_panen)