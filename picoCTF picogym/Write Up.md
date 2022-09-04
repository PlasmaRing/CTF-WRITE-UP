# picoCTF picogym
WEB : `https://picoctf.org/`  

## Overview

| No | Title               | Date              | Category                   | Flag                 | Points
|----|---------------------|-------------------|----------------------------|----------------------|------------
| 1  | Transformation | 19/06/2022 | Reverse Engineering | picoCTF{16_bits_inst34d_of_8_d52c6b93} | 20
| 2  | keygenme-py | 21/06/2022 | Reverse Engineering | picoCTF{1n_7h3_I<3y_of_ac73dc29} | 30
| 3  | crackme-py | 04/09/2022 | Reverse Engineering | picoCTF{1I\/I_4_p34I\Iut_f3bc410e} | 30

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
