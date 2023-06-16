persamaan = input("MASUKKAN BILANGAN :")

posisi_operator = persamaan.find("*")

bilangan1 = int(persamaan[:posisi_operator])
bilangan2 = int(persamaan[posisi_operator + 1:])

hasil_perkalian = 0
for _ in range (bilangan2) :
    hasil_perkalian += bilangan1

print("=================================")
print("HASIL PERKALIAN   :" , hasil_perkalian)