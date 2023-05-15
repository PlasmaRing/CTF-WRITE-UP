## WRITE UP [IND]  

![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/b352b8b1-b77e-448b-956d-45b421b76afb)  

**Team: Tidak Ada**  

**By: [Plasma](https://github.com/PlasmaRing)**

**DATE: 02/25/2023 - 02/26/2023**  

**WRITE UP LINK👇**  
[LINK](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/b34bf545aa12148e5e8ccbc4aacfd890aef50eec/ARA%20CTF%204.0%202023/FILE/WU_ARACTF_sudah%20dapet%20orang.pdf)

## Warm Up Challenges

**REVERSE ENGINEERING**
-  Vidner's Rhapsody  

**CRYPTOGRAPHY**
- One Time Password (?)  
- Secrets Behind a Letter  
- L0v32x0r  
- SH4-32  
- babychall  
- Help *[SOLVED AFTER COMPETITION END]*

**FORENSIC**
- Thinker  

**OTHERS**
- in-sanity check  
- @B4SH  
- D0ts N D4sh3s  
- Truth  
- Feedback    

**OSINT**
- Time Machine  
- Backroom  
- Hey detective, can you help me  

## Qualification Challenges

**REVERSE ENGINEERING**
-  Vidner's Rhapsody  

**CRYPTOGRAPHY**
- One Time Password (?)  
- Secrets Behind a Letter  
- L0v32x0r  
- SH4-32  
- babychall  
- Help *[SOLVED AFTER COMPETITION END]*

**FORENSIC**
- Thinker  

**OTHERS**
- in-sanity check  
- @B4SH  
- D0ts N D4sh3s  
- Truth  
- Feedback    

**OSINT**
- Time Machine  
- Backroom  
- Hey detective, can you help me  

---
# Help  
![image](https://user-images.githubusercontent.com/92077284/221419977-a5e97429-55ed-4768-abed-5fa64ee62d0c.png)  
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
