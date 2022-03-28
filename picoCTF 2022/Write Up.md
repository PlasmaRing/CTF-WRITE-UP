# picoCTF 2022 WRITE UP
MAR 15 - MAR 30 | 2022

## Overview

| No | Title               | Category              | Points  | Flag
|----|---------------------|-----------------------|---------|----------------------------
| 1  | file-run1 | Reverse Engineering | 100 | picoCTF{U51N6_Y0Ur_F1r57_F113_ac61264e} 
| 2  | file-run2 | Reverse Engineering | 100 | picoCTF{F1r57_4rgum3n7_c2db2786}
| 3  | GDB Test Drive | Reverse Engineering | 100 | picoCTF{d3bugg3r_dr1v3_7e8f2155}
| 4  | patchme.py | Reverse Engineering | 100 | picoCTF{p47ch1ng_l1f3_h4ck_e40c120e}
| 5  | Safe Opener | Reverse Engineering | 100 | picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
| 6  | unpackme.py | Reverse Engineering | 100 | picoCTF{175_chr157m45_616d21a3}
| 7  | bloat.py | Reverse Engineering | 200 | 
| 8  | Fresh Java | Reverse Engineering | 200 | 
| 9  | Bbbbloat | Reverse Engineering | 300 | 
| 10 | unpackme | Reverse Engineering | 300 | 
| 11 | basic-mod1 | Cryptography | 100 | 
| 12 | basic-mod2 | Cryptography | 100 | 
| 13 | credstuff | Cryptography | 100 | 
| 14 | morse-code | Cryptography | 100 | 
| 15 | rail-fence | Cryptography | 100 | 
| 16 | substitution0 | Cryptography | 100 | 
| 17 | substitution1 | Cryptography | 100 | 
| 18 | substitution2 | Cryptography | 100 |
| 19 | transposition-trial | Cryptography | 100 | 
| 20 | Vigenere | Cryptography | 100 | 
| 21 | diffie-hellman | Cryptography | 200 | 
| 22 | Enhance! | Forensics | 100 | 
| 23 | Lookey here | Forensics | 100 | 
| 24 | Packets Primer | Forensics | 100 | 
| 25 | Redaction gone wrong | Forensics | 100 | 
| 26 | Includes | Web Exploitation | 100 | 
| 27 | Inspect HTML | Web Exploitation | 100 | 
| 28 | Local Authority | Web Exploitation | 100 | 
| 29 | Power Cookie | Web Exploitation | 200 |


# Reverse Engineering 
## file-run1

**Description**  
A program has been provided to you, what happens if you try to run it on the command line?
Download the program [here](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/86ca38d98bcde32d0d779086bfb8bd680efa27e5/picoCTF%202022/FILE/run)

**Hints 1**  
To run the program at all, you must make it executable (i.e. **$ chmod +x run**)

**Hints 2**  
Try running it by adding a '.' in front of the path to the file (i.e. **$ ./run**)

**Solution [INA]**  
1. Download `run` file
2. Buka terminal, dan pergi ke __directory file__
3. Ketik `chmod +x run` untuk membuat file __executable__
4. Ketik `./run`
5. FLAG DIPEROLEH

