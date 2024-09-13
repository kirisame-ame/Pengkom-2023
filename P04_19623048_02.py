#NIM/NAMA : 19623048 / William Andrian Dharma T
#Tanggal : 02/11/23
#Deskripsi : Program merubah matrix

#kamus
#m, n = int
#matriks, new_matriks = array

#algoritma
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))
matriks = [[0 for i in range(n)] for i in range(m)]
print("Masukkan elemen matriks")
#mengisi matriks secara split agar terlihat seperti matriks biasa
for i in range(m):
    matriks[i] = input().split(" ",n)
    for j in range(n):
        matriks[i][j] = float(matriks[i][j])
#membuat matriks kosong baru seukuran yang lama
new_matriks = [[0 for i in range(n)] for i in range(m)]
#loop perubahan nilai
for i in range(m):
    for j in range(n):
        #vertical check
        if i == 0:
            new_matriks[i][j] += matriks[i+1][j]
        elif i == m - 1:
            new_matriks[i][j] += matriks[i-1][j]
        else:
            new_matriks[i][j] += matriks[i + 1][j] + matriks[i-1][j]
        #horizontal check
        if j == 0:
            new_matriks[i][j] += matriks[i][j+1]
        elif j == n - 1:
            new_matriks[i][j] += matriks[i][j - 1]
        else:
            new_matriks[i][j] += matriks[i][j + 1] + matriks[i][j - 1]
print("Matriks baru:")
for i in range(m):
    for j in range(n):
        print(new_matriks[i][j],end=" ")
    print()

#これは私の印鑑