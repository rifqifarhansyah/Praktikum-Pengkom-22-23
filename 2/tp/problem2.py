i = 2
jumlah = 0
sudah = 0
sudah3 = False
temp = int(input(f"Angka ke-1: "))
while(sudah3 == False):
    n = int(input(f"Angka ke-{i}: "))
    if(n > temp):
        sudah  = 0
        temp = n
        jumlah += n
    elif(n <= temp):
        sudah += 1
        temp = n
    if(sudah  == 3):
        sudah3 = True
print(f"Jumlah nilai yang membesar adalah {jumlah}.")