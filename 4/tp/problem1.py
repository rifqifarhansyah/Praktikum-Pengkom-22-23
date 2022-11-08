def maxTumpukan(tumpukan, baris, kolom):
    nilaiMax = -1
    for i in range(baris):
        if(tumpukan[i][kolom] > nilaiMax):
            nilaiMax = tumpukan[i][kolom]
    return nilaiMax

sesuai = True

tinggi = int(input("Masukkan tinggi tumpukan: "))
banyak = int(input("Masukkan banyak tumpukan: "))
A = [[0 for j in range(banyak)] for i in range(tinggi)]
for i in range(tinggi):
    for j in range(banyak):
        A[i][j] = int(input(f"Masukkan berat benda pad baris ke-{i+1} kolom ke-{j+1}: "))


for i in range(banyak):
    sesuai = True
    valMax = maxTumpukan(A, tinggi, i)
    if(valMax > A[tinggi-1][i]):
        sesuai = False

if(sesuai):
    print("Susunan tersebut memenuhi perintah Tuan Leo.")
else:
    print("Susunan tersebut tidak memenuhi perintah Tuan Leo.")
