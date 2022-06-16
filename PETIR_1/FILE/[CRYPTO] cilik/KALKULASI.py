import gmpy2
from Crypto.Util.number import *
import random

c = 64370826219196693215525738278997084836250364144145087945488252034046370347129763699235756806845841623679802290054958371405384431222042372642769501377229428877300227374798208978565131190542920086065786726026703453551058295286771959711776368555490419235574299710349

print(gmpy2.iroot(c,5))
m = long_to_bytes(36453381165083966928610392291879089439557149699039869)
# m hasil akar pangkat 5 dari nilai c

print('m =', m)