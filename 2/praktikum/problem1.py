catatan = int(input("Masukkan banyaknya catatan: "))
temp = 0
total = 0
for i in range(1,catatan+1):
    v = int(input(f"Masukkan kecepatan ke-{i}: "))
    t = int(input(f"Masukkan batas waktu ke-{i}: "))
    if(i == 1):
        temp = t
        total += (v*temp)
    elif(i !=1):
        temp = t - temp
        total += (v*temp)
        temp = t
print(f"Kota Peng dan Kota Kom berjarak {total} Km.")