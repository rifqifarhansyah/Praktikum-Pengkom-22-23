n = int(input("Masukkan nilai N: "))
papan = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        papan[i][j] = "."
nBidak = int(input("Masukkan banyak bidak: ")) 
for i in range(nBidak):
    x = int(input(f"Masukkan posisi x bidak {i+1}: "))
    y = int(input(f"Masukkan posisi y bidak {i+1}: "))
    papan[y-1][x-1] = "K"
    if((y-1)-2 > 0):
        papan[y-3][x-1] = "#"
    if((y-1)+2 < n):
        papan[y+1][x-1] = "#"
    if((x-1)-3 > 0):
        papan[y-1][x-4] = "#"
    if((x-1)+3 < n):
        papan[y-1][x+2] = "#"
for i in range(n):
    for j in range(n):
        if(j != n-1):
            print(papan[i][j], end=" ")
        else:
            print(papan[i][j], end="\n")