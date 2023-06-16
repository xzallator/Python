# menjumlahkan dua bilangan
def penjumlahan(a, b):
    return a + b

# mengurangi dua bilangan
def pengurangan(a, b):
    return a - b

# mengalikan dua bilangan
def perkalian(a, b):
    return a * b

# membagi dua bilangan
def pembagian(a, b):
    return a / b

# memasukkan dua bilangan
bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))

# Menampilkan hasil operasi matematika
print("======================================================")
print("Hasil penjumlahan:", penjumlahan(bilangan1, bilangan2))
print("Hasil pengurangan:", pengurangan(bilangan1, bilangan2))
print("Hasil perkalian:", perkalian(bilangan1, bilangan2))
print("Hasil pembagian:", pembagian(bilangan1, bilangan2))
