pemain1 = int(input(f"Banyak pemain yang memainkan level 1: "))
berhasil1 = int(input(f"Banyak pemain yang berhasil menyelesaikan level 1: "))
pemain2 = int(input(f"Banyak pemain yang memainkan level 2: "))
berhasil2 = int(input(f"Banyak pemain yang berhasil menyelesaikan level 2: "))
pemain3 = int(input(f"Banyak pemain yang memainkan level 3: "))
berhasil3 = int(input(f"Banyak pemain yang berhasil menyelesaikan level 3: "))
pemain4 = int(input(f"Banyak pemain yang memainkan level 4: "))
berhasil4 = int(input(f"Banyak pemain yang berhasil menyelesaikan level 4: "))
pemain5 = int(input(f"Banyak pemain yang memainkan level 5: "))
berhasil5 = int(input(f"Banyak pemain yang berhasil menyelesaikan level 5: "))
mudah = 0
sedang = 0
sulit = 0
if(berhasil1 >= (pemain1*0.8)):
    mudah += 1
elif((berhasil1 >= (pemain1*0.3)) & (berhasil1 < (pemain1*0.8))):
    sedang += 1
elif(berhasil1 < (pemain1*0.3)):
    sulit += 1

if(berhasil2 >= (pemain2*0.8)):
    mudah += 1
elif((berhasil2 >= (pemain2*0.3)) & (berhasil2 < (pemain2*0.8))):
    sedang += 1
elif(berhasil2 < (pemain2*0.3)):
    sulit += 1

if(berhasil3 >= (pemain3*0.8)):
    mudah += 1
elif((berhasil3 >= (pemain3*0.3)) & (berhasil3 < (pemain3*0.8))):
    sedang += 1
elif(berhasil3 < (pemain3*0.3)):
    sulit += 1

if(berhasil4 >= (pemain4*0.8)):
    mudah += 1
elif((berhasil4 >= (pemain4*0.3)) & (berhasil4 < (pemain4*0.8))):
    sedang += 1
elif(berhasil4 < (pemain4*0.3)):
    sulit += 1

if(berhasil5 >= (pemain5*0.8)):
    mudah += 1
elif((berhasil5 >= (pemain5*0.3)) & (berhasil5 < (pemain5*0.8))):
    sedang += 1
elif(berhasil5 < (pemain5*0.3)):
    sulit += 1

print(f"Banyak level mudah sebanyak {mudah}, level sedang sebanyak {sedang}, dan level sulit sebanyak {sulit}.")
if((mudah >= 2) & (sulit >=1)):
    print(f"Target berhasil dicapai.")
else:
    print(f"Target gagal dicapai.")

