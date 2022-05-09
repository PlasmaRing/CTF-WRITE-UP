# MENGPETIR 1
APR 07 - APR 14 | 2022

## Overview

| No | Title               | Category              | Flag
|----|---------------------|-----------------------|----------------------------
| 1  | guess my number | Reverse Engineering | anjay{}
| 2  | biji waktu | Reverse Engineering | anjay{}
| 3  | ciilik | Cryptography | anjay{}

# Reverse Engineering 
## guess my number

**Description**  
Guess my Number.exe in C++

**Hints 1**  
bruteforce or IDA?

**Solution [INA]**  
1. Download [hahah.exe](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/e86b2c4bb6a9f7c9d718313e3b95fd3f636960c5/PETIR_1/FILE/%5BREV%5D%20guess%20my%20number/hahah.exe) file
2. Proses file __hahah.exe__ menggunakan IDA
![image](https://user-images.githubusercontent.com/92077284/167343987-ccbd82fd-0f95-4739-b944-9182fb810dec.png)
3. Disini dapat dianalisis bahwa program meminta user menginput sebuah angka
4. angka tersebut memiliki syarat yang dapat dianalisis

Berikut analisis angka
![image](https://user-images.githubusercontent.com/92077284/167344194-3cad2619-14cc-4c55-8266-dfa2e503db48.png)
![image](https://user-images.githubusercontent.com/92077284/167344212-b606165c-6cf2-418c-9040-39a580a6c8ac.png)
![image](https://user-images.githubusercontent.com/92077284/167344254-bd4beb56-0ff9-479b-83a4-bd0c8e917a5a.png)
5. Diketahui bahwa __bob == 1692__ untuk menghasilkan return __exit(1)
6. Maka __yeet = 1692 + 8184 = 9876__ 
7. Pada validasi __gemink(nah), angka 9876 lolos__
8. Pada validasi awal __ez(numb), angka 9876 lolos__
9. Diperoleh angka adalah __9876__
10. Proses cek dengan menjalankan __hahah.exe__
11.
12. FLAG DIPEROLEH

**Flag**  
``


## biji waktu

**Description**  
time is money, money is seed

**Hints 1**  
seednya pake srand(time), berarti cari timenya (kapan codingan tersebut dijalankan dalam format unix time). 

**Hints 2**  
program dijalankan ga lama sebelum adminnya upload soal, tapi kapan tepatnya?

**Solution [INA]**  
1. Download `run (1)` file
2. Buka terminal, dan pergi ke __directory file__
3. Ketik `chmod +x 'run(1)'` untuk membuat file __executable__
4. Ketik `./'run(1)' Hello!`
5. FLAG DIPEROLEH

**Flag**  
``

# Cryptography
## cilik

**Description**  
kecil kecil cabe ijo

**Hints 1**  
always use 'from Crypto.Util.number import *' for challenge like this, it's good for u

**Hints 2**  
apa yang terjadi jika modulus (n) terlalu besar?

**Solution [INA]**  
1. Download `gdbme` file
2. Buka terminal, dan pergi ke __directory file__
3. Ketik `chmod +x gdbme` untuk membuat file __executable__
4. Ketik `gdb gdbme`
5. Ketik `(gdb) layout asm` untuk membuka layout gdb
6. Ketik `break *(main+99)`
7. Ketik `run`
8. Ketik `jump *(main+104)`
9. FLAG DIPEROLEH


**Flag**  
``
