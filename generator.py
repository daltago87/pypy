'''
generator.py
2018/02/06
by daltago87
'''

#Generator 함수(Generator function)는 함수 안에 yield 를 사용하여 데이타를 하나씩 리턴하는 함수이다. 

#Generator 함수
def gen():
    yield 1
    yield 2
    yield 3
 
# Generator 객체
g = gen()
print(type(g))  # <class 'generator'>
 
# next() 함수 사용
n = next(g); print(n)  # 1
n = next(g); print(n)  # 2
n = next(g); print(n)  # 3
 
# for 루프 사용 가능
for x in gen():
    print(x)

#iterator 와 generator 의 차이
#리스트나 Set과 같은 컬렉션에 대한 iterator는 해당 컬렉션이 이미 모든 값을 가지고 있는 경우이나, Generator는 모든 데이타를 갖지 않은 상태에서 yield에 의해 하나씩만 데이타를 만들어 가져온다는 차이점이 있다.

# Generator Expression
g = (n*n for n in range(1001))
 
# g는 generator 객체
print(type(g))  # <class 'generator'>
 
# 리스트로 일괄 변환시
# mylist = list(g)
 
# 10개 출력
for i in range(10):
    value = next(g)
    print(value)
 
# 나머지 모두 출력 
for x in g:
    print(x)