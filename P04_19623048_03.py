#NIM/NAMA : 19623048 / William Andrian Dharma T
#Tanggal : 02/11/23
#Deskripsi : Program catur unik

#kamus global
#m, king_x, king_y = int
#papan = array

#kamus lokal
#papan = array
#kingx,kingy = int
#safety = bool

#prosedur keamanan raja
def pathing(papan,kingx,kingy):
    #declare keadaan keamanan raja
    #untuk setiap loop dicek keamanan agar tidak perhitungan sia2 jika sudah tidak aman
    safety = True
    for i in range(m):
        if safety == True:
            for j in range(m):
                if safety == True:
                    #cek semua lokasi kuda
                    if papan[i][j] == "K":
                        #jika ada gerakan valid dari kuda ke raja maka tidak aman
                        if ((kingx - j == 2 and kingy - i == 1) or (kingx - j == -2 and kingy - i == 1) or (kingx - j == -2 and kingy - i == -1) or (kingx - j == 2 and kingy - i == -1))or((kingx - j == 1 and kingy - i == 2) or (kingx - j == -1 and kingy - i == 2) or (kingx - j == -1 and kingy - i == -2) or (kingx - j == 1 and kingy - i == -2)):
                            safety = False
    if safety == True:
        print("Raja aman dari serangan kuda.")
    else:
        print("Raja tidak aman dari serangan kuda.")

#algoritma
m = int(input("Masukkan nilai m: "))
papan = [[0 for i in range(m)]for i in range(m)]
print("Masukkan kondisi papan catur ")
#meminta masuk layout papan catur
for i in range(m):
    papan[i] = input().split(" ",m)
    for j in range(m):
        #mencari index koordinat raja
        if papan[i][j] == "R":
            king_x = j
            king_y = i
pathing(papan,king_x,king_y)

#これは私の印鑑

