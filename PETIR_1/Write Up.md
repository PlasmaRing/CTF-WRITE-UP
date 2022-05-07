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
1. Download `run` file
2. Buka terminal, dan pergi ke __directory file__
3. Ketik `chmod +x run` untuk membuat file __executable__
4. Ketik `./run`
5. FLAG DIPEROLEH

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
