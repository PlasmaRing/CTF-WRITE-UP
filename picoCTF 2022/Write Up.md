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
| 7  | bloat.py | Reverse Engineering | 200 | picoCTF{d30bfu5c4710n_f7w_e9e38c27}
| 8  | Fresh Java | Reverse Engineering | 200 | picoCTF{700l1ng_r3qu1r3d_0c3de6a4}
| 9  | Bbbbloat | Reverse Engineering | 300 | picoCTF{cu7_7h3_bl047_cbc074c0}
| 10 | unpackme | Reverse Engineering | 300 | picoCTF{up><_m3_f7w_a6870b23}
| 11 | basic-mod1 | Cryptography | 100 | 
| 12 | basic-mod2 | Cryptography | 100 | 
| 13 | credstuff | Cryptography | 100 | picoCTF{C7r1F_54V35_71M3}
| 14 | morse-code | Cryptography | 100 | picoCTF{wh47_h47h_90d_w20u9h7}
| 15 | rail-fence | Cryptography | 100 | picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_318F0948}
| 16 | substitution0 | Cryptography | 100 | picoCTF{5UB5717U710N_3V0LU710N_F96A338E}
| 17 | substitution1 | Cryptography | 100 | picoCTF{FR3QU3NCY_4774CK5_4R3_C001_3645BEC6}
| 18 | substitution2 | Cryptography | 100 | picoCTF{N6R4M_4N41Y515_15_73D10U5_C823D467}
| 19 | transposition-trial | Cryptography | 100 | picoCTF{7R4N5P051N6_15_3XP3N51V3_58410214}
| 20 | Vigenere | Cryptography | 100 | picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_0df54reb}
| 21 | diffie-hellman | Cryptography | 200 | picoCTF{C4354R_C1PH3R_15_4_817_0U7D473D_7609EC61}
| 22 | Enhance! | Forensics | 100 | picoCTF{3nh4nc3d_6ae42bba}
| 23 | Lookey here | Forensics | 100 | picoCTF{gr3p_15_@w3s0m3_c91a291d}
| 24 | Packets Primer | Forensics | 100 | picoCTF{p4ck37_5h4rk_2edd7e58}
| 25 | Redaction gone wrong | Forensics | 100 | picoCTF{C4n_Y0u_S33_m3_fully}
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
Run this [Python program](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/9ac796a26646b2403c26b1ad7809177f677f2278/picoCTF%202022/FILE/bloat/bloat.flag.py) in the same directory as this [encrypted flag](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/9ac796a26646b2403c26b1ad7809177f677f2278/picoCTF%202022/FILE/bloat/flag.txt.enc)

**Solution [INA]**  
1. Download kedua file dan masukan kedua file di folder yang sama
2. Buka file `bloat.flag.py`
3. Tambahkan `print(a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68])` agar mendapatkan __password__
4. Buka terminal dan pergi ke __directory file__
5. Ketik `python3 bloat.flag.py` untuk menjalankan file
6. Didapati __password__ adalah `happychance`
7. Input password: `happychance`
8. FLAG DIPEROLEH

