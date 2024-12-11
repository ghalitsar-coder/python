# i = 0
# total = 0
# while i < 10 and total < 50:
#     total += i
#     print(f"Perulangan ke {i}, total = {total}")
#     i += 1


# //* PART 2
# found = False
# i = 0
# while not found :
#     if  i == 7 :
#          found = True
#          print("akhirnya no 7 ketemu")
#     else :
#         i += 1
#         print(f"perulangan ke {i}")


# //* PART 3
# buahbuahan = ["apple","banana","cherry"]
# buahbuahan.insert(0,"mango")
# buahbuahan.append('durian')

# pilihan = buahbuahan[0], buahbuahan[1]
# print(f"ini adalah pilihan {pilihan}\n\n")
# buahbuahan.pop(0)

# buahbuahan[1] = 'blueberry'

# buahbuahan.remove('cherry')

# print(f"buahnya adalah : {buahbuahan}")

# //* PART 4
# buahbuahan =  {"apple","apple","banana","cherry"}

# buahbuahan.add("nanas")
# buahbuahan.remove("banana")

# print(f"buahnya adalah : {buahbuahan}")


# //* PART 5
# buahbuahan = ['apple','banana','cherry','manggo']

# for i  in range(3,-1,-1) :
#     print(f"index ke {i} buahnya adalah {buahbuahan[i]}")


# //* PART 6
nama = [1,'firdaus','diash','if']
nq = "diash"
ada = False

for i in range(0,4):
    print(f"perulangan ke {i}")
    if nama[i] == nq:
        ada= True
        break
    
if ada:
    print(f"{nq} ditemukan pada index ke {i}")
else :
    print(f"{nq} tidak ditemukan")