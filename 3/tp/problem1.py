awal = [0 for i in range(100)]
diskon = [0 for i in range(100)]
akhir = [0 for i in range(100)]
n = int(input("Masukkan banyak barang: "))
for i in range(n):
    awal[i] = int(input(f"Masukkan harga awal barang ke-{i+1}: "))
for i in range(n):
    diskon[i] = int(input(f"Masukkan besar diskon (dalam persen) barang ke-{i+1}: "))
for i in range(n):
    akhir[i] = (diskon[i]/100) * awal[i]
diskonMax = akhir[n]
imax = n
for i in range(n-1, -1, -1):
    if (akhir[i] >= diskonMax):
        diskonMax = akhir[i]
        imax = i
print(f"Barang {imax+1} memiliki diskon paling besar yaitu {diskonMax:.0f}.")