![CTFPICO](https://user-images.githubusercontent.com/92077284/160277012-1141bead-106c-4303-86d0-53f19d6b52d6.png)

**Flag**  
`picoCTF{U51N6_Y0Ur_F1r57_F113_ac61264e}`


## file-run2

**Description**  
Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?  
Download the program [here](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/0879a933e5e3c4d4a24921d2be7d48ffcb4f9cec/picoCTF%202022/FILE/run%20(1))

**Hints 1**  
Try running it and add the phrase "Hello!" with a space in front (i.e. **"./run Hello!"**)

**Solution [INA]**  
1. Download `run (1)` file
2. Buka terminal, dan pergi ke __directory file__
3. Ketik `chmod +x 'run(1)'` untuk membuat file __executable__
4. Ketik `./'run(1)' Hello!`
5. FLAG DIPEROLEH

![PICOCTF png](https://user-images.githubusercontent.com/92077284/160289524-7bde6d04-15f6-4933-9c6c-ec868e8d43ee.png)

**Flag**  
`picoCTF{F1r57_4rgum3n7_c2db2786}`


## GDB Test Drive

**Description**  
Can you get the flag?  
Download this [binary](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/6e04ec175decea84a6c1b989b32d864e72426eb7/picoCTF%202022/FILE/gdbme)  
Here's the test drive instructions:
```html
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```

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

![PICO1](https://user-images.githubusercontent.com/92077284/160289926-ef45b165-a8c7-42e3-ab22-de1b5f43cfa9.png)
![PICO2](https://user-images.githubusercontent.com/92077284/160289928-a0e842a3-3efe-4920-a17f-0e86ac179bd6.png)
![PICO3](https://user-images.githubusercontent.com/92077284/160289929-acb8110e-5bf9-41e1-aca2-67e534b3f231.png)

**Flag**  
`picoCTF{d3bugg3r_dr1v3_7e8f2155}`


## patchme.py

**Description**  
Can you get the flag?  
Run this [Python program](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/a1e50c69ec32ade2299b7f11163bb2e41434b43d/picoCTF%202022/FILE/patchmeflag/patchme.flag.py) in the same directory as this [encrypted flag](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/a1e50c69ec32ade2299b7f11163bb2e41434b43d/picoCTF%202022/FILE/patchmeflag/flag.txt.enc)

**Solution [INA]**  
1. Download kedua file dan masukan kedua file di folder yang sama
2. Buka file `patchme.flag.py`
3. Ubah input __user_pw__ menjadi sama dengan syarat mendapatkan flag
4. Buka terminal dan pergi ke __directory file__
5. Ketik `python patchme.flag.py` untuk menjalankan file
6. FLAG DIPEROLEH

![PICO1](https://user-images.githubusercontent.com/92077284/160290740-f43a3c21-cc52-4874-b9a2-4c89984fb8de.png)
![PICO2](https://user-images.githubusercontent.com/92077284/160290741-aca7b1c8-b14c-400f-a50f-3cbd7ff115e7.png)

**Flag**  
`picoCTF{p47ch1ng_l1f3_h4ck_e40c120e}`


## Safe Opener

**Description**  
Can you open this safe?  
I forgot the key to my safe but this [program](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/0b9517138b003f511e19f7cbe836cf452a9b7eb7/picoCTF%202022/FILE/SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?  
Put the password you recover into the picoCTF flag format like:  
__picoCTF{password}__

**Solution [INA]**  
1. Download file `SafeOpener.java`
2. Buka file dan analisa, didapati kode yang terenkripsi oleh __Base64__ adalah `cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz`
3. Decode string menggunakan __Base64 online decoder__ seperti https://www.base64decode.org/
4. Didapati hasil: `pl3as3_l3t_m3_1nt0_th3_saf3`, ubah sesuai format flag
5. FLAG DIPEROLEH

![PICO1](https://user-images.githubusercontent.com/92077284/160291573-2a9fe800-783c-42f8-ae62-ee78d6cbdf68.png)

**Flag**  
`picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}`


## unpackme.py

**Description**  
Can you get the flag?  
Reverse engineer this [Python program](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/21ba29aaece9f670d034ed39b03b1200fa447ce9/picoCTF%202022/FILE/unpackme.flag.py)

**Solution [INA]**  
1. Download file `unpackme.flag.py`
2. Buka file dan tambahkan `print(plain)` di baris paling bawah, lalu simpan
3. Buka terminal dan pergi ke __directory file__
4. Ketik `python3 unpackme.flag.py` untuk menjalankan file
5. Input password secara random
6. FLAG DIPEROLEH

![PICO1](https://user-images.githubusercontent.com/92077284/160292135-6d160061-24b0-4186-84e8-e1e37a2d5208.png)
![PICO2](https://user-images.githubusercontent.com/92077284/160292137-90b98a05-70c7-4458-88ed-6f059037325e.png)

**Flag**  
`picoCTF{175_chr157m45_616d21a3}`


## bloat.py

**Description**  
Can you get the flag?  
Run this [Python program]() in the same directory as this [encrypted flag]()

**Solution [INA]**  

**Flag**  
``


## Fresh Java

**Description**  
Can you get the flag?  
Reverse engineer this [Java program]()

**Hints 1**  
Use a decompiler for Java!

**Solution [INA]**  

**Flag**  
``


## Bbbbloat

**Description**  
Can you get the flag?  
Reverse engineer this [binary]()

**Solution [INA]**  

**Flag**  
``


## unpackme

**Description**  
Can you get the flag?
Reverse engineer this [binary]()

**Hints 1**  
What is UPX?

**Solution [INA]**  

**Flag**  
``


# Cryptography
## file-run1
