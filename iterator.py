'''
iterator.py
2018/02/06
by daltago87
'''

'리스트, Set, Dictionary와 같은 컬렉션이나 문자열과 같은 문자 Sequence 등은 for 문을 써서 하나씩 데이타를 처리할 수 있는데, 이렇게 하나 하나 처리할 수 있는 컬렉션이나 Sequence 들을 Iterable 객체(Iterable Object)라 부른다'
mylist = [1,2,3]
it = iter(mylist) #Iterable 객체의 iterator 리턴


'''
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
'''

#또는

#print(next(it))
#print(next(it))
#print(next(it))
#print(next(it))


class MyCollection:
    def __init__(self):
        self.size = 10
        self.data = list(range(self.size))

    def __iter__(self): #어떤 클래스를 Iterable 하게 하려면, 그 클래스의 iterator를 리턴하는 __iter__() 메서드를 작성해야 한다.
        self.index = 0
        return self
    
    def __next__(self): #어떠한 경우든 Iterator가 되는 클래스는 __next()__ 메서드 (Python 2 인 경우 next() 메서드) 를 구현해야 한다. 
        if self.index >= self.size:
            raise StopIteration
        
        n = self.data[self.index]
        self.index += 1
        return n

coll = MyCollection()
for x in coll:
    print(x)