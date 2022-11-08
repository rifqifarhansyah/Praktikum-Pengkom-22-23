nim = int(input(f"Masukkan akhiran NIM: "))

if (nim%2==0):
    cek = "genap"
else:
    cek = "ganjil"

if (nim>=1) & (nim<=100):
    if(cek == "ganjil"):
        kelas = "K1"
    else:
        kelas = "K2"
elif (nim>=101) & (nim<=200):
    if(cek == "ganjil"):
        kelas = "K3"
    else:
        kelas = "K4"
elif (nim>=201) & (nim<=300):
    if(cek == "ganjil"):
        kelas = "K5"
    else:
        kelas = "K6"
else:
    if(cek == "ganjil"):
        kelas = "K7"
    else:
        kelas = "K8"
print(f"Mahasiswa masuk ke ke kelas {kelas}.")