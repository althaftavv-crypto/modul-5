def Biodata(tahun_lahir, nama, asal):
    tahun_sekarang = 2020
    print("Perkenalkan Nama Saya :", nama)
    print("Umur Saya :", tahun_sekarang - tahun_lahir)
    print("Saya Adalah Angkatan :", tahun_sekarang)
    print("Asal Saya dari :", asal)


tahunLahir = int(input())
Namaku = input().strip()
Asal = input().strip()
Biodata(tahunLahir, Namaku, Asal)