from itertools import count


panjang = int(input("Masukkan panjang rantai DNA: "))
arrayOfRantai = [0 for i in range(panjang)]
arrayOfRantai = str(input("Masukkan rantai DNA: "))
arrayOfKodon = [0 for i in range(3)]
arrayOfKodon = str(input("Masukkan kodon yang dicari: "))
kodon = ''
for i in range(3):
    kodon += arrayOfKodon[i]
sama = True
countFind = 0
for i in range(0, panjang-3):
    sama = True
    j = i
    for a in range(0, 3):
        if(arrayOfRantai[j] != arrayOfKodon[a]):
            sama = False
        j += 1
    if(sama == True):
        countFind += 1
if(countFind > 0):
    print(f"Kodon {kodon} muncul sebanyak {countFind} kali.")
else:
    print(f"Kodon {kodon} tidak muncul pada rantai DNA.")
