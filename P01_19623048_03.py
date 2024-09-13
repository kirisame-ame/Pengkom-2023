#Nama : William Andrian Dharma T
#NIM : 19623048
#Tanggal : 21/09/23
#Sesi : 4.3 c

#Program penentuan kecukupan bahan untuk baju

#KAMUS

#jumlah_kain = float
#jumlah_pita = float
#jumlah_s, jumlah_m, jumlah_l

#ALGORITMA
jumlah_kain = float(input("Jumlah Kain : "))
jumlah_pita = float(input("Jumlah Pita : "))

#nona deb ingin membuat 1 setiap ukuran jika tidak maka gagal
if jumlah_kain >= 4.7 and jumlah_pita >= 3.1:
    jumlah_kain -= 4.7
    jumlah_pita -= 3.1
    jumlah_s = 1
    jumlah_m = 1
    jumlah_l = 1
    #nona deb memprioritaskan ukuran L
    if jumlah_kain >= 2 and jumlah_pita >= 1.3:
        if jumlah_kain / 2 >= jumlah_pita / 1.3:
            jumlah_l += int(jumlah_pita / 1.3)
            jumlah_kain -= int(jumlah_pita / 1.3) * 2
            jumlah_pita -= int(jumlah_pita / 1.3) * 1.3
        elif jumlah_kain / 2 < jumlah_pita / 1.3:
            jumlah_l += int(jumlah_kain / 2)
            jumlah_kain -= int(jumlah_kain / 2) * 2
            jumlah_pita -= int(jumlah_kain / 2) * 1.3
    #setelah ukuran L, ukuran M
    if jumlah_kain >= 1.5 and jumlah_pita >= 1:
        if jumlah_kain / 1.5 >= jumlah_pita / 1:
            jumlah_m += int(jumlah_pita / 1)
            jumlah_kain -= int(jumlah_pita / 1) * 1.5
            jumlah_pita -= int(jumlah_pita / 1) * 1
        elif jumlah_kain / 1.5 < jumlah_pita / 1:
            jumlah_m += int(jumlah_kain / 1.5)
            jumlah_kain -= int(jumlah_kain / 1.5) * 1.5
            jumlah_pita -= int(jumlah_kain / 1.5) * 1
    # setelah ukuran M, ukuran S
    if jumlah_kain >= 1.2 and jumlah_pita >= 0.8:
        if jumlah_kain / 1.2 >= jumlah_pita / 0.8:
            jumlah_s += int(jumlah_pita / 0.8)
            jumlah_kain -= int(jumlah_pita / 0.8) * 1.2
            jumlah_pita -= int(jumlah_pita / 0.8) * 0.8
        elif jumlah_kain / 1.2 < jumlah_pita / 0.8:
            jumlah_s += int(jumlah_kain / 1.2)
            jumlah_kain -= int(jumlah_kain / 1.2) * 1.2
            jumlah_pita -= int(jumlah_kain / 1.2) * 0.8
    print("Nona Deb dapat membuat",jumlah_s,"ukuran S,",jumlah_m,"ukuran M,",jumlah_l,"ukuran L.")

else:
    print("Bahan tidak cukup untuk membuat baju.")



