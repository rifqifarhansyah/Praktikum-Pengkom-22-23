n =  int(input("Masukkan N: "))
m = int(input("Masukkan M: "))
a = [[0 for j in range(m)] for i in range(n)]
x = 1
for i in range(n):
    if(i%2==0):
        for j in range(m):
            a[i][j] = x
            x += 1
    else:
        for j in range(m-1,-1,-1):
            a[i][j] = x
            x += 1
aFind = int(input("Masukkan A: "))
bFind = int(input("Masukkan B: "))
print(f"Nilai elemen tersebut adalah {a[aFind-1][bFind-1]}")
            