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
    """Fungsi untuk melihat hasil panen"""
    print(" ======== Nomor 1 ===========")
    [print( f"Lokasi {value['nama_lokasi']}\nHasil panen\nJagung {value['hasil_panen']['jagung']}\nPadi {value['hasil_panen']['padi']}\nKedelai {value['hasil_panen']['kedelai']} {'\n'} ") for value in data.values()]
    
    print("\n ======== Nomor 2 ===========")
    [print(f"Lokasi {value['nama_lokasi']}\nHasil panen\nJagung {value['hasil_panen']['jagung']}{'\n'*1} ")for key, value in data.items() if key == 'lokasi2' ]
    
    print("\n ======== Nomor 3 ===========")
    [print(f"Nama Lokasi dari {key} adalah {value['nama_lokasi']}\n")for key, value in data.items()if key == "lokasi3"]
    
    print(" ======== Nomor 4 ===========")
    rice_fields_sum = sum(val["hasil_panen"]["padi"] for val in data.values())
    soybean_fields_sum = sum(val["hasil_panen"]["kedelai"] for val in data.values())
    print(f"Hasil panen Padi : {rice_fields_sum} , Kedelai : {soybean_fields_sum}")
    
    print("\n ======== Nomor 5 ===========")
    dataVar = {val['nama_lokasi']: {'padi': val['hasil_panen']['padi'],'kedelai': val['hasil_panen']['kedelai'],'jagung': val['hasil_panen']['jagung']}for val in data.values()}
    [print(f"Lokasi {key}\nPadi:{val['padi']}\nKedelai:{val['kedelai']}\nJagung:{val['jagung']}\n ")  for key,val in dataVar.items()]

    print("\n\n\n ======== Nomor 6 ===========")
    [print(f"Lokasi {key} memerlukan perhatian khusus") if val['padi'] > 1300 or val['jagung'] > 800 else print(f"Lokasi {key} dalam kondisi baik ") for key, val in dataVar.items()]


harvest_list(data_panen)
