#Nama : William Andrian Dharma T
#NIM : 19623048
#Tanggal : 21/09/23
#Sesi : 4.3 c

#Program konversi mata uang

#KAMUS
#jumlah_peng = int
#jumlah_kom = int
#pengidr = int
#komidr = int

#ALGORITMA
#meminta input semua variable yang dibutuhkan
jumlah_peng = int(input("Banyak uang Peng yang ditawarkan: "))
jumlah_kom = int(input("Banyak uang Kom yang ditawarkan: "))
pengidr = int(input("Konversi mata uang Peng ke rupiah: "))
komidr = int(input("Konversi mata uang Kom ke rupiah: "))
#membandingkan hasil konversi peng dan kom, kemudian dipilih yang lebih besar
if jumlah_peng * pengidr > jumlah_kom * komidr:
    print("Adik Tuan Kil memilih uang Peng.")
elif jumlah_kom * komidr > jumlah_peng * pengidr:
    print("Adik Tuan Kil memilih uang Kom.")
elif jumlah_kom * komidr == jumlah_peng * pengidr:
    print("Adik Tuan Kil bebas memilih yang manapun.")
