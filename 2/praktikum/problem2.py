ganjil = 0
ganjil3 = False
jumlah = 0
while(ganjil3 == False):
    cekPrima = True
    n = int(input(f"Masukkan bilangan: "))
    for i in range(2,n):
        if(n%i == 0):
            cekPrima = False
            break
    if(n == 1):
        cekPrima = False
    if(cekPrima == True):
        jumlah += n
    if(n%2==1):
        ganjil += 1
    elif(n%2==0):
        ganjil = 0
    if(ganjil == 3):
        ganjil3 = True
print(f"Jumlah bilangan prima adalah {jumlah}.")
