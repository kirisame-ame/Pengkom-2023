#NIM/Nama : 19623048 / William Andrian Dharma T
#Tanggal : 05/10/23
#Deskripsi : Program membuat barisan bilangan

#Program membuat barisan bilangan

#KAMUS
#x,y,bilangan,y_new,sign_trigger = int

#ALGORITMA
bilangan = 0
#meminta input x dan y
x = int(input("Masukkan x: "))
y = int(input("Masukkan y: "))
#variabel untuk kelipatan y
y_new = y
#variable untuk +1 atau -1
sign_trigger = 1
#meloop hingga jumlah bilangan sama dengan x
for i in range(x):
    #jika kelipatan y pertama adalah 1, maka langsung ditambah 1
    if y_new == 1:
        y_new += y
    #jika bilangan mencapai kelipatan y yang ke-sekarang, akan menurun
    elif bilangan == y_new:
        sign_trigger = -1
        y_new += y
    #jika bilangan sudah kembali mencapai 1, akan naik lagi
    elif bilangan == 1:
        sign_trigger = 1
    #bilangan tambah atau kurang sesuai kondisi
    bilangan += 1 * sign_trigger
    #mengeluarkan bilangan tanpa pindah baris
    print(bilangan,end=" ")

