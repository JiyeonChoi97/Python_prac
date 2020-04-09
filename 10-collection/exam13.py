dic = {'a':1, 'b':2, 'c':'Hello', 'd':'파이썬'}

print(dic)
print('='*30)

# key값 유무 확인
print('c' in dic)
print('Hello' in dic)
print('='*30)

# data 유무 확인은 안됨
#print(dic['a'] in dic)

# 개별 데이터 확인
# 1. 인덱싱
# 2. get() 함수 
print(dic['a'])
print(dic.get('c'))
print('='*30)

#print(dic['f'])        --> error 발생, 없는 키값 사용
print(dic.get('f'))   # --> None 발생, 없는 키값 사용
print('='*30)

# for문으로 데이터 처리
for key in dic.keys():
    print(key, dic[key], end=', ')

print('='*30)

for value in dic.values():
    print(value, end=' ')
print()
print('='*30)

for key, value in dic.items():
    print(key, value, end=', ')
print()
print('='*30)

# 정렬
for key in sorted(dic.keys()): # 오름차순 정렬
    print(key, dic[key], end=', ')
print()
print('='*30)   

for key in sorted(dic.keys(), reverse=True): # 내림차순 정렬
    print(key, dic[key], end=', ')
print()
print('='*30)   

# 데이터 갯수 확인
print(len(dic), '개')
print('='*30)

# 데이터 추가
# 데이터 1개 추가
dic['e']='빅데이터'
print(dic)
print('='*30)
# 데이터 여러개 추가
dic.update({'f':'머신러닝', 'g':'딥러닝'})
print(dic)
print('='*30)

'''
{'a': 1, 'b': 2, 'c': 'Hello', 'd': '파이썬'}
==============================
True
False
==============================
1
Hello
==============================
None
==============================
a 1, b 2, c Hello, d 파이썬, ==============================
1 2 Hello 파이썬 
==============================
a 1, b 2, c Hello, d 파이썬, 
==============================
a 1, b 2, c Hello, d 파이썬, 
==============================
d 파이썬, c Hello, b 2, a 1, 
==============================
4 개
==============================
{'a': 1, 'b': 2, 'c': 'Hello', 'd': '파이썬', 'e': '빅데이터'}
==============================
{'a': 1, 'b': 2, 'c': 'Hello', 'd': '파이썬', 'e': '빅데이터', 'f': '머신러닝', 'g': '딥러닝'}
==============================
'''
