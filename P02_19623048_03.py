#NIM/Nama : 19623048 / William Andrian Dharma T
#Tanggal : 05/10/23
#Deskripsi : Program membuat piramida bilangan

#Program membuat piramida bilangan

#KAMUS
#pjg, selisih, bilangan,bil_count,baris = int

#ALGORITMA
#meminta input
pjg = int(input("Masukkan panjang piramida : "))
selisih = int(input("Masukkan selisih bilangan : "))
#inisialisasi variable
bilangan = 1
bil_count = 0
baris = 0
#jika piramida genap kurangi 1
if pjg % 2 == 0:
    pjg -= 1
#program terus berjalan sampai count bilangan baris terbawah sama dengan panjang piramida
while bil_count != pjg:
    baris += 1
    #memprint 'X' di kiri bilangan sejumlah (pjg+1)//2 - baris
    for j in range((pjg+1)//2 - baris,0,-1):
            print("X",end="")
    #memprint nilai bilangan setelah 'X' kiri sejumlah 2*baris - 1
    for k in range(2*baris-1):
            print(bilangan,end="")
            bil_count = k + 1
    # memprint 'X' di kanan bilangan sejumlah (pjg+1)//2 - baris
    for l in range((pjg+1) // 2 - baris, 0, -1):
            print("X", end="")
    #menghitung nilai bilangan baris berikutnya yang hanya diambil satuannya
    bilangan = (bilangan + selisih) % 10
    #berpindah barus
    print()