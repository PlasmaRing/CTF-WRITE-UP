## WRITE UP [IND]  

![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/dc3dc7e4-0fe0-43ec-9c71-d7eaac627fd7)  

**Platform : https://odyssey.hackrocks.com/**  
**By: [Plasma](https://github.com/PlasmaRing)**   

**DATE: 7/21/23 - 7/23/23**  

---
# Catch The Fox  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/531d23e9-3728-490e-be09-c73722d779ac)

```
The flag is in three parts. The middle part is a number.
Concatenate the three parts to get the full flag.
```

**Private Video :** [video](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/9802d776064bf7847f9e447bd60675eb2eb1cac5/The%20Odyssey%20CTF%202023/catch_the_fox_CTF_odyssey.zip)  
**CHALL :** [challenge.zip](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/e60271746dc6ac4a27cd3695a72e4879811bdb11/The%20Odyssey%20CTF%202023/challenge.zip)  

**Tahap pengerjaan:**  
1. Pertama saya mencoba membuka file, file ini merupakan program exe yang jalan pada terminal.  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/f65ea367-4531-4ac6-b96e-7a0ab9484cd7)  
*Diperlukan _arguments_ untuk menjalankan file.  
2. Saya coba menganalisa menggunakan **IDA Pro**, dan ternyata file merupakan **.NET**, maka saya beralih menggunakan **dnSpy 32 bit**
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/c27ff1d3-03b0-47aa-8358-a97d005c381f)  

3. Disini saya melanjutkan menganalisa file secara mendalam, dan ditemukan bagian ini
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/f492554d-2d01-4204-bef7-12c1c03a8d3a)  
*Beds Protector merupakan sebuah _protector_ terhadap debugger, tampering, memory dump, dll
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/366ddb13-f095-45c5-9d88-14eb6164b068)  

4. Setelah mengetahui hal tersebut saya terpikirkan memeriksa file tersebut menggunakan **Detect It Easy**, dan ternyata file di protect menggunakan BABEL dan Goliath  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/1ff50159-bd3e-4dee-9dd0-3cd297ccbe55)  

5. Selanjutnya saya menggunakan tools untuk mencoba menghapus protector tersebut, saya menggunakan **de4dot**
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/8f0c30a8-dcb6-40ec-be6f-28a36b9ed770)  

6. Dan file ternyata memnag terlihat lebih rapi, namun sayangnya setelah dilepas protectornya, file menjadi rusak dan tidak bisa dijalankan, namun disini dapat terlihat secara garis besar bagaimana flag akan di print

  Protected  
  ![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/83fb70ba-955b-47a0-a5bd-ce51b7bd2c46)  

  Not Protected  
  ![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/b0ffb415-28b8-4a66-8cda-521e0ab14dd3)  
  

7. Setelah itu saya melakukan _dynamic analysis_ dengan melakukan beberapa kali _breakpoints_ pada file awal (protected), disini saya mendapatkan beberapa konklusi.
* Saya menemukan flag bagian 1 dan 2 dengan memasukan value ini : `Beds-Protector-rown-FoxᅠᅠᅠᅠᅠJumped-Over-The-Lazy-DogUAThe-ᅠᅠᅠᅠQuick-Brown-ᅠᅠᅠᅠᅠᅠe-Lazy-DogUAᅠᅠᅠᅠᅠThe-Quick--Over-The-Laᅠᅠᅠᅠzyᅠ`, string ini saya dapatkan dari sini  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/90be7976-f7b0-4e6b-95cb-d4e9ef5292e1)  
Asumsi saya, stringnya seharusnya bukan seperti ini, namun entah kenapa flagnya muncul. Disini flag pertama adalah 
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/732867dd-7f8e-4090-87f7-ecf2767b7726)  

* Berikut adalah tampilan flag bagian 2, flag bagian 2 adalah angka, hal ini juga dijelaskan dalam deskripsi soal, maka dari itu saya sudah merasa bahwa flag ini benar.
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/9d7335b4-d60a-4895-af3a-99f4f251d614)  


* Pada flag bagian 3 ini TIDAK AKAN TERKIRIM, mungkin dikarenakan input yang memang salah, namun disini saya mencoba untuk mengubah value ketika proses _debugging_, dan setelah beberapa kali percobaan akhirnya flag bisa terlihat.
```
1. Ubah value _ menjadi "nop" sebelum program melakukan compare. Kenapa "nop" ? karena value nantinya akan menyimpan isi "nop", hal itu bisa dilihat ketika dijalankan, dan karena "if (_.Contains(value))", maka kita samakan saja valuenya.
2. Lakukan continue lalu STEP OVER, karena program akan langsung exit, maka untuk lihat valuenya harus dilakukan step over
```

![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/b95663da-6082-415a-96ab-5d0fb1b28559)  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/5f208897-daf9-46b7-bf6d-fc9bb578261d)  

8. Didapati flagnya, dan disusun menjadi satu.

**FLAG : flag{s1mple_90_0bfusc4ti0n}**
