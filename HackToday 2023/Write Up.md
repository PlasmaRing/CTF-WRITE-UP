## WRITE UP [IND]  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/9fc7baf4-a2f2-4f82-afff-b067f8cecef9)  

**Team: Bude Jiang Society**  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/5b8b28b9-bda7-456f-8a72-633ec2c56667)

**DATE: 26 AUGUST 2023**  

**WRITE UP LINK👇**  
[LINK](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/6f14c90b1582c14a5b1b0c8baa67b0404744b938/HackToday%202023/FILE/WRITE%20UP%20HackToday%202023.pdf)

## Solved Probs

**Reverse Engineering**  
● OnlyAdminCanSee  
● kurang-lebih+  
● Nyicil **[SOLVED AFTER COMPETITION END]**  
  
**Web Exploitation**  
● LogInspek 

**Forensic**  
● Doodled  

**Misc**  
● DCHEZKIBOXS  
● Where is my git?  

**OSINT**  
● MUA    

---
# Nyicil
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/5e28f78b-af96-4042-bd2e-74dca99030cc)  
1. Pertama-tama diberikan sebuah file ELF, dan disini merupakan flag checker namun dibatasi panjangnya sebanyak 10 karakter
   ![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/d6fc6262-8e7e-491e-a79b-9d9ea0a4b576)  
   Kesimpulan dari file ini:  
   * BENAR = seluruhnya benar  
   * ADA YANG BENAR = terdapat bagian yang benar  
   * MENYICIL TIDAK PERLU BANYAK = panjang karakter melebihi 10  
2. Dari situlah kita bisa melakukan **bruteforce** dan _wordlist_ karena dari awal sudah diketahui bahwa format flag adalah **hacktoday{*}**, maka tinggal dicari didalamnya apa

   Script untuk generate wordlist =
   ```c
   #include <stdio.h>
   #include <string.h>
   
   int main() {
     char key[] = "hacktoday"; // diganti-ganti
   
   // nebak char setelah key
     for (char z = '!'; z <= '}'; z++) {
       printf("%s%c\n", key, z);
     }
   
   // Nebak char di belakang key
     for (char z = '!'; z <= '}'; z++) {
       printf("%c%s\n", z, key);
     }
     return 0;
   }
   ```
   command untuk store ke .txt =  
   ```
   gcc brute.c -o brute
   ./brute > output.txt
   ```

   script untuk bruteforce =
   ```py
   from pwn import *
   
   r = process("./Nyicil")
   r.recv()
            
   with open("output.txt", "r") as f:
     passwords = f.readlines()
                
     for password in passwords:
       r.sendline(password.strip())
       print(r.recv(), password)   
   ```
    
3. Setelah itu lakukan percobaan hingga flag berhasil dicicil secara utuh

   Contoh dengan menggunakan key = `today{`

   Output =  
   ![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/1424d49f-b9de-40ee-9b0e-1bc4147517ed)
   Didapati potongannya menjadi `today{A`
4. Setelah percobaan berkali-kali ditemukan adanya kejanggalan dengan kata "Nyicil" karena disini terdapat 4 variasi yang dihasilkan
   ![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/a26f8dc0-44fa-403a-8dfb-724f325fdba7)
   ![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/05384229-6fe8-4bc3-a805-8f685ee2e6e9)
   Kesimpulannya :  
   * Terdapat 4 variasi penulisan Nyicil
   * Jika **flag checker** ini benar, maka seharusnya dalam flag terdapat 4 variasi nyicil tersebut, hanya saja berbeda penulisan
   * Karena terdapat pembatasan karakter, maka tidak bisa mencari lebih dari 10 karakter, tapi dapat disimpulkan bahwa pasti ada minimal 2 Nyicil yang bersambungan, contoh : `Ny1c1l_Ny1cIL`
6. Setelah disusun, kurang lebih didapati flag sebagai berikut `hacktoday{AkH1rny4_Luna5_Jug4_j4d1_G4k_Us4h_[kalimatnyicil]_L4g1}`
   Note : `[kalimatnyicil]` merupakan kombinasi dari 2 kata nyicil
