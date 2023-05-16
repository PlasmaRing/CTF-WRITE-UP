## WRITE UP [IND]  

![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/b352b8b1-b77e-448b-956d-45b421b76afb)  

**Team: Tidak Ada**  

**By: [Plasma](https://github.com/PlasmaRing)**

**DATE: 02/25/2023 - 02/26/2023**  

**WRITE UP LINK👇**  
[LINK](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/b34bf545aa12148e5e8ccbc4aacfd890aef50eec/ARA%20CTF%204.0%202023/FILE/WU_ARACTF_sudah%20dapet%20orang.pdf)

## Warm Up Challenges

**REVERSE ENGINEERING**
- Buzzer 
- PindahKuy  

**CRYPTOGRAPHY**
- ASCII-PI  
- BanyakPrima  
- EzRSA  

**FORENSIC**
- Citra  
- Morse  

**OTHERS**
- MagicEquation    

**OSINT**
- Dimana  
- WhereIsIt  

---
## Qualification Challenges

**REVERSE ENGINEERING**
- [Furr(y)verse](#furryverse)  
- Bypass the Py  
- Joy Sketching in the Matrix  
- Top-Level-Security  

**CRYPTOGRAPHY**
- Detective Handal  
- [Choo-Choo](#choo-choo)  
- Confusing Encryption  
- CRYptograPI  
- I Like Matrix  
- One Of Us  
- Random is not Random  
- Randomized Seed  

**FORENSIC**
- Been There Done That  
- Date Night  
- Enhanced  
- [Me(me)tadata](#memetadata)  
- The Spectre  

**OTHERS**
- Discovered  
- [Mental Health Check](#mental-health-checK)  
- NCS Cipher  

**OSINT**
- [Back In My Day](#back-in-my-day)  
- Mixtape  
- Know Your Worth  
- Lost
- Twitch Frogs

---

## Buzzer
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## PindahKuy  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## ASCII-PI  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## BanyakPrima  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## EzRSA  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`

## Citra  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Morse  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## MagicEquation    
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Dimana  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## WhereIsIt  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Furr(y)verse  
**Description**   
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/c94eac52-979b-4a95-b60b-95284e44b80b)  

**Solution [INA]**  
1. Pertama download filenya, lalu disini didapati filenya merupakan **ELF**, disini saya lakukan dulu _static analysis_ menggunakan **IDA**  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/c1045e24-af60-47f3-bea2-ff92d6beedcf)  
Disini setelah saya analisis, saya mendapati bahwa terdapat sistem enkripsi sederhana, seperti dapat terlihat terdapat fungsi **EncodeKey**  
2. Karena flag tidak bisa dilihat secara terang-terangan, saya coba untuk melakukan _dinamic analysis_ menggunakan **GDB** pada linux  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/57da75dd-e2e2-49a2-8729-849185d09fa8)  
Gambaran jika file dijalankan  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/b4100590-c81a-410e-8cac-46555d1f37bf)  
Disini saya melakukan _breakpoint_ pada alamat tersebut, karena ada fungsi **cmp**  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/5884d6dc-bc72-4e90-b71a-822142ac7d4f)  
Dan setelah saya jalankan dan memasukan input apapun, disini ternyata sudah terlihat flagnya.
3. FLAG DIPEROLEH  

**Flag**  
`FindITCTF{s0l1d_50L1d_5Ol1D}`  

## Bypass the Py  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Joy Sketching in the Matrix  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Top-Level-Security  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Detective Handal  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Choo-Choo  
**Description**   
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/8658a2a0-0c7a-408e-9096-233108340782)  

**Solution [INA]**  
1. Pertama disini saya download file-file soal, disini didapati 

**Flag**  
`FLAG`  

## Confusing Encryption  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## CRYptograPI  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## I Like Matrix  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## One Of Us  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Random is not Random  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Randomized Seed  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Been There Done That  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Date Night  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Enhanced  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Me(me)tadata  
**Description**   
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/f8e54f31-8491-4bf9-814e-d687e32b5008)  

**Solution [INA]**  
1. Download file, file tersebut adalah file gambar berformat **.jpg**  
2. Karena disini membahas soal metadata maka saya melihat _properties_ pada gambar  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/5a21b5b4-cd89-493d-beda-a83cecc1f725)  
3. Disini ditemukan sebuah string `NDYgNjkgNkUgNjQgNDkgNTQgNDMgNTQgNDYgN0IgNzAgMzQgNEIgMzMgNUYgNkUgNDEgNkUgNzkgMzQgNUYgMzUgMzcgMzIgMzkgMzEgN0Q=;` dan saya gunakan tools seperti **CyberChef** untuk mendekripnya  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/6ec2aaa9-3a2f-4313-8ee6-a0774b4c1961)  
4. FLAG DIPEROLEH  

**Flag**  
`FindITCTF{p4K3_nAny4_57291}`  

## The Spectre  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  


## Discovered  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Mental Health Check  
**Description**   
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/991f5acd-0458-4cbf-951a-d706e137eee0)  

**Solution [INA]**  
1. Pertama download filenya, kebetulan disini memiliki ekstensi **.exe**, maka dari itu saya coba untuk melakukan _static analysis_ menggunakan **IDA**  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/a02a8426-e106-4079-8c92-55154331641c)  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/0ba2f4a9-e952-4779-93d2-83dce99c9975)  
2. Disini langsung ditemukan flagnya, namun kita juga bisa menemukan flagnya menggunakan `strings` pada KALI LINUX  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/31f905ca-1a4c-4dca-a82a-106b51f30287)

**Flag**  
`FindITCTF{everyone_asks_who_are_you_but_not_how_are_you}`  

## NCS Cipher  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  


## Back In My Day  
**Description**   
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/d08461b0-b834-4aaf-a6cc-2b26b9239406)  

**Solution [INA]**  
1. Pertama disini saya coba mencari website yang mencatat riwayat IP Address pada sebuah website, awalnya saya mencoba menggunakan **WayBackMachine**, namun saya tidak menemukan record IPnya  
2. kemudian saya mencoba mencari lagi dan menemukan website https://viewdns.info/iphistory, lalu saya mencoba memasukan website `ugm.ac.id`  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/80d06039-dc98-4afc-a0e3-e11378c7ebae)  
WEB = https://viewdns.info/iphistory/?domain=ugm.ac.id  
3. Pada rentang waktu sesuai soal (2017-05-26 - 2017-09-03), maka IPnya adalah `175.111.88.11`, selanjutnya tinggal dikemas dalam format flag  
4. FLAG DITEMUKAN

**Flag**  
`FindITCTF{175.111.88.11}`  

## Mixtape  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Know Your Worth  
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Lost
**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  

## Twitch Frogs**Description**   


**Solution [INA]**  
1.

**Flag**  
`FLAG`  
