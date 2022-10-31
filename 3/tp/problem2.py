lampu = int(input("Masukkan banyak lampu: "))
arrayOfLamp = [0 for i in range(lampu)]
string = ''
# for i in range(lampu):
#     string += str(arrayOfLamp[i])
# print(f"{string}")
n = int(input("Masukkan berapa kali Tuan Kil menekan tombol: "))
for i in range(n):
    index = int(input(f"Tombol yang ditekan ke {i+1}: "))
    if(((index-1) != 0) & ((index-1) != (lampu-1))):
        for i in range(index-2, index+1):
            if(arrayOfLamp[i] == 0):
                arrayOfLamp[i] = 1
            else:
                arrayOfLamp[i] = 0
    else:
        if(index-1 == 0):
            if(arrayOfLamp[0] == 0):
                arrayOfLamp[0] = 1
            else:
                arrayOfLamp[0] = 0
            if(arrayOfLamp[1] == 0):
                arrayOfLamp[1] = 1
            else:
                arrayOfLamp[1] = 0
        else:
            if(arrayOfLamp[lampu-2] == 0):
                arrayOfLamp[lampu-2] = 1
            else:
                arrayOfLamp[lampu-2] = 0
            if(arrayOfLamp[lampu-1] == 0):
                arrayOfLamp[lampu-1] = 1
            else:
                arrayOfLamp[lampu-1] = 0
    string = ''
    for i in range(lampu):
        string += str(arrayOfLamp[i])
    print(f"{string}")
print(f"Keadaan akhir rangkaian lampu adalah {string}.")