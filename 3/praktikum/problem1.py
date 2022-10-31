banyakData = int(input("Masukkan nilai banyak data: "))
data = [0 for i in range(banyakData)]
for i in range(banyakData):
    data[i] = int(input(f"Masukkan data ke-{i+1}: "))
nilai = int(input("Masukkan nilai yang dicari: "))
n = int(input("Masukkan nilai N: "))
countFind = 0
iFind = 0
iFindFinal = 0
for i in range(banyakData):
    if(data[i] == nilai):
        countFind += 1
        iFind = i
    if(countFind == n):
        iFindFinal = iFind
print(f"Nilai {nilai} ke-{n} berada pada indeks {iFindFinal}.")