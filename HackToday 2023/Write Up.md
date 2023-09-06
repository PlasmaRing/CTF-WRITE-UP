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

   Script untuk generate wordlist:
   
4. 
