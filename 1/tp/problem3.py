print(f"Masukkan waktu mulai!")
jam1= int(input(f"Jam    : "))
menit1= int(input(f"Menit   : "))
detik1= int(input(f"Detik   : "))
print(f"Masukkan waktu selesai!")
jam2= int(input(f"Jam   : "))
menit2= int(input(f"Menit   : "))
detik2= int(input(f"Detik   : "))
totalDetik = (jam2*3600+menit2*60+detik2) - (jam1*3600+menit1*60+detik1)
if (totalDetik >=3600):
    print(f"Tuan Riz berlari selama {totalDetik//3600} jam {totalDetik//60%60} menit {totalDetik%60} detik.")
elif (totalDetik >=60) & (totalDetik < 3600):
    print(f"Tuan Riz berlari selama {totalDetik//60%60} menit {totalDetik%60} detik.")
else:
    print(f"Tuan Riz berlari selama {totalDetik%60} detik.")

