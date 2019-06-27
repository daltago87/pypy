'''
dictionary.py
2018/01/28
by daltago87


'''

dic = {'name':'sophia', 'phone':'01041307623', 'birth':'0704'}
print(dic['name'])
print(dic.get('name'))
print(dic.get('notkey'))
print(dic.get('notkey', 'test'))

dic_keys = dic.keys()
print(dic_keys)

for k in dic_keys:
    print(k)

print(list(dic.keys()))

dic_values = dic.values()
for v in dic_values:
    print(v)

dic_items = dic.items()
for i in dic_items:
    print(i)


print('name' in dic)
print('test' in dic)

for k,v in dic.items():
    print(k + '_' + v)
    