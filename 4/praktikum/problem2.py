def prima(x):
    isPrima = True
    for i in range(2,x):
        if(x%i==0):
            isPrima = False
    return isPrima

a = int(input("Masukkan nilai A: "))
b = int(input("Masukkan nilai B: "))
isi = b-a
temp = a
array = [0 for i in range(isi+1)]
for i in range(isi+1):
    array[i] = temp
    temp += 1
for i in range(isi):
    if(prima(array[i]) == False):
        j = i+1
        while(j != isi+1):
            if(prima(array[j]) ==  False):
                print(array[i], end=" ")
                print(array[j], end="\n")
            j+=1
