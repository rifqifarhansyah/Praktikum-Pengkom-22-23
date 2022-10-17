n = int(input("Masukkan bilangan: "))
jumlah = 0
for i in range(1, n):
    if((n%i) == 0):
        jumlah += i
if(jumlah == n):
    print(f"Bilangan tersebut adalah bilangan sempurna.")
else:
    print(f"Bilangan tersebut bukan bilangan sempurna.")
