from Crypto.Util.number import *
import random

file = open('flag.txt', 'rb')
m = bytes_to_long(file.read())

p = getPrime(512)
q = getPrime(512)
n = p * q
e = 5

c = pow(m, e, n)
print('n =', n)
print('e =', e)
print('c =', c)