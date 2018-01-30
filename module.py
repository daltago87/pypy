'''
module.py
2018/01/30
by daltago87
'''

import math
n = math.factorial(5)
print(n)

# factorial 함수만 import > 모듈명.함수명 대신 함수명만 사용가능
from math import factorial 
m = factorial(5) / factorial(3)
print(m)


# 여러 함수를 import
from math import (factorial,acos)
a = factorial(3) + acos(1)
 
# 모든 함수를 import
from math import *
b = sqrt(5) + fabs(-12.5)

import sys
sys.path
print(sys.path[0])