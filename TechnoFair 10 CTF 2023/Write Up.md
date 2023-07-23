## WRITE UP [IND]  

![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/cfa6d2fb-de39-4d76-8cc7-fd9a3299a3df)



**Team: pwnijoditambahrgbag**  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/936bbda0-da18-4673-966e-91b797c96c08)


**By: [green](https://github.com/PlasmaRing) & [blue]() & [red]()**   

**DATE: 09 JULY 2023**  

**WRITE UP LINK👇**  
[LINK](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/f63454c2183cb3a04055b5509ca0f82d4567b2f2/TechnoFair%2010%20CTF%202023/FILE/CTF_TECHNOFAIR10.0_PWNRGBDITAMBAHIJO.pdf)

## Solved Probs


**Binary Exploitation**  
● Terobozz  

**Reverse Engineering**  
● mencariPW  
● PM Gratis  
● Asep  
● The Password Quest *[SOLVED AFTER COMPETITION END]*  
  
**Web Exploitation**  
● Jin App  
● secret_door  

**Cryptography**  
● RSA Bwang  
● Marsah  

**Forensic**  
● file pemberian fans  

**Misc**  
● Forward Player  
● Welcome  

---
# The Password Quest  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/582f7390-629d-4bf1-bce8-dca24fa83ee6)  

**HINT :**  
```
follow the traffic lights flag rules:

- when it shows red flag, you're not allowed to submit
- when it shows green flag, you're ready to go!
```

**CHALL :** [chall](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/0e3b4ce4729c33224c25e01a3760b640dcb2daa5/TechnoFair%2010%20CTF%202023/FILE/chall)  

**Tahap pengerjaan:**  
1. Pertama-tama lakukan analisa menggunakan IDA, karena disini file dalam bentuk ELF  
2. Saat program dijalankan, program akan mengirimkan beberapa _Fake Flag_ secara acak, disini didapati ada sekitar 4-5 _Fake Flag_  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/78644b83-03f2-4532-87e0-6872e1891e44)  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/7fb522de-187f-4b46-bdcd-9d022b784088)  
*Gambar diatas adalah merupakan contoh _fake flag_ dan isinya.  

3. Setelah itu dilakukan analisa lebih lanjut terhadap fungsi-fungsi dalam program, dan ditemukan bagian ini, yang ternyata merupakan bagian yang memeriksa input
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/0f235ddc-54bd-446e-baf8-9732e6163851)
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/f696c1ae-4b8e-457c-8ce9-9e6fb18267bd)  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/559796f0-1aaf-43e2-ab31-2bc95db3c6ad)  

Keterangan:  
* dword_40C0 = flag yang sudah di_encrypt_ sesuai algoritma diatas  
* sub_1239 = strlen  
* sub_1568 =  reverse string

4. Maka dari itu dibuatlah sebuah code dari python yang sekiranya sama seperti program  

```py
def check_a1(a1):
    a1 = [ord(char) for char in a1]
    v4 = 0
    v3 = len(a1)

    dword_40C0 = [0xC4, 0xBE, 0x96, 0xB7, 0xBD, 0xBC, 0x88, 0xCD, 0x98, 0xFD, 0xF8, 0x38, 0x96, 0x09, 0xFD, 0xFF, 0x84, 0xA0, 0xC6, 0xE7, 0xA6, 0xCD, 0xF2, 0xD9, 0xF6, 0xED, 0x8E, 0xC6, 0x94, 0x32, 0xD4, 0xC4, 0x3B, 0x91, 0x2E, 0xF4, 0x34, 0xA4, 0xB0, 0xF6, 0xCA, 0x8C, 0xF6, 0xED, 0x9E, 0xE9, 0xA2, 0xCF, 0xCD, 0xE7, 0xE7, 0x96, 0xAB, 0xB7, 0x97, 0xDD, 0x99, 0x5F, 0xA5, 0x08, 0xB2, 0xA0, 0xEC, 0xCB, 0x9D, 0xE5, 0xD4, 0x90, 0x93, 0xB5, 0xE7, 0x8C, 0x2E, 0xBC, 0xE0, 0xCE, 0xD9, 0xE3, 0x9F, 0xE7, 0x94, 0xD3, 0x85, 0xF9, 0x8D, 0xEF, 0xE9, 0x34, 0xA6, 0xA6, 0xCA, 0xCA]

    for i in range(len(a1) // 2): 
        if i & 1 != 0:
            if (a1[v4 + 1] + a1[v4]) ^ a1[v3 - 1] != dword_40C0[i]:
                print("Wrong")
                return
            v4 += 1
        else:
            if (a1[v3 - 2] + a1[v3 - 1]) ^ a1[v4] != dword_40C0[i]:
                print("Wrong")
                return
            v3 -= 1

    print("Correct")

if __name__ == "__main__":
    input_text = input("Enter the text: ")
    input_text = input_text[::-1]
    check_a1(input_text)
```

