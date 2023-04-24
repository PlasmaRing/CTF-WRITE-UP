# HTB challenges
23 April 2023  
WEB : https://app.hackthebox.com/challenges/

## Overview

``CATEGORY : REVERSING``

| No | Title               | Date              | Flag                 | Points               | Status               | Diff        
|----|---------------------|-------------------|----------------------|----------------------|----------------------|---------
| 1  | [Wide](#wide) | 23/4/2023 | HTB{som3_str1ng5_4r3_w1d3} | 0 | RETIRED | VERY EASY |
| 2  | [The Art of Reversing](#the-art-of-reversing) | 23/4/2023 | HTB{hacktheplanet365} | 0 | RETIRED | EASY |
| 3  | [Tear Or Dear](#tear-or-dear) | 23/4/2023 | HTB{piph:roiw!@#} | 0 | RETIRED | EASY |

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
4.  Proses ini saya coba beberapa kali, namun saya tidak menemukan string asli yang dicompare  
*note : mungkin saya kurang teliti*  
akhirnya saya langsung jump ke 0x555555400d93 , dimana lokasi ini seharusnya terpanggil jika saya menginput key yang benar.  
![image](https://user-images.githubusercontent.com/92077284/233834854-0816d2bd-b90a-4e54-9af2-3d3c88a5a30d.png)

5.  FLAG DIPEROLEH

**Flag**  
`HTB{som3_str1ng5_4r3_w1d3}`

## The Art of Reversing

**Description**  
```
This is a program that generates Product Keys for a specific Software Brand.

The input is the client UserName and the Number of Days that the sofware will remain active on the client.
The output is the product key that client will use to activate the software package.

We just have the following product key 'cathhtkeepaln-wymddd'
Could you find the corresponding Username say A and the number of activation days say B given as input?

The flag you need to enter must follow this format: HTB{AB}
```
FILE : []()  

**Solution [INA]**  
1.  Download file yang diberikan, kebetulan disini berformat **.exe**, maka saya coba jalankan langsung di windows.  
2.  Didapati sebuah generator kunci, dengan algoritma tertentu, disini memiliki ketentuan bahwa _activation days_ harus dalam interval **15-3650**
![image](https://user-images.githubusercontent.com/92077284/233841225-d2a2f43b-8703-4ecc-ada2-7b7a49b939c4.png)  
3.  Setelah itu saya coba menggunakan tools seperti **IDA** dan **JustDecompile**, disini saya dapati bahwa untuk _activation days_ di generate menggunakan angka romawi yang di reverse dan di shifting. Hal ini saya sadari dari hasil _decompile_ softwarenya.  
![image](https://user-images.githubusercontent.com/92077284/233841375-232af077-64e8-46b5-bcc1-9742c07f0734.png)  
Disini, saya amati bahwa jika diatas 1000, maka di hapus dan string di _concat_, jika diatas 500 maka di hapus dan string di _concat_, dan seterusnya, selain itu saya menganalisis bila saya memasukan angka **16 = jwy**, **17 = jjwy**. Hal ini sama dengan cara penulisan angka romawi hanya saja sedikit dienkrip   
![image](https://user-images.githubusercontent.com/92077284/233841539-1dfe5c37-e867-47e1-a696-94d935e3564d.png)  
Disini didapati bahwa output harus **wymddd**, maka string saya shift 1 menjadi **vxlccc**, lalu saya reverse menjadi **CCCLXV**, dimana bila diterjemahkan menjadi **365**  
Tools : https://www.rapidtables.com/convert/number/roman-numerals-converter.html & https://www.dcode.fr/shift-cipher  
4.  Setelah itu tinggal usernamenya, disini saya menggunakan cara manual, karena melihat bahwa sistem generatenya sangatlah mudah, karena tidak ada algoritma random dan hanya diacak urutannya, seperti berikut saya memasukan **ABCDEFGHIJKLM**, didapati output **CBEFAMDLGHJIK**  
![image](https://user-images.githubusercontent.com/92077284/233841151-b456b622-463f-471d-8879-dcd7c49c1dad.png)  
Maka dengan menyusun urutannya didapati hasil sebagai berikut
```
ABCDEFGHIJKLM
CBEFAMDLGHJIK

hacktheplanet
cathhtkeepaln
```
5.  Terakhir hanya tinggal disusun formatnya, dan FLAG DIPEROLEH  

**Flag**  
`HTB{hacktheplanet365}`

## Tear Or Dear

**Description**  
```
Find the username and password and put them in the flag in the format: HTB{username:password}
Warning: It can produce false positives.
```
FILE : []() 

**Solution [INA]**  
1.  Pertama-tama download _chall_, disini file merupakan **.exe** sehingga saya coba jalankan dulu agar tahu jalan kerja program, disini diperlukan input username dan password, sehingga saya mencoba menganalisis menggunakan tools **IDA Pro** untuk melakukan analisa singkat, disini file menggunakan **.NET**, maka saya melanjutkan menggunakan tools **JustDecompile** dan **dnSpy 32 Bit**
![image](https://user-images.githubusercontent.com/92077284/233891745-4977ff6e-d78e-48a7-92b2-42ce3e9efab8.png)  

2.  Disini terdapat fungsi pemeriksa username dan password, jika benar maka akan melakukan print _Correct!_  
![image](https://user-images.githubusercontent.com/92077284/233891710-50d2611e-a670-4ff9-8cc1-c0c881682f92.png)  
Setelah saya menganalisis, validasinya ada 2 : **this.username == this.o dan this.check1(str)**
![image](https://user-images.githubusercontent.com/92077284/233891985-a59094eb-cc93-437a-b816-07bc30ad81ef.png)  
dan bila dianalisa, check1 akan memanggil fungsi sampai berakhir pada **(this.textBox_user.Text != this.aa)**
maka dari itu karena username dan password tidak bisa dilihat, maka saya melakukan debugging menggunakan **dnSpy**  
3.  Saya menaruh _breakpoint_ ketika melakukan validasi password dan username,  
![image](https://user-images.githubusercontent.com/92077284/233892295-f63ba2bf-5313-4cb9-9ced-89ab7f155611.png)  
lalu saya memasukan password = PASS , dan username = USER  
![image](https://user-images.githubusercontent.com/92077284/233892464-6c7ce927-f935-4613-9448-2c69b867dea8.png)  
Setelah melakukan debug, didapati beberapa data sebagai berikut
![image](https://user-images.githubusercontent.com/92077284/233892676-435d0d52-b8e1-4366-8204-cf351c9a87cf.png)
![image](https://user-images.githubusercontent.com/92077284/233892732-33112e0f-7a26-4a54-b8ea-aa812afe41b5.png)
![image](https://user-images.githubusercontent.com/92077284/233892793-71531339-b423-49a3-9246-92023c31448c.png)
Disini bisa terlihat bahwa **o = "roiw!@#"** **aa = "piph"**, dan **this.username = "PASS"**,  
a. karena **this.username == this.o** maka Passwordnya adalah `roiw!@#`  
b. karena **this.check1(str) berujung pada (this.textBox_user.Text != this.aa)**, maka input user adalah `piph`  
![image](https://user-images.githubusercontent.com/92077284/233893358-e7425fc0-d98b-48f5-9401-76ad95ea8f44.png)  

4.  Masukan kedua data tersebut, dan FLAG DIPEROLEH

**Flag**  
`HTB{piph:roiw!@#}`
