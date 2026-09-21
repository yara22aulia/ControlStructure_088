

if nilai >= 90:
    print("Excellent performance")
elif nilai >= 80:
    print("Very Good performance")
elif nilai >=70:
    print("Good performance")
elif nilai >=60:
    print("average performance")
else:
    print("Poor performance")

#2
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

if a >= b and a >= c:
    terbesar = a
elif b >= a and b >= c:
    terbesar = b
else:
    terbesar = c
    
print("Angka terbesar adalah:", terbesar)

#3
n = int(input("Masukkan n: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#4
n = int(input("Masukkan n: "))

for i in range(1, n + 1, 2):
    print(i, end=" ")

#5
n = int(input("Masukkan n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

