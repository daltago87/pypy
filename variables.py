'''
variables.py
'''

a = 3
print(type(3))

import sys
print(sys.getrefcount(3))
a = 3
print(sys.getrefcount(3))
b = 3
print(sys.getrefcount(3))
c = 3
print(sys.getrefcount(3))


b = 4
c = 5
print(b)
print(c)
b, c = c, b
print(b)
print(c)

d = [1,2,3]
e = d

d[1] = 4

print(d)
print(e)

f = [1,2,3]
'g =  f[:]'
from copy import copy
g = copy(f)

f[1] = 4

print(f)
print(g)

print(f is g)