'''
comprehension.py
2018/02/06
by daltago87
'''


#List Comprehension
#[출력표현식 for 요소 in 입력sequence if 조건식]

oldlist = [1, 2, 'A', False, 3]
newlist = [ i*i for i in oldlist if type(i) == int]

print(newlist)


#Set Comprehension
#{출력표현식 for 요소 in 입력sequence if 조건식}

oldset = [1, 1, 2, 3, 3, 4]
newset = {i*i for i in oldset if type(i) == int}

print(newset)

# Dictionary Comprehension
#{Key:Value for 요소 in 입력Sequence if 조건식}

id_name = {1: '박진수', 2: '강만진', 3: '홍수정'}
name_id = {val:key for key,val in id_name.items()}

print(name_id)

def isodd(val):
    return val % 2 == 1

mydict = {x:x*x for x in range(101) if isodd(x)}
print(mydict)