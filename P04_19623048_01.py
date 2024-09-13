#NIM/NAMA : 19623048 / William Andrian Dharma T
#Tanggal : 02/11/23
#Deskripsi : Program menghitung nilai

#kamus Global
#a, b, c, nilai1, nilai2, nilai3 = float

#kamus lokal
#validity = bool
#b1,b2,b3,n1,n2,n3 = float

#fungsi/prosedur

#cek_valid = fungsi (karena me-return nilai)
#hitung = prosedur (karena tidak me-return nilai)

def cek_valid(b1,b2,b3):
    #jika bobot total = 1
    if b1 + b2 + b3 == 1:
        #jika bobot masing2 di rentang 0 - 1
        if 0 <= b1 <= 1 and 0 <= b2 <= 1 and 0 <= b3 <= 1:
            validity = True
        else:
            validity = False
    else:
        validity = False
    #mengembalikan validitas bobot
    return validity
def hitung(b1,b2,b3,n1,n2,n3):
    validity = cek_valid(b1,b2,b3)
    #jika valid maka baru dihitung nilainya
    if validity == True:
        print("Nilai tugas praktikum adalah",b1 * n1 + b2 * n2 + b3 * n3)
    else:
        print("bobot tidak valid")

#algoritma
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))
nilai1 = float(input("Masukkan nilai soal 1: "))
nilai2 = float(input("Masukkan nilai soal 2: "))
nilai3 = float(input("Masukkan nilai soal 3: "))

hitung(a,b,c,nilai1,nilai2,nilai3)

#これは私の印鑑