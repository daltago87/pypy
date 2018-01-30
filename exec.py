'''
exec.py
2018/01/30
by daltago87
'''

from mylib import *

i = add(10,20)
print(i)
j = substract(20,5)
print(j)

'''
import models.account.bill
models.account.bill.charge(1, 50)

# 모듈안의 모든 함수 import
# from 패키지명 import 모듈명
from models.account import bill
bill.charge(1, 50)
 
# 특정 함수만 import
# from 패키지명.모듈명 import 함수명
from models.account.bill import charge
charge(1, 50)
'''
from models.account import *
bill.charge(1, 50)