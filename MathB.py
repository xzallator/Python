
def hitung_segitiga():
    print("Hitung Luas Segitiga")
    alas    = float (input("Masukkan Alas    : "))
    tinggi  = float (input("Masukkan Tinggi  : "))
    luas = 0.5 * ( alas * tinggi )

    print("Luas Segitiga : ", luas, "\n")
    print("============================")

def hitung_balok():
    print("Hitung Luas Balok")
    panjang  = float (input("Masukkan Panjang : "))
    tinggi   = float (input("Masukkan Tinggi  : "))
    lebar    = float (input("Masukkan lebar   : "))
    luas     = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)

    print("Luas Balok   : " , luas, "\n")
    print("============================")

def hitung_bola():
    print("Hitung Luas Bola")
    r      = float (input("Masukkan Jari-Jari : "))
    luas   = 4 * 3,14 * ( r**2 )

    print("Luas Bola : " , luas, "\n")
    print("============================")

while True :
    userInput = int(input("OPSI PROSES PERHITUNGAN : \n\n1.Luas Segitiga\n2.Luas Balok\n3.Luas Bola\n\n0.Keluar Program\n\nSilahkan Pilih Nomor :"))
    if(userInput == 1):
        hitung_segitiga()
    elif(userInput == 2):
        hitung_balok()
    elif(userInput == 3):
        hitung_bola()
    else:
        break