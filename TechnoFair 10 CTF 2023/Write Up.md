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

**CHALL :** [chall]()  

**Tahap pengerjaan:**  
1. Download attachment, lalu disini diberikan 31 baris, 7 bit binary. menurut soal ada keyword `display` yang mengarahkan kepada 7 segment display  
source: https://electronics-fun.com/7-segment-hex-decoder/  
![image](https://user-images.githubusercontent.com/92077284/221499933-c995527e-5e4e-4ae2-8728-1b7c2fe1f10e.png)  

2. Dari sini saya coba menggunakan online decoder : https://www.dcode.fr/7-segment-display dan mendapati hasil yang masih berantakan
![image](https://user-images.githubusercontent.com/92077284/221500516-184da63f-4392-438a-a2d6-a6992f60ce2d.png)  

3. Dari sini saya memahami bahwa perlu mereverse dari kanan ke kiri untuk tiap binarynya, jadi saya menggunakan https://www.browserling.com/tools/reverse-binary 
![image](https://user-images.githubusercontent.com/92077284/221501457-5ccef76e-2555-4d0e-a70d-7bf2ad722dd0.png)  

4. Saya menggunakan kembali decoder dan menemukan flagnya, namun karena belum sesuai dengan formatnya, saya merubah rubah dikit untuk hasilnya  
![image](https://user-images.githubusercontent.com/92077284/221502070-8db6d7fd-ef35-4cf2-842b-51535600da86.png)  

```
5UEtAM5CEMEMtE55_|t_|5_HEHE
suetamscememtess_it_is_hehe
supertranscendentess_it_is_hehe
```

**FLAG : ARA23{supertranscendentess_it_is_hehe}**
