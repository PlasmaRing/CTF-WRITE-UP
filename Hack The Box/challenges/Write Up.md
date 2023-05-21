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
| 4  | [Find The Easy Pass](#find-the-easy-pass) | 24/4/2023 | HTB{fortran!} | 0 | RETIRED | EASY |

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

## Find The Easy Pass

**Description**  
```
Find the password (say PASS) and enter the flag in the form HTB{PASS}
```
FILE : []()  

**Solution [INA]**  
1.  Pertama-tama download _chall_, disini file merupakan **.exe** sehingga saya coba jalankan dulu agar tahu jalan kerja program, disini diperlukan input password  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/2ccf1bf4-df6e-4f7d-8932-40965dbdd617)  

2.  Karena file ini **.exe** maka saya coba lakukan static analysis menggunakan tools **IDA**, disini saya mencoba masuk kebagian **Button1Click** karena disini kita perlu melakukan klik submit untuk memeriksa _password_  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/cbb75642-11ed-4ec1-b07b-bc11553e26c3)  
Pada bagian ini saya menganalisis bahwa input string berjumlah **8** karena disini dia membaca setiap _character_ lalu di gabungkan
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/896192bd-099f-4015-a411-719e098546ae)  
dan bila password benar maka akan melakukan output **Congrats**  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/f6a76e95-0ea6-4549-816a-16ab916b9300)  
Setelah saya coba cek, ternyata setiap charnya tersimpan dan dapat disusun menjadi `fortran!`  

