muncul = 0
# coba = 0
sama = True
panjang1 = int(input(f"Masukkan panjang string 1: "))
array1 = [0 for i in range(panjang1)]
array1 = str(input(f"Masukkan string 1: "))
panjang2 = int(input(f"Masukkan panjang string 2: "))
array2 = [0 for i in range(panjang2)]
array2 = str(input(f"Masukkan string 2: "))
for i in range(0, (panjang2-panjang1)+1):
    sama = True
    j = i
    for a in range(0, panjang1):
        if(array1[a] != array2[j]):
            sama = False
        j += 1
    if(sama == True):
        print(f"{muncul}")
        muncul += 1
print(f"String 1 muncul sebanyak {muncul} kali.")