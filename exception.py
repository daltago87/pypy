'''
exception.py
2018/02/02
by daltago87
'''

def calc(values):
    sum = None

    try:
        sum = values[0] +  values[1] + values[2]
    except IndexError as err:
        print('인덱스 에러')
    except Exception as err:
        print(str(err))
    else:
        print('에러없음')
    finally:
        print(sum)


calc([1,2,3,6])
calc([1,2])

'with 는 c#의 using 과 같음'
with open('test.txt', 'r') as fp:
    lines = fp.readlines()
    print(lines)