![PICO1](https://user-images.githubusercontent.com/92077284/160359157-2c4fc768-7b61-45c5-bc30-86106b61523b.png)
![PICO2](https://user-images.githubusercontent.com/92077284/160359163-c9f85184-f802-4aea-8128-59f9f50cd0bf.png)

**Flag**  
`picoCTF{d30bfu5c4710n_f7w_e9e38c27}`


## Fresh Java

**Description**  
Can you get the flag?  
Reverse engineer this [Java program](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/9ac796a26646b2403c26b1ad7809177f677f2278/picoCTF%202022/FILE/KeygenMe.class)

**Hints 1**  
Use a decompiler for Java!

**Solution [INA]**  
1. Download file
2. Gunakan online java decompiler http://www.javadecompilers.com/
3. Masukan file, dan urutkan `nextLine.charAt(0) sampai nextLine.charAt(33)`
4. FLAG DIPEROLEH

**Flag**  
`picoCTF{700l1ng_r3qu1r3d_0c3de6a4}`


## Bbbbloat

**Description**  
Can you get the flag?  
Reverse engineer this [binary](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/9ac796a26646b2403c26b1ad7809177f677f2278/picoCTF%202022/FILE/bbbbloat)

**Solution [INA]**  
1. Download file
2. Buka file menggunakan IDA
3. Pergi ke `main`
4. KLik F5 untuk __decompile__
5. __Secret Number__ ditemukan: `549255`
6. Buka terminal, dan pergi ke __directory file__
7. Ketik `chmod +x bbbbloat` untuk membuat file __executable__
8. Ketik `./bbbbloat` untuk menjalankan file
9. Masukan __Secret Number__ `549255`
10. FLAG DIPEROLEH

![PICO1](https://user-images.githubusercontent.com/92077284/160372597-5ccef086-d8c2-4fe8-beb4-a28610db0088.png)
![PICO2](https://user-images.githubusercontent.com/92077284/160372606-01d0447d-1f03-435b-a53c-2a08e21cfc30.png)
![PICO3](https://user-images.githubusercontent.com/92077284/160372612-df5ff57b-4e51-4b98-834c-0c01b24b7f70.png)

**Flag**  
`picoCTF{cu7_7h3_bl047_cbc074c0}`


## unpackme

**Description**  
Can you get the flag?  
Reverse engineer this [binary](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/9ac796a26646b2403c26b1ad7809177f677f2278/picoCTF%202022/FILE/unpackme-upx)

**Hints 1**  
What is UPX?

**Solution [INA]**  
1. Download file
2. Cek apakah file `unpackme-upx` dalam status __packed__ menggunakan tool seperti __Detect It Easy__
3. Buka terminal, dan pergi ke __directory file__
4. __unpack__ file dengan mengetikan `upx -d unpackme-upx -o unpackme-unpack `
5. Cek apakah file `unpackme-unpack` berhasil di __unpack__
6. Buka file `unpackme-unpack` menggunakan IDA
7. Pergi ke `main`
8. KLik F5 untuk __decompile__
9. __Secret Number__ ditemukan: `754635`
10. Buka terminal, dan pergi ke __directory file__
11. Ketik `chmod +x unpackme-upx` untuk membuat file __executable__
12. Ketik `./unpackme-upx` untuk menjalankan file
13. Masukan __Secret Number__ `754635`
14. FLAG DIPEROLEH

![PICO1](https://user-images.githubusercontent.com/92077284/160375948-f0677ea3-1887-4e6b-95f6-246b6869d41e.png)
![PICO2](https://user-images.githubusercontent.com/92077284/160375953-871b3f62-084d-4de3-b1a8-007385d58d45.png)
![PICO3](https://user-images.githubusercontent.com/92077284/160375960-44273c7a-247b-4687-ad8d-e8013ff2416a.png)
![PICO4](https://user-images.githubusercontent.com/92077284/160375969-25b2803f-8d62-4578-bc51-20c555b5ec6f.png)
![PICO5](https://user-images.githubusercontent.com/92077284/160375976-1fd629cb-b192-4dfe-b947-5a3bec824791.png)
![PICO6](https://user-images.githubusercontent.com/92077284/160375980-8cd62bcc-5ea5-48f6-bb04-e576ed47930d.png)


**Flag**  
`picoCTF{up><_m3_f7w_a6870b23}`


# Cryptography
## basic-mod1

**Description**  
We found this weird message being passed around on the servers, we think we have a working decrpytion scheme.  
Download the message here.  
message: `387 248 131 272 373 221 161 110 91 359 390 50 225 184 223 137 225 327 42 179 220 365 `  
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.  
Wrap your decrypted message in the picoCTF flag format (i.e. __picoCTF{decrypted_message}__)

**Hints 1**  
Do you know what mod 37 means?

**Hints 2**  
mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.

**Solution [INA]**  
1. Gunakan __Online Modulo Cipher Decoder__ seperti: https://www.dcode.fr/modulo-cipher
2. Input **message** dan **37** sebagai modulonya
3. Didapati hasil: `17 26 20 13 3 36 13 36 17 26 20 13 3 36 1 26 3 31 5 31 35 32`
4. Ubah **string angka** menjadi **string** sesuai ketentuan pada deskripsi
5. Didapati hasil: 
6. FLAG DIPEROLEH

**Flag**  


## basic-mod2

**Description**  
A new modular challenge!  
Download the message here.  
message: `145 126 356 272 98 378 395 352 392 215 446 168 180 359 51 190 404 209 185 115 363 431 103 `  
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.  
Wrap your decrypted message in the picoCTF flag format (i.e. __picoCTF{decrypted_message}__)

**Hints 1**  
Do you know what the modular inverse is?

**Hints 2**  
The inverse modulo z of x is the number, y that when multiplied by x is 1 modulo z

**Hints 3**  
It's recommended to use a tool to find the modular inverses

**Solution [INA]**  
1. Gunakan __Online Modulo Cipher Decoder__ seperti: https://www.dcode.fr/modulo-cipher
2. Input **message** dan **41** sebagai modulonya
3. Didapati hasil: `22 3 28 26 16 9 26 24 23 10 36 4 16 31 10 26 35 4 21 33 35 21 21`
4. **Invers modulo 41** pada setiap angka
5. Didapati hasil: 
6. Ubah **string angka** menjadi **string** sesuai ketentuan pada deskripsi
7. Didapati hasil: 
8. FLAG DIPEROLEH

**Flag**  


## credstuff

**Description**  
We found a leak of a blackmarket website's login credentials. Can you find the password of the user **cultiris** and successfully decrypt it?  
Download the leak [here](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/7a4936ddf23a7f4b457db0f39cc1144166b85984/picoCTF%202022/FILE/leak.tar)  
The first user in **usernames.txt** corresponds to the first password in **passwords.txt**. The second user corresponds to the second password, and so on.  

**Hints 1**  
Maybe other passwords will have hints about the leak?

**Solution [INA]**  
1. Download file, dan buka kedua file
2. Ditemukan `cultiris` berada di line ke **378**
3. Ditemukan password di line **378** pada file `passwords.txt` adalah `cvpbPGS{P7e1S_54I35_71Z3}`
4. Menurut hint, terdapat hint pada file `passwords.txt`
5. Ditemukan hint berupa `pICo7rYpiCoU51N6PicOr0t13` setelah mencari kata kunci `pico`
6. Decode `cvpbPGS{P7e1S_54I35_71Z3}` menggunakan **Online ROT13 Decoder** seperti https://rot13.com/
7. FLAG DIPEROLEH

![PICO1](https://user-images.githubusercontent.com/92077284/160408903-b56a467a-856b-4a4a-b3f8-d92e2cbf3ac1.png)
![PICO2](https://user-images.githubusercontent.com/92077284/160408914-a18d4c82-5f0a-4a0d-98b5-efdb573cc7d8.png)

**Flag**  
`picoCTF{C7r1F_54V35_71M3}`

## morse-code

**Description**  
Morse code is well known. Can you decrypt this?  
Download the file [here](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/fc90db01513230b9ca77ef6e7c4bbbafccdcaff3/picoCTF%202022/FILE/morse_chal.wav)  
Wrap your answer with picoCTF{}, put underscores in place of pauses, and use all lowercase.

**Hints 1**
Audacity is a really good program to analyze morse code audio.

**Solution [INA]**  
1. Download file
2. Buka file menggunakan **Audacity**
3. Morse dapat terbaca jelas dan dapat diterjemahkan menggunakan **Online Morse Code Translator** seperti https://morsecode.world/international/translator.html
4. Didapati hasil: `WH47 H47H 90D W20U9H7`
5. Ubah menjadi format flag: `picoCTF{wh47_h47h_90d_w20u9h7}`
6. FLAG DIPEROLEH

![image](https://user-images.githubusercontent.com/92077284/160412423-3e1a4917-2a1e-454a-b6f2-d80e27c48389.png)
![image](https://user-images.githubusercontent.com/92077284/160412498-ff8fbf11-0ab0-4432-ac63-b6a46afdac6b.png)

**Flag**  
`picoCTF{wh47_h47h_90d_w20u9h7}`

## rail-fence

**Description**  
A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it?  
Download the message here.  
message: `Ta _7N6D34hlg:W3D_H3C31N__198ef sHR053F38N43D80 i33___NF`  
Put the decoded message in the picoCTF flag format, picoCTF{decoded_message}. 

**Hints 1**  
Once you've understood how the cipher works, it's best to draw it out yourself on paper

**Solution [INA]**  
1. Download file berisi `Ta _7N6D34hlg:W3D_H3C31N__198ef sHR053F38N43D80 i33___NF`
2. Decode menggunakan **Online Rail Fence Cipher Decoder** seperti: https://www.boxentriq.com/code-breaking/rail-fence-cipher
3. Set rail ke 4, Ofset ke 0
4. FLAG DIPEROLEH

**Flag**  
`picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_318F0948}`

## substitution0

**Description**  
A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?  
Download the message here.  
message: 
```html 
PJFRENTZHOMQKLAIUVSWCYDXGB 

Zevecial Qetvplr pvase, dhwz p tvpye plr swpweqg phv, plr jvactzw ke wze jeewqe
nvak p tqpss fpse hl dzhfz hw dps elfqaser. Hw dps p jepcwhncq sfpvpjpecs, plr, pw
wzpw whke, clmladl wa lpwcvpqhsws—an facvse p tvepw ivhbe hl p sfhelwhnhf iahlw
an yhed. Wzeve deve wda vaclr jqpfm siaws lepv ale exwvekhwg an wze jpfm, plr p
qalt ale lepv wze awzev. Wze sfpqes deve exfeerhltqg zpvr plr tqassg, dhwz pqq wze
piiepvplfe an jcvlhszer taqr. Wze dehtzw an wze hlsefw dps yevg vekpvmpjqe, plr,
wpmhlt pqq wzhlts hlwa falshrevpwhal, H facqr zpvrqg jqpke Ocihwev nav zhs aihlhal
vesiefwhlt hw.

Wze nqpt hs: ihfaFWN{5CJ5717C710L_3Y0QC710L_N96P338E}
```

**Hints 1**  
Try a frequency attack. An online tool might help.

**Solution [INA]**  
1. Download file
2. Decode text menggunakan **Online Subtitution Decoder** seperti: https://www.dcode.fr/monoalphabetic-substitution
3. Setting bahasa menjadi **English** dan **DECRYPT AUTOMATICALLY**
4. Didapati flag: `PICOCTF{5UB5717U710N_3V0LU710N_F96A338E}`
5. Ubah format menjadi: `picoCTF{5UB5717U710N_3V0LU710N_F96A338E}`
6. FLAG DIPEROLEH

![image](https://user-images.githubusercontent.com/92077284/160416406-64464beb-967e-458e-876f-a46830f255f6.png)

**Flag**  
`picoCTF{5UB5717U710N_3V0LU710N_F96A338E}`

## substitution1

**Description**  
A second message has come in the mail, and it seems almost identical to the first one. Maybe the same thing will work again.  
Download the message here.
message: 
```html 
DAFq (qgjwa fjw dkxahwz agz frke) kwz k aoxz jf djbxhazw qzdhwtao djbxzatatjn. Djnazqaknaq kwz xwzqznazs mtag k qza jf dgkrrznezq mgtdg azqa agztw dwzkatltao, azdgntdkr (kns ejjertne) qutrrq, kns xwjyrzb-qjrltne kytrtao. Dgkrrznezq hqhkrro djlzw k nhbyzw jf dkazejwtzq, kns mgzn qjrlzs, zkdg otzrsq k qawtne (dkrrzs k frke) mgtdg tq qhybtaazs aj kn jnrtnz qdjwtne qzwltdz. DAFq kwz k ewzka mko aj rzkwn k mtsz kwwko jf djbxhazw qzdhwtao qutrrq tn k qkfz, rzekr znltwjnbzna, kns kwz gjqazs kns xrkozs yo bkno qzdhwtao ewjhxq kwjhns agz mjwrs fjw fhn kns xwkdatdz. Fjw agtq xwjyrzb, agz frke tq: xtdjDAF{FW3VH3NDO_4774DU5_4W3_D001_3645YZD6}
```

**Hints 1**  
Try a frequency attack

**Hints 2**  
Do the punctuation and the individual words help you make any substitutions?

**Solution [INA]**  
1. Download file
2. Decode text menggunakan **Online Subtitution Decoder** seperti: https://www.dcode.fr/monoalphabetic-substitution
3. Setting bahasa menjadi **English** dan **DECRYPT AUTOMATICALLY**
4. Didapati flag: `PICOCTF{FR3JU3NCY_4774CK5_4R3_C001_3645BEC6}`
5. Sedikit ubah agar kata dan flag lebih sesuai `picoCTF{FR3QU3NCY_4774CK5_4R3_C001_3645BEC6}`
6. FLAG DIPEROLEH

![image](https://user-images.githubusercontent.com/92077284/160417625-c3ed4edb-620a-4885-891a-f10b5988942f.png)

**Flag**  
`picoCTF{FR3QU3NCY_4774CK5_4R3_C001_3645BEC6}`

## substitution2

**Description**  
It seems that another encrypted message has been intercepted. The encryptor seems to have learned their lesson though and now there isn't any punctuation! Can you still crack the cipher?  
Download the message here.
message:
```html
xkjvjjapmxmjcjvnifxkjvdjiijmxneipmkjokphkmykffiyfsulxjvmjylvpxzyfsujxpxpfrmpryiloprhyzejvunxvpfxnrolmyzejvykniijrhjxkjmjyfsujxpxpfrmqfylmuvpsnvpizfrmzmxjsmnosprpmxvnxpfrqlronsjrxnimdkpyknvjcjvzlmjqlinrosnvtjxneijmtpiimkfdjcjvdjejipjcjxkjuvfujvulvufmjfqnkphkmykffiyfsulxjvmjylvpxzyfsujxpxpfrpmrfxfrizxfxjnykcnilneijmtpiimelxnimfxfhjxmxlojrxmprxjvjmxjoprnrojaypxjoneflxyfsulxjvmypjryjojqjrmpcjyfsujxpxpfrmnvjfqxjrinefvpflmnqqnpvmnroyfsjofdrxfvlrrprhykjytipmxmnrojajylxprhyfrqphmyvpuxmfqqjrmjfrxkjfxkjvknropmkjncpizqfylmjofrjauifvnxpfrnropsuvfcpmnxpfrnrofqxjrknmjijsjrxmfquinzdjejipjcjnyfsujxpxpfrxflykprhfrxkjfqqjrmpcjjijsjrxmfqyfsulxjvmjylvpxzpmxkjvjqfvjnejxxjvcjkpyijqfvxjykjcnrhjipmsxfmxlojrxmprnsjvpynrkphkmykffimqlvxkjvdjejipjcjxknxnrlrojvmxnroprhfqfqqjrmpcjxjykrpgljmpmjmmjrxpniqfvsflrxprhnrjqqjyxpcjojqjrmjnroxknxxkjxffimnroyfrqphlvnxpfrqfylmjryflrxjvjoprojqjrmpcjyfsujxpxpfrmofjmrfxijnomxlojrxmxftrfdxkjpvjrjsznmjqqjyxpcjiznmxjnykprhxkjsxfnyxpcjizxkprtiptjnrnxxnytjvupyfyxqpmnrfqqjrmpcjizfvpjrxjokphkmykffiyfsulxjvmjylvpxzyfsujxpxpfrxknxmjjtmxfhjrjvnxjprxjvjmxpryfsulxjvmypjryjnsfrhkphkmykffijvmxjnykprhxkjsjrflhkneflxyfsulxjvmjylvpxzxfupgljxkjpvylvpfmpxzsfxpcnxprhxkjsxfjauifvjfrxkjpvfdrnrojrneiprhxkjsxfejxxjvojqjroxkjpvsnykprjmxkjqinhpmupyfYXQ{R6V4S_4R41Z515_15_73O10L5_Y823O467}
```

**Hints 1**  
Try refining your frequency attack, maybe analyzing groups of letters would improve your results?

**Solution [INA]**  
1. Download file
2. Decode text menggunakan **Online Subtitution Decoder** seperti: https://www.dcode.fr/monoalphabetic-substitution
3. Setting bahasa menjadi **English** dan **DECRYPT AUTOMATICALLY**
4. Didapati flag: `PICOCTF{N6R4M_4N41Y515_15_73D10U5_C823D467}`
5. Ubah format menjadi: `picoCTF{N6R4M_4N41Y515_15_73D10U5_C823D467}`
6. FLAG DIPEROLEH

![image](https://user-images.githubusercontent.com/92077284/160418094-c97198d3-bb6e-4bae-8599-0224b523aab0.png)

**Flag**  
`picoCTF{N6R4M_4N41Y515_15_73D10U5_C823D467}`

## transposition-trial

**Description**  
Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.  
Download the corrupted message here.  
message: `heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V8450214}1`

**Hints 1**  
Split the message up into blocks of 3 and see how the first block is scrambled

**Solution [INA]**  
1. Download file yang berisi text: `heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V8450214}1`
2. Pisahkan text dengan char, tiap char ke3
```html
 heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V8450214}1
   T     a  i  p  o  F  R  5  5  6  5  X  N  V  5  1  1
```
3. Pindahkan char ke3 ke char sebelumnya(kiri)
```html
 heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V8450214}1
   T     a  i  p  o  F  R  5  5  6  5  X  N  V  5  1  1
The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_58410214} 
```
4. FLAG DIPEROLEH

**Flag**  
`picoCTF{7R4N5P051N6_15_3XP3N51V3_58410214}`

## Vigenere

**Description**  
Can you decrypt this message?  
Decrypt this message using this key "CYLAB".  
message: `rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_0fd54cec}`

**Hints 1**  
https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

**Solution [INA]**  
1. Download file yang berisi text: `rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_0fd54cec}`
2. Decode menggunakan **Online Vignere Cipher Decoder** seperti: https://www.dcode.fr/vigenere-cipher
3. Masukan Key: `CYLAB` lalu **DECRYPT**
4. FLAG DIPEROLEH

![image](https://user-images.githubusercontent.com/92077284/160421654-a3acd498-4dea-4c21-a8a9-e03447ee4e07.png)

**Flag**  
`picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_0df54reb}`

## diffie-hellman

**Description**  
Alice and Bob wanted to exchange information secretly. The two of them agreed to use the Diffie-Hellman key exchange algorithm, using p = 13 and g = 5. They both chose numbers secretly where Alice chose 7 and Bob chose 3. Then, Alice sent Bob some encoded text (with both letters and digits) using the generated key as the shift amount for a Caesar cipher over the alphabet and the decimal digits. Can you figure out the contents of the message?  
Download the message here.  
message: `H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_CB5EJHB6`  
Wrap your decrypted message in the picoCTF flag format like: **picoCTF{decrypted_message}**  

**Hints 1**  
Diffie-Hellman key exchange is a well known algorithm for generating keys, try looking up how the secret key is generated

**Hints 2**  
For your Caesar shift amount, try forwards and backwards.

**Solution [INA]**  
1. Download file yang berisi text: `H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_CB5EJHB6`
2. **Generate key** dengan menggunakan **Online Diffie Hellman Key Exchange Calculator** seperti: https://www.irongeek.com/diffie-hellman.php?
3. Masukan p = 13, g = 5, Alice = 7, dan Bob = 3, lalu **submit**
4. Didapati key = **5**
![image](https://user-images.githubusercontent.com/92077284/160423189-b8cfb90b-3689-4682-ada4-35dcc62e53f2.png)
5. Gunakan **Online Caesar Cipher Decoder**, lalu masukan **5** sebagai key seperti: https://www.boxentriq.com/code-breaking/caesar-cipher
![image](https://user-images.githubusercontent.com/92077284/160423955-a752bd1c-fe50-4c60-bde6-fba03fbbb9e3.png)
6. Didapati hasil: `C98V9R_C6PH8R_6V_9_Y6X_5UXD9X8D_XW5ZECW6`
7. Sempurnakan hasil, karena terdapat angka yang tidak ikut berubah dan beberapa char yang seharusnya berubah menjadi angka
8. Hasil berubah menjadi: `C4354R_C1PH3R_15_4_817_0U7D473D_7609EC61`
9. FLAG DIPEROLEH

**Flag**  
`picoCTF{C4354R_C1PH3R_15_4_817_0U7D473D_7609EC61}`


# Forensics
## Enhance!

**Description**  
Download this image file and find the flag.  
[Download image file](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/8ec682f123788218df54eef0e8f29ccbd318d637/picoCTF%202022/FILE/drawing.flag.svg)

**Solution [INA]**  
1. Download file `drawing.flag.svg`
2. Buka file menggunakan **VS CODE**
![image](https://user-images.githubusercontent.com/92077284/160430459-58e1e8ee-8f08-49ae-affe-8fff71f9bb3f.png)
3. Susun char dan text yang ada diantara `tspan`
4. Text dapat disusun menjadi: `picoCTF{3nh4nc3d_6ae42bba}`
5. FLAG DIPEROLEH

**Flag**  
`picoCTF{3nh4nc3d_6ae42bba}`


## Lookey here

**Description**  
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.  
Download the data [here](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/22a311e69d0848c226484c492e76ad19fb505317/picoCTF%202022/FILE/anthem.flag.txt)

**Hints 1**  
Download the file and search for the flag based on the known prefix.

**Solution [INA]**  
1. Download file `anthem.flag.txt`
2. Buka file menggunakan **VS CODE**
3. Cari kata kunci **pico**
4. FLAG DIPEROLEH

![image](https://user-images.githubusercontent.com/92077284/160431787-f7573ef5-5ed9-4e6b-9ada-01b7d3271698.png)

**Flag**  
`picoCTF{gr3p_15_@w3s0m3_c91a291d}`


## Packets Primer

**Description**  
Download the packet capture file and use packet analysis software to find the flag.  
Download [packet capture](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/701efc7132eb0c0fb4d77c4af2c966d86d4d35f7/picoCTF%202022/FILE/network-dump.flag.pcap)

**Hints 1**  
Wireshark, if you can install and use it, is probably the most beginner friendly packet analysis software product.

**Solution [INA]**  
1. Download file `network-dump.flag.pcap`
2. Buka file menggunakan **Wireshark**
3. Cari flag pada **tab Wireshark**
4. FLAG DIPEROLEH

![PICO1](https://user-images.githubusercontent.com/92077284/160433643-b4246067-1700-48d3-9060-91873b472c58.png)

**Flag**  
`picoCTF{p4ck37_5h4rk_2edd7e58}`


## Redaction gone wrong

**Description**  
Now you DON’T see me.  
This [report](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/d0af4457acca51a7514e95ef8e6d97658aff7425/picoCTF%202022/FILE/Financial_Report_for_ABC_Labs.pdf) has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?

**Hints 1**  
How can you be sure of the redaction?

**Solution [INA]**  
1. Download file `Financial_Report_for_ABC_Labs`
2. **Blok** semua text pada pdf, lalu **Copy**
3. **Paste** text ke **notepad**
4. FLAG DIPEROLEH

![image](https://user-images.githubusercontent.com/92077284/160436104-c7b5656e-1bb1-4f16-885b-d3270461d902.png)
![image](https://user-images.githubusercontent.com/92077284/160436187-cd0c260d-e304-4eb8-bab2-57a7c981f758.png)

**Flag**  
`picoCTF{C4n_Y0u_S33_m3_fully}`


# Web Exploitation
## 

**Description**  


**Hints 1**  


**Hints 2**  


**Solution [INA]**  


**Flag**  
