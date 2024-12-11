# # #* percobaan - 1
# obj = {}

# obj = {"nama": "diash", "usia": 25, "kota": "Ujungberung"}


# # #* percobaan - 2

# obj['kelamin'] = 'laki-laki'
# # my_dict.add({'makan':'ayam'})
# kota = obj['kota']
# nama = obj['nama']
# usia = obj['usia']
# print(f"nama saya adalah {nama} , usia saya adalah {usia} , asal saya dari {kota}")


# # #* percobaan - 3

# obj['pekerjaan'] = 'Programmer'
# print(obj)

# obj['usia'] = 26
# print(obj)

# # #* percobaan - 4

# del obj['kelamin']
# print(obj)

# kota_yang_dihapus = obj.pop('kota')
# print(kota_yang_dihapus)
# print(obj)


# * percobaan - 5
obj1 = {
    "a": 1,
    "b": 2,
}
obj2 = {"b": 3, "c": 4}
obj1.update(obj2)
obj3 = {**obj1, **obj2, "e": 5, "f": 6}
print(obj3)

# * percobaan - 6
for value in obj3.values():
    print(value)
for key in obj3.keys():
    print(key)

for key, value in obj3.items():
    print(f"{key} - {value}")

# * percobaan - 7

people = {
    "person1": {"name": "diash", "gender": "male", "age": 25},
    "person2": {"name": "Alara", "gender": "male", "age": 29},
}

# * percobaan - 8
# person1_name = people["person1"]["name"]
# person1_age = people["person1"]["age"]
# person1_gender = people["person1"]["gender"]

# person2_name = people["person2"]["name"]
# person2_age = people["person2"]["age"]
# person2_gender = people["person2"]["gender"]
# print(
#     f"Person One: {person1_name} and {'his' if person1_gender =='male' else 'her'} age {person1_age}\Person - 2 : {person1_name} and {'his' if person2_gender =='male' else 'her'} age {person1_age}"
# )

# * percobaan - 9
for key, value in people.items():
    print(
        f"Id Orang: {key}\nNama: {value['name']}\nUmur: {value['age']}\nGender: {value['gender']}"
    )
