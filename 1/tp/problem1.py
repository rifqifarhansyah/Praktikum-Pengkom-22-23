hargaA = int(input(f"Masukkan harga dasar barang A: "))
jualA = int(input(f"Masukkan harga jual barang A: "))
hargaB = int(input(f"Masukkan harga dasar barang B: "))
jualB = int(input(f"Masukkan harga jual barang B: "))
hargaC = int(input(f"Masukkan harga dasar barang C: "))
jualC = int(input(f"Masukkan harga jual barang C: "))
keuntunganA = jualA - hargaA
keuntunganB = jualB - hargaB
keuntunganC = jualC - hargaC
if (keuntunganA>=keuntunganB) & (keuntunganA>=keuntunganC):
    print(f"Barang yang harus ditawarkan adalah barang A.")
elif (keuntunganB>=keuntunganA) & (keuntunganB>=keuntunganC):
    print(f"Barang yang harus ditawarkan adalah barang B.")
else:
    print(f"Barang yang harus ditawarkan adalah barang C.")