# picoCTF 2022 WRITE UP
MAR 15 - MAR 30 | 2022

## Overview

| No | Title               | Category              | Points  | Flag
|----|---------------------|-----------------------|---------|----------------------------
| 1  | file-run1 | Reverse Engineering | 100 | picoCTF{U51N6_Y0Ur_F1r57_F113_ac61264e} 
| 2  | file-run2 | Reverse Engineering | 100 | picoCTF{F1r57_4rgum3n7_c2db2786}
| 3  | GDB Test Drive | Reverse Engineering | 100 | 
| 4  | patchme.py | Reverse Engineering | 100 | 
| 5  | Safe Opener | Reverse Engineering | 100 | 
| 6  | unpackme.py | Reverse Engineering | 100 | 
| 7  | bloat.py | Reverse Engineering | 200 | 
| 8  | Fresh Java | Reverse Engineering | 200 | 
| 9  | Bbbbloat | Reverse Engineering | 300 | 
| 10 | unpackme | Reverse Engineering | 300 | 
| 11 | basic-mod1 | Cryptography | 100 | 
| 12 | basic-mod2 | Cryptography | 100 | 
| 13 | credstuff | Cryptography | 100 | 
| 14 | morse-code | Cryptography | 100 | 
| 15 | rail-fence | Cryptography | 100 | 
| 16 | substitution0 | Cryptography | 100 | 
| 17 | substitution1 | Cryptography | 100 | 
| 18 | substitution2 | Cryptography | 100 |
| 19 | transposition-trial | Cryptography | 100 | 
| 20 | Vigenere | Cryptography | 100 | 
| 21 | diffie-hellman | Cryptography | 200 | 
| 22 | Enhance! | Forensics | 100 | 
| 23 | Lookey here | Forensics | 100 | 
| 24 | Packets Primer | Forensics | 100 | 
| 25 | Redaction gone wrong | Forensics | 100 | 
| 26 | Includes | Web Exploitation | 100 | 
| 27 | Inspect HTML | Web Exploitation | 100 | 
| 28 | Local Authority | Web Exploitation | 100 | 
| 29 | Power Cookie | Web Exploitation | 200 |


# Reverse Engineering 
## file-run1

**Description**  
A program has been provided to you, what happens if you try to run it on the command line?
Download the program [here](https://github.com/PlasmaRing/CTF-WRITE-UP/blob/86ca38d98bcde32d0d779086bfb8bd680efa27e5/picoCTF%202022/FILE/run)

**Hints 1**  
To run the program at all, you must make it executable (i.e. **$ chmod +x run**)

**Hints 2**  
Try running it by adding a '.' in front of the path to the file (i.e. **$ ./run**)

**Solution [INA]**  
1. Download `run` file
2. Buka terminal, dan pergi ke __directory file__
3. Ketik `chmod +x run` untuk membuat file __executable__
4. Ketik `./run`
5. FLAG DIPEROLEH

![CTFPICO](https://user-images.githubusercontent.com/92077284/160277012-1141bead-106c-4303-86d0-53f19d6b52d6.png)

**Flag**  
`picoCTF{U51N6_Y0Ur_F1r57_F113_ac61264e}`


## file-run2

**Description**  
Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?
Download the program [here]()

**Hints 1**  
Try running it and add the phrase "Hello!" with a space in front (i.e. **"./run Hello!"**)

**Solution [INA]**  
1. Download `run (1)` file
2. Buka terminal, dan pergi ke __directory file__
3. Ketik `chmod +x 'run(1)'` untuk membuat file __executable__
4. Ketik `./'run(1)' Hello!`
5. FLAG DIPEROLEH

**Flag**  
`picoCTF{F1r57_4rgum3n7_c2db2786}`

## GDB Test Drive
tES

## patchme.py
Tes

## Safe Opener
tES

## unpackme.py
Tes

## bloat.py
tES

## Fresh Java
Tes

## Bbbbloat
tES

## unpackme
Tes


# Cryptography
## file-run1
