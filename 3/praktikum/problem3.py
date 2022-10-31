from array import array


banyakData = int(input("Masukkan banyak data: "))
arrayOfData = [0 for i in range(banyakData)]
arrayOfDataNew = [0 for i in range(banyakData)]
count = 1
for i in range(banyakData):
    arrayOfData[i] = int(input(f"Masukkan data ke-{i+1}: "))
for i in range(banyakData-1):
    for j in range(0, banyakData-i-1):
        if(arrayOfData[j] > arrayOfData[j+1]):
            arrayOfData[j], arrayOfData[j+1] = arrayOfData[j+1], arrayOfData[j]
for i in range(banyakData-1):
    if(arrayOfData[i+1] != (arrayOfData[i]+1)):
        count += 1
print(f"banyak grup angka terurut adalah {count}.")

