def maxFinal(array, n):
    maxVal = 0
    for i in range(n):
        if(array[i] > maxVal):
            maxVal = array[i]
    return maxVal

n = int(input("Masukkan besar Kota Kompeng: "))
a = [[0 for j in range(n)] for i in range(n)]
b = [0 for i in range(2*n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(input(f"Masukkan tinggi bangunan baris {i+1} kolom {j+1}: "))
idxB = 0
for j in range(n):
    maxBawah = 0
    maxAtas = 0
    maxBawahVal = 0
    maxAtasVal = 0
    for i in range(n):
        if(a[i][j] >= maxAtasVal):
            maxAtasVal = a[i][j]
            maxAtas += a[i][j]
    for i in range(n-1,-1,-1):
        if(a[i][j] >= maxBawahVal):
            maxBawahVal = a[i][j]
            maxBawah += a[i][j]
    b[idxB] = maxAtas
    idxB+=1
    b[idxB] = maxBawah
    idxB+=1

maxFinalVal = maxFinal(b, 2*n)
print(f"Foto terbaik memiliki total tinggi: {maxFinalVal}") 
