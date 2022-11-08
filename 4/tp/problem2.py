def minArray(array, n):
    nilaiMin = 99999999999 
    for i in range(n):
        if((array[i] < nilaiMin) & (array[i] != 0)):
            nilaiMin = array[i]
    return nilaiMin

def cekNol(array, n):
    val = True
    for i in range(n):
        if(array[i] != 0):
            val =  False
    return val

n = int(input("Masukkan banyak nilai: "))
a = [0 for i in range(n)]
for i in range(n):
    a[i] = int(input(f"Masukkan nilai ke-{i+1}: "))
for i in range(n):
    if(i != n-1):
        print(f"{a[i]}", end=" ")
    else:
        print(f"{a[i]}", end="\n")
while(cekNol(a,n) == False):
    valMin = minArray(a, n)
    for i in range(n):
        if(a[i] != 0):
            a[i] -= valMin
    for i in range(n):
        if(i != n-1):
            print(f"{a[i]}", end=" ")
        else:
            print(f"{a[i]}", end="\n")