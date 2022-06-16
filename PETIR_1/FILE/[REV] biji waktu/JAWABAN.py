from ctypes import * #import modulenya

libc = CDLL("libc.so.6") #import library yg dipake sama c

fl = open('secret_message.enc', 'r').read()

for i in range (1649203200, 1649376000):
    text = ""
    libc.srand(i)
    for j in range(len(fl)):
        key = libc.rand() % 50
        text += chr(key ^ ord(fl[j]))

    if "anjay" in text: #karena flag format "anjay"
        print(text)
        break