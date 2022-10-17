n = int(input("Masukkan N: "))
jumlah = 0
temp = int(input("Masukkan bilangan ke-1: "))
for i in range(2,n+1):
    cekTemp = True
    cekPrima = True
    angka = int(input(f"Masukkan bilangan ke-{i}: "))
    if(angka >= temp):
        for i in range(2, angka):
            if(angka%i== 0):
                cekPrima = False
        if((cekPrima == True) & (angka != 1)):
            angka *= 2
        jumlah += (angka - temp)
        if((cekPrima == True) & (angka != 1)):
            temp = (angka//2)
        else:
            temp = angka
    else:
        temp = angka
print(f"Total menaik sebesar {jumlah}.")