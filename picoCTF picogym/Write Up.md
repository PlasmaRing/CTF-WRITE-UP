# picoCTF picogym
WEB : `https://picoctf.org/`  

## Overview

| No | Title               | Date              | Category                   | Flag                 | Points
|----|---------------------|-------------------|----------------------------|----------------------|------------
| 1  | [Transformation](#transformation) | 19/06/2022 | Reverse Engineering | picoCTF{16_bits_inst34d_of_8_d52c6b93} | 20
| 2  | [keygenme-py](#keygenme-py) | 21/06/2022 | Reverse Engineering | picoCTF{1n_7h3_I<3y_of_ac73dc29} | 30
| 3  | [crackme-py](#crackme-py) | 04/09/2022 | Reverse Engineering | picoCTF{1I\/I_4_p34I\Iut_f3bc410e} | 30
| 4  | [ARMssembly 0](#armssembly-0) | 05/09/2022 | Reverse Engineering | picoCTF{5ee79c2b} | 40
| 5  | [vault-door-training](#vault-door-training) | 05/09/2022 | Reverse Engineering | picoCTF{w4rm1ng_Up_w1tH_jAv4_3808d338b46} | 50
| 6  | [speeds and feeds](#speeds-and-feeds) | 05/09/2022 | Reverse Engineering | picoCTF{num3r1cal_c0ntr0l_775375c7} | 50
| 7  | [Shop](#shop) | 07/09/2022 | Reverse Engineering | picoCTF{b4d_brogrammer_3da34a8f} | 50
| 8  | [ARMssembly 1](#armssembly-1) |  | Reverse Engineering | picoCTF{} | 70
| 9  | [ARMssembly 2](#armssembly-2) |  | Reverse Engineering | picoCTF{} | 90
| 10  | [vault-door-1](#vault-door-1) | 08/09/2022 | Reverse Engineering | picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_f6daf4} | 100
| 11  | [Hurry up! Wait!](#hurry-up!-wait!) | 08/09/2022 | Reverse Engineering | picoCTF{d15a5m_ftw_a82650a} | 100

# Reverse Engineering 
## Transformation 

**Description**  
I wonder what this really is... [enc](https://mercury.picoctf.net/static/a757282979af14ab5ed74f0ed5e2ca95/enc) ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

**Hints 1**  
You may find some decoders online

**Solution [INA]**  
1.  Analisa file `enc` yang berisi: `灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽`
2.  Gunakan online decoder seperti CyberChef
3.  Gunakan Magic & Intensive Mode pada Cyber Chef
![image](https://user-images.githubusercontent.com/92077284/174487475-945bbb78-1445-4980-a895-335a348e2a82.png)  
4.  FLAG DIPEROLEH 

**Flag**  
`picoCTF{16_bits_inst34d_of_8_d52c6b93}`

## keygenme-py
**Description**  
[keygenme-trial.py](https://mercury.picoctf.net/static/9055e7d35f5f4646338a1734aea0dda5/keygenme-trial.py)

**Solution [INA]**  
1.  Analisa file `keygenme-trial.py`
2.  Diketahui bahwa format flag : `"picoCTF{1n_7h3_|<3y_of_" + "xxxxxxxx" + "}"` __*xxxxxxxx perlu dicari__

![image](https://user-images.githubusercontent.com/92077284/174823182-a3ac3156-ce7d-4a9b-9300-7971452346e6.png)

3.  Pada file ini terdapat bagian `def check_key(key, username_trial):` dimana pada file ini akan memeriksa input string  
    a. panjang string harus sama dengan format flag.  
    b. pada bagian `key_part_dynamic1_trial` akan dicek satu persatu sesuai dengan script hashingnya.  
    Semua validasi pada `def check_key(key, username_trial):` harus sesuai  
    
![image](https://user-images.githubusercontent.com/92077284/174829860-2f0c35bb-705e-4d5a-995c-f7cab520d588.png)

4.  Untuk mengetahui isi dari `key_part_dynamic1_trial` maka dibuat file [keygenpico.py]()  

![image](https://user-images.githubusercontent.com/92077284/174828283-eea1d8c1-ab50-4130-890d-7eadbc368cf9.png)

5.  Didapati hasil dari file `keygenpico.py` adalah __ac73dc29__, gabungkan dengan format flag awal
6.  FLAG DIPEROLEH

**Flag**  
`picoCTF{1n_7h3_|<3y_of_ac73dc29}`

## crackme-py

**Description**  
[crackme.py](https://mercury.picoctf.net/static/b7cabaae6561256c50728d3515db3058/crackme.py)

**Solution [INA]**  
1.  Buka file `crackme-py`
2.  Diketahui ada string yang dienkripsi dengan ROT47   
![image](https://user-images.githubusercontent.com/92077284/188305187-1d39eb48-27ef-4add-8018-c1d17922215d.png)
3.  Decode string dengan menambahkan `decode_secret(bezos_cc_secret)` pada file `crackme-py`   
![image](https://user-images.githubusercontent.com/92077284/188305299-f00e7a53-d4f0-46f9-8dd4-d25241c01208.png)
4.  Jalankan program   
![image](https://user-images.githubusercontent.com/92077284/188305281-bee0ae1d-8e50-4ad9-8d39-0080d3b8c1a9.png)
5.  FLAG DIPEROLEH

**Flag**  
`picoCTF{1|\/|_4_p34|\|ut_f3bc410e}`

## ARMssembly 0

**Description**  
What integer does this program print with arguments 266134863 and 1592237099? File: [chall.S](https://mercury.picoctf.net/static/104d6022bcea93f53083aeb61b134e8b/chall.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

**Hints 1**  
Simple compare

**Solution [INA]**  
1.  Buka file `chall.S` melalui terminal dengan mengetikan `vi chall.S`
2.  Analisa file bagian **main**, sesuai dengan deskripsi soal, fokus pada apa yang akan di **print** program
![image](https://user-images.githubusercontent.com/92077284/188314780-c6ba8575-d500-42a6-a327-649ac6a6d358.png)
3.  Program melakukan load dan menggubah ASCII to Integer **[atoi]**, value yang diload adalah `266134863` dan `1592237099`
![image](https://user-images.githubusercontent.com/92077284/188421396-54ea3697-8a07-4c54-933a-b7500d4e1f27.png)
![image](https://user-images.githubusercontent.com/92077284/188421484-b3c4dda9-f6ce-473a-84bd-474b6e703f7d.png)
4.  Lalu **func1** dipanggil, dimana **func1** akan melakukan compare **[cmp]** pada 2 value tersebut. Disini `w1 =  266134863` dan `w0 = 1592237099`.  
![image](https://user-images.githubusercontent.com/92077284/188421997-5445acb1-bb71-46ae-b843-3b2db993e036.png)
5.  **[bls]** dapat diartikan sebagai **lower or same**, karena w1 lebih kecil dari w0 maka program memanggil **.L2** dan melakukan load value **w0**
6.  Setelah itu kembali lagi ke **main**, dimana setelah itu akan memanggil **.LC0** yang akan melakukan print value
![image](https://user-images.githubusercontent.com/92077284/188424487-a27cbc37-84dc-4d4f-9609-cd645589b2e9.png)
![image](https://user-images.githubusercontent.com/92077284/188424525-db6d10bb-3d51-48de-be96-cf5c60366724.png)
7.  Karena value yang akan di print dalam bentuk hex, maka `1592237099` diubah menjadi `0x5ee79c2b`, lalu rangkai flag sesuai ketentuan deskripsi
8.  FLAG DIPEROLEH

**Flag**  
`picoCTF{5ee79c2b}`

## vault-door-training

**Description**  
Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](https://jupiter.challenges.picoctf.org/static/03c960ddcc761e6f7d1722d8e6212db3/VaultDoorTraining.java)  

**Hints 1**  
The password is revealed in the program's source code.

**Solution [INA]**  
1.  Buka fie `VaultDoorTraining.java` menggunakan **vscode**
2.  Analisa source code dan susun flagnya  
![image](https://user-images.githubusercontent.com/92077284/188442331-9877126a-a51e-4351-a77f-ea6685d9f801.png)
3.  FLAG DIPEROLEH

**Flag**  
`picoCTF{w4rm1ng_Up_w1tH_jAv4_3808d338b46}`

## speeds and feeds

**Description**  
There is something on my shop network running at **nc mercury.picoctf.net 53740**, but I can't tell what it is. Can you?

**Hints 1**  
What language does a CNC machine use?

**Solution [INA]**  
1.  Jalankan `nc mercury.picoctf.net 53740` pada terminal linux
2.  Diketahui bahwa disini ditemukan source code yang biasa digunakan oleh mesin CNC, yaitu `G CODE`
3.  Copy source code, lalu paste pada **gcode online compiler** seperti https://nraynaud.github.io/webgcode/  
![image](https://user-images.githubusercontent.com/92077284/188488182-6d8fa54c-0464-40fc-92f3-b2b45c909b66.png)
4.  FLAG DIPEROLEH

**Flag**  
`picoCTF{num3r1cal_c0ntr0l_775375c7}`

## Shop

**Description**  
Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: [source](https://mercury.picoctf.net/static/73724c199e55e6c056bb00e7bbfdfb38/source). The shop is open for business at **nc mercury.picoctf.net 10337**.

**Hints 1**  
Always check edge cases when programming

**Solution [INA]**  
1.  Download source file untuk melakukan analisis
2.  Diketahui bahwa memerlukan **100 coins** untuk melakukan pembelian flag  
![image](https://user-images.githubusercontent.com/92077284/188860158-bdcc9e4c-693a-499d-9a7c-1006404d5ebf.png)  
3.  Analisa source file menggunakan *decompiler tools* seperti IDA PRO
4.  Didapati bahwa terdapat celah test case yang dapat menambah coins. Hal ini dapat ditemukan pada bagian **main_menu**  
![image](https://user-images.githubusercontent.com/92077284/188861371-639c3acd-bb27-4f47-a694-4daee5f8ec4d.png)  
5.  Karena disini tertulis `v15 = wallet - *_num * inv.array[v14].price;` maka disimpulkan dapat membeli dengan jumlah minus. *Note : minus * minus = plus*
6.  Disini buka terminal lalu ketik **nc mercury.picoctf.net 10337**, pilih **Quiet Quiches atau Average Apple**, lalu masukin input negatif sebagai jumlahnya  
![image](https://user-images.githubusercontent.com/92077284/188862186-93f3543d-7a6c-46c9-a291-7b46a7ab4212.png)  
7.  Karena coin sudah mencukupi maka kita dapat membeli **Fruitful Flag**  
![image](https://user-images.githubusercontent.com/92077284/188862469-dd6f96cf-e4f1-4f34-b823-6293dd3ec5c8.png)  
8.  Ubah ASCII to TEXT
9.  FLAG DIPEROLEH

**Flag**  
`picoCTF{b4d_brogrammer_3da34a8f}`

## vault-door-1

**Description**  
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](https://jupiter.challenges.picoctf.org/static/87e103a8db01087de9ccf5a7a022ddf8/VaultDoor1.java)

**Hints 1**  
Look up the charAt() method online.

**Solution [INA]**  
1.  Download file `VaultDoor1.java` lalu buka file
2.  Pada source file terdapat bagian **flag checker**
3.  Susun urutan flag yang masih teracak  
![image](https://user-images.githubusercontent.com/92077284/189050827-8775bda1-e44b-408f-b57e-d6c42fba96c8.png)
4.  FLAG DIPEROLEH

**Flag**  
`picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_f6daf4}`

## Hurry up! Wait!

**Description**  
[svchost.exe](https://mercury.picoctf.net/static/18afff80df59ffe13188a4907089ec8d/svchost.exe)

**Solution [INA]**  
1.  Download file `svchost.exe` lalu masukan file ke **decompiler** seperti IDA
2.  Pergi menuju **main**  
![image](https://user-images.githubusercontent.com/92077284/189061562-51bc529c-fad1-4a47-8353-6f16d62c1d86.png)
3.  Pergi menuju **sub_298A()**  
![image](https://user-images.githubusercontent.com/92077284/189061744-1372a61e-3c90-4771-b4e0-3a73842f23ef.png)
4.  Klik salah satu **sub**, seperti pada contoh **sub_2616()**  
![image](https://user-images.githubusercontent.com/92077284/189061924-f5afd259-600e-4d9a-99c6-6f62b1626f8e.png)
5.  Klik **&unk_2CD8**  
![image](https://user-images.githubusercontent.com/92077284/189062138-b9b5ca0d-142a-40ba-8765-101f33b941b9.png)
6.  Diketahui bahwa sub ini menyimpan huruf `p`, sesuai dengan format flag pertama: `picoCTF{}`
7.  Lakukan pada sub lainnya
8.  FLAG DIPEROLEH

**Flag**  
`picoCTF{d15a5m_ftw_a82650a}`

## gogo

**Description**  
Hmmm this is a weird file... [enter_password](https://mercury.picoctf.net/static/de0c0cd34d8d819b915dc37081372c7a/enter_password). There is a instance of the service running at **mercury.picoctf.net:47423**.

**Hints 1**  
use go tool objdump or ghidra

**Solution [INA]**  
1.  Download file `enter_password` lalu masukan file ke **decompiler** seperti IDA PRO
2.  Pergi ke bagian **main_checkPassword**  
![image](https://user-images.githubusercontent.com/92077284/189170099-ac8f27aa-8309-46be-80ac-0fa1fca956a0.png)
3.  Dianalisa bahwa input string berjumlah **32** dan disini terdapat perintah **XOR** `(key[v1] ^ input.str[v1]) == v4[v1]`
4.  Masuk ke text view agar mengetahui nilai hex keduanya  
![image](https://user-images.githubusercontent.com/92077284/189170965-f583a68d-2417-4b76-9cc6-c729f8b2f11f.png)  
![image](https://user-images.githubusercontent.com/92077284/189171093-16f6a55c-7e8d-4d50-9d42-8db8fe600e1d.png)
5.  Masuk ke terminal dengan command `gdb ./enter_password`, lalu buat breakpoints di **0x80d4b2d** dengan command `break *0x80d4b2d` agar nantinya dapat membaca hex value di `[esp+eax+44h+key]` dan `[esp+eax+44h+var_20]`
6.  Ketik `run` lalu masukan input asal sebanyak 32 digit  
![image](https://user-images.githubusercontent.com/92077284/189173403-b4cfc72a-cb09-4117-b3de-eafe2387e39b.png)
![image](https://user-images.githubusercontent.com/92077284/189173669-d617f25a-cc6b-4755-ba4d-7a23b4151cb0.png)
7.  Ketik `hexdump byte $esp+0x4` dan `hexdump byte $esp+0x24`untuk mendapatkan **key dan hex value satunya**
![image](https://user-images.githubusercontent.com/92077284/189174082-3283df5a-c6d6-42d3-80bb-ca153f49f754.png)
![image](https://user-images.githubusercontent.com/92077284/189175229-6d302815-7ab2-4503-856d-361898f33f55.png)
8.  Didapati key(ASCII): `861836f13e3d627dfa375bdb8389214e` dan  hex value satunya: `4a53475d414503545d025a0a5357450d05005d555410010e4155574b45504601`
9.  Gunakan Online XOR Calculator, seperti **https://xor.pw/**  
![image](https://user-images.githubusercontent.com/92077284/189176276-9179d285-f832-4462-b513-5d5c4bea6c0f.png)
10. Didapati hasil XOR adalah `reverseengineericanbarelyforward`
11. Masukan hasil XOR kedalam **mercury.picoctf.net 47423**  
![image](https://user-images.githubusercontent.com/92077284/189177097-9173d232-5c44-4039-8a78-362511bd9bec.png)