6.  Setelah itu saya coba mendapati value a1 dengan cara menggunakan z3 solver

```py
from z3 import *

def solve_a1(dword_40C0):
    s = Solver()

    a1 = [BitVec(f"a1_{i}", 8) for i in range(len(dword_40C0))]
    v4 = 0
    v3 = len(dword_40C0)

    # Format FLAG TechnoFairCTF{*} kalau di reverse jadi }*{FTCriaFonhceT
    # Kalau tidak di declare akan error, mungkin karena bisa ada value lain yang sesuai dengan kondisi
    s.add(a1[0] == ord('}'))
    s.add(a1[-1] == ord('T'))
    s.add(a1[-2] == ord('e'))
    s.add(a1[-3] == ord('c'))
    s.add(a1[-4] == ord('h'))
    s.add(a1[-5] == ord('n'))
    s.add(a1[-6] == ord('o'))
    s.add(a1[-7] == ord('F'))
    s.add(a1[-8] == ord('a'))
    s.add(a1[-9] == ord('i'))
    s.add(a1[-10] == ord('r'))
    s.add(a1[-11] == ord('C'))
    s.add(a1[-12] == ord('T'))
    s.add(a1[-13] == ord('F'))
    s.add(a1[-14] == ord('{'))

    for i in range(len(dword_40C0)):  # ALGORITMA
        if i & 1 != 0:
            s.add((a1[v4 + 1] + a1[v4]) ^ a1[v3 - 1] == dword_40C0[i])
            v4 += 1
        else:
            s.add((a1[v3 - 2] + a1[v3 - 1]) ^ a1[v4] == dword_40C0[i])
            v3 -= 1

    if s.check() == sat:
        model = s.model()
        result_a1 = "".join([chr(model[a1[i]].as_long()) for i in range(len(dword_40C0))])
        return result_a1[::-1]  # REVERSE
    else:
        return None

if __name__ == "__main__":
    dword_40C0 = [0xC4, 0xBE, 0x96, 0xB7, 0xBD, 0xBC, 0x88, 0xCD, 0x98, 0xFD, 0xF8, 0x38, 0x96, 0x09, 0xFD, 0xFF, 0x84, 0xA0, 0xC6, 0xE7, 0xA6, 0xCD, 0xF2, 0xD9, 0xF6, 0xED, 0x8E, 0xC6, 0x94, 0x32, 0xD4, 0xC4, 0x3B, 0x91, 0x2E, 0xF4, 0x34, 0xA4, 0xB0, 0xF6, 0xCA, 0x8C, 0xF6, 0xED, 0x9E, 0xE9, 0xA2, 0xCF, 0xCD, 0xE7, 0xE7, 0x96, 0xAB, 0xB7, 0x97, 0xDD, 0x99, 0x5F, 0xA5, 0x08, 0xB2, 0xA0, 0xEC, 0xCB, 0x9D, 0xE5, 0xD4, 0x90, 0x93, 0xB5, 0xE7, 0x8C, 0x2E, 0xBC, 0xE0, 0xCE, 0xD9, 0xE3, 0x9F, 0xE7, 0x94, 0xD3, 0x85, 0xF9, 0x8D, 0xEF, 0xE9, 0x34, 0xA6, 0xA6, 0xCA, 0xCA]
    result_a1 = solve_a1(dword_40C0)
    if result_a1:
        print(f"FLAG: {result_a1}")
    else:
        print("NOT FOUND")
```

![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/e176b669-145a-4c5a-97f7-8fda70e05884)  

**FLAG : TechnoFairCTF{VOI1@!_TUrn$_ou7_7hE_m19hTy_fla6_1$_@LReADy_p0s$35sed_BY_y0U_AL1_7h1s_71ME^v^}**
