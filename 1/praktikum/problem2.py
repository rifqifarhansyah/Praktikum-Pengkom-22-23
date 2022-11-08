antrian = int(input("Masukkan nomor antrian tiket: "))
nomor = (antrian//4)+1
abjad = (antrian%4)
if(abjad == 1):
    abjad = "A"
elif(abjad == 2):
    abjad = "B"
elif(abjad == 3):
    abjad = "C"
else:
    abjad = "D"
print(f"Tempat duduk tiket nomor {antrian} memiliki nomor {nomor}{abjad}.")