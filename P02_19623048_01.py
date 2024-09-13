#NIM/Nama : 19623048 / William Andrian Dharma T
#Tanggal : 05/10/23
#Deskripsi : Program Menghitung alokasi gedung

#Program menghitung alokasi gedung

#KAMUS
#n, slot_a, slot_b,peserta,index = int

#ALGORITMA
index = 1
slot_a = 0
slot_b = 0
#meminta nilai n
n = int(input("Masukkan nilai N : "))
#program berhenti saat kapasitas gedung b penuh
while slot_b < 3:
    peserta = int(input("Masukkan peserta kegiatan ke-{} : ".format(index)))
    #acara di gedung a saat peserta < n dan kapasitas gedung a belum penuh
    if peserta < n and slot_a < 5:
        slot_a += 1
    #jika tidak pindah ke gedung b
    else:
        slot_b += 1
    index += 1
print("Terdapat",slot_a,"kegiatan di gedung A dan",slot_b,"kegiatan di gedung B.")