# HTB challenges
23 April 2023  
WEB : https://app.hackthebox.com/challenges/

## Overview

``CATEGORY : REVERSING``

| No | Title               | Date              | Flag                 | Points               | Status               | Diff        
|----|---------------------|-------------------|----------------------|----------------------|----------------------| 
| 1  | [Wide](#wide) | 23/4/2023 | HTB{som3_str1ng5_4r3_w1d3} | 0 | RETIRED | VERY EASY

# Reversing
## Wide

**Description**  
```
We've received reports that Draeger has stashed a huge arsenal in the pocket dimension Flaggle Alpha. You've managed to smuggle a discarded access terminal to the Widely Inflated Dimension Editor from his headquarters, but the entry for the dimension has been encrypted. Can you make it inside and take control?
```
FILE : []()  

**Solution [INA]**  
1.  Download Filenya, disini diberikan file elf dan file dengan extension **.ex**, pertama-tama saya memeriksa jalannya file  
![image](https://user-images.githubusercontent.com/92077284/233834174-dafd261e-7e02-4b35-ad8a-464450e86a8f.png)  
Setelah dilakukan beberapa kali percobaan, disini perlu dimasukan angka 1 dst untuk memilih opsi dari tabel, disini terdapat file tersembunyi pada opsi **6**, dimana akan diminta input lagi berupa _key_  
![image](https://user-images.githubusercontent.com/92077284/233834326-a923ca98-720b-46f8-a3ec-97683a773ffa.png)
2.  Setelah mengetahui bahwa gile memerlukan input key, saya menggunakan tools **IDA**, untuk memeriksa file, dan disini saya menemukan adanya compare string pada fungsi **menu**  
![image](https://user-images.githubusercontent.com/92077284/233834414-e53b503d-9a12-4a51-88f0-b82922a9be00.png)
3.  Disini saya mencoba untuk menemukan keynya menggunakan **strings** namun tidak ada, sehingga saya menggunakan **gdb** untuk memeriksa string yang dicompare  
4.  Proses ini saya coba beberapa kali, namun saya tidak menemukan string asli yang dicompare *note : mungkin saya kurang teliti* akhirnya saya langsung jump ke 0x555555400d93 , dimana lokasi ini seharusnya terpanggil jika saya menginput key yang benar.  
![image](https://user-images.githubusercontent.com/92077284/233834854-0816d2bd-b90a-4e54-9af2-3d3c88a5a30d.png)

5.  FLAG DIPEROLEH

**Flag**  
`HTB{som3_str1ng5_4r3_w1d3}`

