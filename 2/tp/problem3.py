n = int(input("Masukkan N: "))
prima = 1
string = "Faktor primanya adalah "
for i in range(2, n+1):
    cekprima = True
    if((n%i) == 0):
        for j in range(2, i):
            if((i%j) == 0):
                cekprima = False
        if(cekprima == True):
            if(prima == 1):
                string += str(i)
                prima += 1
            else:
                string += ", "
                string += str(i)
                prima += 1
string += "."
print(string)    