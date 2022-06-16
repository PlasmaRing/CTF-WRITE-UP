# MENGPETIR 1
APR 07 - APR 14 | 2022

## Overview

| No | Title               | Category              | Flag
|----|---------------------|-----------------------|----------------------------
| 1  | guess my number | Reverse Engineering | anjay{9876}
| 2  | biji waktu | Reverse Engineering | anjay{were_you_toooooooo_fast?}
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
![image](https://user-images.githubusercontent.com/92077284/167345412-aa1dd78c-9172-4878-a95a-abd1af735881.png)  
11. FLAG DIPEROLEH

**Flag**  
`anjay{9876}`


## biji waktu

**Description**  
time is money, money is seed

**Hints 1**  
seednya pake srand(time), berarti cari timenya (kapan codingan tersebut dijalankan dalam format unix time). 

**Hints 2**  
program dijalankan ga lama sebelum adminnya upload soal, tapi kapan tepatnya?

**Solution [INA]**  
1. Analisa file `biji waktu` menggunakan IDA  
![image](https://user-images.githubusercontent.com/92077284/174102773-13ce6214-b9e5-4ee1-9270-491300c01274.png)
![image](https://user-images.githubusercontent.com/92077284/174109251-28a19aba-f926-45c4-bd5d-13843ff4f091.png)

file __biji waktu__ merupakan file yang akan membaca file dan akan __generate key__ lalu di simpan di `secret_message.enc`. Key yang akan di __generate__ akan di random sesuai dengan waktu key dibuat. Proses pembuatan key tertera pada foto kedua.  

2. Prediksi kapan admin membuat soal dengan melihat kapan admin memberikan soal `(admin memberikan soal pada 7 April 2022)`  
3. Tentukan __range timestamp__ menggunakan website `https://www.epochconverter.com`   
`1649203200 - 6 April 2022 07:00 GMT+7`  
`1649376000 - 8 April 2022 07:00 GMT+7`

4. Buat program untuk melakukan searching pada __range timestamp__ diatas  
Program : [JAWABAN.py](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/88d10af4ebad36165dd1ba1a789a067f4a666142/PETIR_1/FILE/%5BREV%5D%20biji%20waktu/JAWABAN.py)  
![image](https://user-images.githubusercontent.com/92077284/174110176-32fec449-ce61-46ef-9149-5ec37d66eca4.png)  
Pada program ini, file akan membaca file `secret_message.enc` lalu melakukan searching pada __range timestamp__ lalu dikombinasikan dengan proses pembuatan key `key = libc.rand() % 50`. Lalu selama proses searching, apabila ditemukan kata __anjay__ maka program akan melakukan proses print. 

5. Ketik `python3 JAWABAN.py` di terminal pada directory yang sama dengan `secret_message.enc`  
![image](https://user-images.githubusercontent.com/92077284/174112143-c1656e46-b552-4aec-bad7-3702eba56993.png)

6. FLAG DIPEROLEH

**Flag**  
`anjay{were_you_toooooooo_fast?}`

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
