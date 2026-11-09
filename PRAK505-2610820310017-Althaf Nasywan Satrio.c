#include <stdio.h>

void Biodata(int tahun_lahir, char nama[], char asal[]) {
    int tahun_sekarang = 2020;
    printf("Perkenalkan Nama Saya : %s\n", nama);
    printf("Umur Saya : %d\n", tahun_sekarang - tahun_lahir);
    printf("Saya Adalah Angkatan : %d\n", tahun_sekarang);
    printf("Asal Saya dari : %s\n", asal);
}

int main() {
    int tahunLahir;
    char A[20], B[15];
    scanf(" %d", &tahunLahir);
    scanf(" %19[^\n]%*c", A);
    scanf(" %14[^\n]%*c", B);
    Biodata(tahunLahir, A, B);
    return 0;
}