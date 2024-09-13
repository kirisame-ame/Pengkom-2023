#Nama : William Andrian Dharma T
#NIM : 19623048
#Tanggal : 21/09/23
#Sesi : 4.3 c

#Program penentuan jenis angka

#KAMUS
#angka = int
#digit1, digit2, digit3, digit4 = int

#ALGORITMA
angka = int(input("Masukkan Angka: "))
#mendapat digit pertama
digit1 = int(angka / 1000)
#modulo 1000 agar sisa 3 digit lalu diambil terdepan
digit2 = int(angka % 1000 / 100)
#modulo 100 agar sisa 2 digit lalu diambil terdepan
digit3 = int(angka % 100 / 10)
#modulo 10 agar sisa 1 digit lalu diambil
digit4 = int(angka % 10)

#mengecek kondisi angka spesial
if digit2 + digit3 == 0:
    print("Angka", angka, "bukan angka spesial.")
elif (digit1 * digit4) % (digit2 +digit3) == 0:
    print("Angka",angka,"adalah angka spesial.")
else:
    print("Angka", angka, "bukan angka spesial.")


