# MENGPETIR DUA
WEB : `https://picoctf.org/`  

## Overview

| No | Title               | Date              | Category                   | Flag                 | Points
|----|---------------------|-------------------|----------------------------|----------------------|------------
| 1  | Transformation | 19/6/2022 | Reverse Engineering | picoCTF{16_bits_inst34d_of_8_d52c6b93} | 20
| 2  | 
| 3  | 

# Reverse Engineering 
## Transformation 

**Description**  
I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

**Hints 1**  
You may find some decoders online

**Solution [INA]**  
1.  Analisa file `enc` yang berisi: `灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽`
2.  Gunakan online decoder seperti CyberChef
3.  Gunakan Magic & Intensive Mode pada Cyber Chef
![image](https://user-images.githubusercontent.com/92077284/174487475-945bbb78-1445-4980-a895-335a348e2a82.png)  
4.  FLAG DIPEROLEH 

**Flag**  
`picoCTF{16_bits_inst34d_of_8_d52c6b93}`

## JUDUL 2
