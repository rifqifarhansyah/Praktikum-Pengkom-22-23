bagianSusu = int(input("Masukkan bagian Susu: "))
bagianSirup = int(input("Masukkan bagian Sirup: "))
bagianEs = int(input("Masukkan bagian Es: "))
porsi = int(input("ml per porsi: "))
takaran = porsi//(bagianSusu+bagianSirup+bagianEs)
susu = int(input("Masukkan ml banyak Susu: "))
sirup = int(input("Masukkan ml banyak Sirup: "))
es = int(input("Masukkan ml banyak Es: "))
maksimum = susu//(takaran*bagianSusu)
if((sirup//(takaran*bagianSirup)) >= maksimum):
    maksimum = sirup//(takaran*bagianSirup)
elif((es//(takaran*bagianEs)) >= maksimum):
    maksimum = es//(takaran*bagianEs)
print(f"Tuan Kil dapat membuat {maksimum} porsi minuman.")