3.  Saya coba masukan _password_ dengan input `fortran!` dan FLAG DIPEROLEH  
![image](https://github.com/PlasmaRing/CTF-WRITE-UP/assets/92077284/44812b15-7693-4790-9abc-5f26eebfde9f)  

**Flag**  
`HTB{fortran!}`  

## Shattered Tablet

**Description**  
```
Deep in an ancient tomb, you've discovered a stone tablet with secret information on the locations of other relics. However, while dodging a poison dart, it slipped from your hands and shattered into hundreds of pieces. Can you reassemble it and read the clues?
```

## Eat the Cake!

**Description**  
```
Find the Password and enter it in the form HTB{password}
```

## Baby RE

**Description**  
```
Show us your basic skills! (P.S. There are 4 ways to solve this, are you willing to try them all?)
```

## Ransom

**Description**  
```
We received an email from Microsoft Support recommending that we apply a critical patch to our Windows servers. A system administrator downloaded the attachment from the email and ran it, and now all our company data is encrypted. Can you help us decrypt our files?
```

## You Cant C Me

**Description**  
```
Can you see me?
```

## Baby Crypt

**Description**  
```
Give me the key and take what's yours.
```

## Anti Flag

**Description**  
```
Flag? What's a flag?
```

## IRCWare

**Description**  
```
During a routine check on our servers we found this suspicious binary, although when analyzing it we couldn't get it to do anything. We assume it's dead malware, but maybe something interesting can still be extracted from it?
```

## Sekure Decrypt

**Description**  
```
Timmy created a secure decryption program
```

## Hissss

**Description**  
```
Can you slither around the authentication?
```

## Rebuilding

**Description**  
```
You arrive on a barren planet, searching for the hideout of a scientist involved in the Longhir resistance movement. You touch down at the mouth of a vast cavern, your sensors picking up strange noises far below. All around you, ancient machinery whirrs and spins as strange sigils appear and change on the walls. You can tell that this machine has been running since long before you arrived, and will continue long after you're gone. Can you hope to understand its workings?
```

## Snakecode

**Description**  
```
We found this ancient text inscribed on a stone tablet. We believe it describes the history and technology of a mighty but extinct civilization, but we can't be certain as it's written in a dead language. Can you use your specialist knowledge to uncover the truth, and recover their technology?
```

## Ouija

**Description**  
```
You've made contact with a spirit from beyond the grave! Unfortunately, they speak in an ancient tongue of flags, so you can't understand a word. You've enlisted a medium who can translate it, but they like to take their time...
```

## Secured Transfer

**Description**  
```
Ghosts have been sending messages to each other through the aether, but we can't understand a word of it! Can you understand their riddles?
```

## Potion Master

**Description**  
```
After adding the curried eel, your potion is almost complete, your cauldron boiling over. All you need to do now is incant the final spell to finish your masterwork!
```

## Pseudo

**Description**  
```
Do you have enough permissions to get the flag?
```

## The Vault

**Description**  
```
After following a series of tips, you have arrived at your destination; a giant vault door. Water drips and steam hisses from the locking mechanism, as you examine the small display - 'PLEASE SUPPLY PASSWORD'. Below, a typewriter for you to input. You must study the mechanism hard - you might only have one shot...
```

## Malception

**Description**  
```
Attackers have infiltrated our domain and poisoned DNS records to infect users with a ransomware. We weren't able to retrieve any artifacts, but we have a packet capture you could use.
```

## Teleport

**Description**  
```
You've been sent to a strange planet, inhabited by a species with the natural ability to teleport. If you're able to capture one, you may be able to synthesise lightweight teleportation technology. However, they don't want to be caught, and disappear out of your grasp - can you get the drop on them?
```

## Indefinite

**Description**  
```
You hold in one hand an encrypted datastream, and in the other the central core of a Golden Fang communications terminal. Countless spies have risked their lives to steal both the encrypted attack plans, and the technology used to conceal it, and bring them to you for expert analysis. To your horror, as you turn the screws on the core, its defense mechanisms spring to life, concealing and covering its workings. You have minutes to spare before the device destroys itself - can you crack the code?
```

## Mr. Abilgate

**Description**  
```
Mr. Abilgate, the CFO of a Fortune 500 company, has reportedly been the victim of a recent spree of ransomware attacks. The behavior of the malware seems consistent with our current APT target's tactics, but the ransom note makes us think it's a targeted attack. We suspect bad faith from corporate espionage gone wrong. Could you investigate?
```

## Pneumatic Validator

**Description**  
```
In some alternate reality, computers are not electronics-based but instead use air pressure. No electrons are zipping by and instead, a large pneumatic circuit takes care of all the math. In that world, we reverse engineers are not staring countless hours into debuggers and disassemblers but are inspecting the circuits on a valve level, trying to figure out how the particles will behave in weird components and how they are connected. Thinking about it, that doesn't sound too different, does it?
```

---
# Crypto
## Gonna-Lift-Em-All

**Description**  
```
Quick, there's a new custom Pokemon in the bush called "The Custom Pokemon". Can you find out what its weakness is and capture it?
```

## Ancient Encodings

**Description**  
```
Your initialization sequence requires loading various programs to gain the necessary knowledge and skills for your journey. Your first task is to learn the ancient encodings used by the aliens in their communication.
```

## Perfect Synchronization

**Description**  
```
The final stage of your initialization sequence is mastering cutting-edge technology tools that can be life-changing. One of these tools is quipqiup, an automated tool for frequency analysis and breaking substitution ciphers. This is the ultimate challenge, simulating the use of AES encryption to protect a message. Can you break it?
```

## Weak RSA

**Description**  
```
Can you decrypt the message and get the flag?
```

## Classic, yet complicated!

**Description**  
```
Find the plaintext, the key is your flag!
Flag format : HTB{key in lowercase}
```

## Brainy's Cipher

**Description**  
```
Brainy likes playing around with esoteric programming. He also likes math and has therefore encrypted his very secure password with a popular encryption algorithm. Claiming that his password cannot be retrieved now, he has sent the ciphertext to some of his friends. Can you prove to Brainy that his password can actually be recovered?
```

## RsaCtfTool

**Description**  
```
Crypto is fun ;)
```

## TwoForOne

**Description**  
```
Alice sent two times the same message to Bob.
```

## Nuclear Sale

**Description**  
```
Plutonium Labs is a private laboratory experimenting with plutonium products. A huge sale is going to take place and our intelligence agency is interested in learning more about it. We have managed to intercept the traffic of their mail server. Can you find anything interesting?
```

## LunaCrypt

**Description**  
```
Our astronaut gained access to a key satellite and intercepted an encrypted message. The forensics team also recovered a file that looks like a custom encryption protocol. We're sure that these two elements are linked. Please can you help us reveal the contents of the secret message?
```

## Space Pirates

**Description**  
```
Jones and his crew have started a long journey to discover the legendary treasure left by the guardians of time in the early beginnings of the universe. Mr Jones, though, is wanted by the government for his crimes as a pirate. Our agents entered his
```

## baby quick maffs

**Description**  
```
Wikipedia says "the Rabin cryptosystem has been mathematically proven to be computationally secure against a chosen-plaintext attack as long as the attacker cannot efficiently factor integers", so I created my own cool implementation.
```

## How The Columns Have Turned

**Description**  
```
A day before the memorial of the Dying Sun, Miyuki began talking about Broider, a death squad commander and a friend of Paulie’s capturer. He would be a party guest at Viryr’s palace. After examining a lot of different scenarios, Miyuki came up with a plan in which Paulie would lure Broider to a secluded location so the group could capture him. Following the plan, a wild chase had just begun when the two looked each other in the eye. After an extremely risky maneuver, Paulie outwitted Broider and led him into an alley in Vinyr’s undercity. The plan was a success. Your squad had managed to capture Broider and bring him back to the ship. After hours of interrogation by Ulysses, he revealed the final key to a series of encrypted messages. Can you find a way to decrypt the others? The flag consists entirely of uppercase characters and has the form HTB{SOMETHINGHERE}. You still have to add the {} yourself.
```

## ElElGamal

**Description**  
```
After some minor warnings from IDS, you decide to check the logs to see if anything suspicious is happening. Surprised by what you see, you realise that one of your honeypots has been compromised with a cryptominer. As you look at the processes, you discover a backdoor attached to one of them. The backdoor retrieves the private key from the /key route of a C2. It establishes a session by sending an encrypted initilazation sequence. After the session is established, it waits for commands. The commands are encrypted and executed by the source code you found. Unfortunately, the IDS could not detect the request to /key and the machine was rebooted after the compromise, so the key cannot be found on the stack. Can you find out if any data was exfiltrated from the honeypot to mitigate future attacks?
```

## Spooky RSA

**Description**  
```
It was a Sunday evening when, after years, you managed to understand how RSA works. Unfortunately, that changed when the worst villain ever decided to dress up like RSA and scare people who wanted to learn more about cryptography. But his custom uniform has a hole in it. Can you find it?
```

## Infinite Descent

**Description**  
```
DevOps have come up with a great way to choose primes for RSA and an even better way to established a key for AES.
Can you find the flaws?
Flag Format: HTB{flag}
```

## Ebola Virus

**Description**  
```
We suspect that some terrorists have a plan to use the Ebola virus. We have managed to collect an encypted message and its key. Can you help us decrypt the message?
```

## signup

**Description**  
```
The aliens attacked our territory and stole our necessary supplies and kept them in a secure manner. We can get them back, but it requires a lot of data samples. Fortunately, we have some stuff to get back what we need. But, are we lucky enough?!
```

## BFD56

**Description**  
```
At least Delastelle didn't have to worry about bit flipping. p.s. The flag format is HTB{ALL_IN_UPPERCASE}.
```

## Down the Rabinhole

**Description**  
```
Miyuki, wanting to find out more evidence about Draeger and his escape, planned a space trip to the maximum security black hole where Draeger was held captive. Problems though soon arose as the approach to the black hole caused distortions on your electronics. Memories of the traumatic experience you had when the Council guards brutally ripped you from your father’s hands painfully flooded your mind. The one thing you never forgot was the signal he sent you while you were still within range of the planet. Only two packets got through, but since they were encrypted you couldn’t figure out what they were. Now, being more determined than ever to find your father, having gained experience during the missions with the squad, you know that it’s time to decrypt the signal.
```

## P

**Description**  
```
I
```

## P

**Description**  
```
I
```

## P

**Description**  
```
I
```

## P

**Description**  
```
I
```

## P

**Description**  
```
I
```

## P

**Description**  
```
I
```

## P

**Description**  
```
I
```

## P

**Description**  
```
I
```

## P

**Description**  
```
I
```

## P

**Description**  
```
I
```

## P

**Description**  
```
I
```

## P

**Description**  
```
I
```

## P

**Description**  
```
I
```

## P

**Description**  
```
I
```

## P

**Description**  
```
I
```
