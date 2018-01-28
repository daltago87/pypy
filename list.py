'''
list.py
2018/01/28
by daltago87
'''

a = [1,2,3]
print(a)
print(a[0]+a[1])
print(a[-1])
print(a[-2])

b = [1,2,3, ['a', 'b', 'c']]
print(b[-1])

c = [1,2,3]
c[2] = 4
print(c)

"c[1:2] = ['a','b','c']"
c[1] = ['a','b','c']
print(c)

'c[1] = []'
del c[1]
print(c)

d = [1,2,3]
d.append([5,6])
print(d)

e=[5,3,4,2,1]
print(e)
e.sort()
print(e)
e.reverse()
print(e)
e.pop()
print(e)

f=[1,2,3]
f.extend([4,5])
print(f)