7. Flag akhirnya didapat = **hacktoday{AkH1rny4_Luna5_Jug4_j4d1_G4k_Us4h_NY1c1l_Ny1cIL_L4g1}**  
   Note :
   ```
   Algoritma enkripsi sebenarnya bisa dibaca dari IDA, sudah juga untuk dicoba untuk recreate programnya dengan bahasa C, namun mungkin terdapat kesalahan / multiple output sehingga program bisa menuliskan "BENAR" walaupun sebenarnya salah
   ```

   Recreate Program in C =
    ```c
    #include <stdio.h>
    #include <string.h>
    
    int cicilan1[] = {
                    4, 0xFFFFFFFD, 0xFFFFFFFF, 0xFFFFFFFC, 0xFFFFFFFE, 6, 0xFFFFFFF8, 0, 9, 0xFFFFFFFC, 5, 0, 7, 2,
                0xFFFFFFF7, 9, 0xFFFFFFFE, 0xFFFFFFFB, 0xFFFFFFFA, 0xFFFFFFF7, 0xF, 0xFFFFFFF0, 8, 0xA, 0x12, 0x14,
                0xFFFFFFDA, 0x19, 0xFFFFFFDF, 9, 0xFFFFFFF0, 0x1A, 0xFFFFFFF7, 0x1F, 0xFFFFFFFC, 0xFFFFFFE5, 0xFFFFFFFA,
                0xFFFFFFE3, 0x24, 0xFFFFFFD6, 0x17, 0x13, 0xFFFFFFFF, 0xFFFFFFFB, 6, 0x10, 0x1B, 0xFFFFFFD6, 0x20,
                0xFFFFFFDB, 6, 0xFFFFFFEA, 0x15, 2, 0xFFFFFFFF, 0xFFFFFFEC, 0x15, 0xFFFFFFE7, 0x10, 9, 9, 2, 0xFFFFFFF5,
                0x18, 0xB, 0xFFFFFFDF, 0x10, 0xFFFFFFE4, 0xE, 0xFFFFFFEB, 0x15, 2, 2, 0xFFFFFFEB, 0x16, 0xFFFFFFE8,
                0x13, 5, 0x1B, 0xD, 0xFFFFFFDA, 0x14, 0xFFFFFFE1, 0xC, 0xFFFFFFE0, 0xB, 0x16, 0xB, 0x16, 0xFFFFFFE0,
                0x14, 0xFFFFFFDE, 0xE, 0xFFFFFFF1, 0x21, 0xFFFFFFEE, 0x13, 0xFFFFFFE0, 0xE, 0xFFFFFFEA, 0x18, 0, 0x17,
                0xFFFFFFFF, 0xFFFFFFEC, 0xFFFFFFFB, 0xFFFFFFE8, 0x1F, 0xFFFFFFE0, 0x17, 0xB, 0xC, 0, 0xFFFFFFF6,
                0xFFFFFFFD, 0xFFFFFFF3, 0x11, 1, 0x1F, 0xFFFFFFE0, 0x19, 0xFFFFFFDA, 0xE, 0xFFFFFFE1, 0x15, 0xC, 0xC,
                3, 0xFFFFFFF2, 8, 0xFFFFFFF7, 2, 6, 0x11, 0xFFFFFFE9, 0xA, 0xFFFFFFE2, 0x14, 0xFFFFFFF0, 0x22,
                0xFFFFFFF0, 0xE, 0xFFFFFFDC, 0x17, 0xFFFFFFDD, 0x18, 0xB, 0xF, 2, 0xFFFFFFF1, 0xFFFFFFFD, 0xFFFFFFEC,
                0x17, 0xFFFFFFFC, 0x27, 0xFFFFFFDF, 0x20, 0xFFFFFFD8, 0xA, 0xFFFFFFE8, 0x1A, 0, 0x11, 0xFFFFFFF7,
                0xFFFFFFFA, 0xFFFFFFF8, 0xFFFFFFFB, 0xE, 0xFFFFFFFA, 0xD, 0xFFFFFFFA, 0x15, 2, 0xFFFFFFEA,
                0xFFFFFFFF, 0xFFFFFFE7, 0x1A, 0xFFFFFFF0, 0x23, 0xFFFFFFED, 0xB, 0xFFFFFFD5, 0x21, 0
    };
    
    int cicilan2[] = {
                0x64, 0x65, 0x6B, 0x6F, 0x6D, 0x66, 0x6A, 0x71, 0x67, 0x62, 0x51, 0x4C, 0x4E, 0x5B, 0x73, 0x5E,
                0x59, 0x4A, 0x60, 0x65, 0x6C, 0x56, 0x51, 0x4A, 0x5F, 0x62, 0x5A, 0x53, 0x54, 0x54, 0x56, 0x43,
                0x51, 0x47, 0x48, 0x4C, 0x54, 0x5F, 0x62, 0x54, 0x5A, 0x53, 0x5C, 0x57, 0x48, 0x4F, 0x41, 0x55,
                0x54, 0x5D, 0x62, 0x52, 0x59, 0x49, 0x52, 0x51, 0x52, 0x4A, 0x4D, 0x44, 0x5C
    };
    
    int cek(int a1, int a2, int a3, int a4) {
        for (int i = 0; i < 61; ++i) {
            if (a4 == cicilan2[i]) {
                int v6 = 3 * i;
                if (a1 == cicilan1[3 * i] && a2 == cicilan1[v6 + 1] && a3 == cicilan1[v6 + 2]) {
                    return 128;
                }
            }
        }
        return -11;
    }
    
    int nyicil(int* a1, int a2) {
        if (a2 <= 2) {
            return -1; // 0xFFFFFFFF
        }
        int v3 = 0;
        for (int i = 0; i < a2 - 2; ++i) {
            int v5 = 0;
            for (int j = i; j < i + 3; ++j) {
                v5 += a1[j];
            }
            if (cek(a1[i] - v5 / 3, a1[i + 1] - v5 / 3, a1[i + 2] - v5 / 3, v5 / 3) == 128) {
                v3++;
            }
        }
        return v3;
    }
    
    int main() {
        char s[256]; // Assuming maximum input length
        printf("masukan FLAG: ");
        scanf("%s", s);
        
        int v4 = strlen(s);
        int s_bytes[v4];
        for (int i = 0; i < v4; ++i) {
            s_bytes[i] = (int)s[i];
        }
        
        int v5 = nyicil(s_bytes, v4);
        
        if (v5 == v4 - 2) {
            printf("BENAR!\n");
        } else {
            printf("salah\n");
        }
    
        return 0;
    }
    
    ```
