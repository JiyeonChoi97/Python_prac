dic = {'a':1, 'b':2, 'c':'Hello', 'd':'파이썬'}

print(dic)
print('='*30)

# 인덱싱
print(dic['a'])
print(dic['b'])
print(dic['c'])
print(dic['d'])
print('='*30)

# 키값만 읽어오기
dic_key = dic.keys()
print(dic_key)
print('='*30)

# value값만 읽어오기
dic_value = dic.values()
print(dic_value)
print('='*30)

# key, value 쌍으로 읽어오기
dic_item = dic.items()
print(dic_item)
print('='*30)

# 데이터 추가
dic['phone'] = '010-1234-5678'
print(dic)
print('='*30)

# 데이터 1개 삭제
del(dic['b'])
print(dic)
print('='*30)

# 모든 데이터 삭제
dic.clear()
print(dic)
print('='*30)

test = {}
print(type(test))
test2 = {1}
print(type(test2))
test3 = {1:2}
print(type(test3))

'''
{'a': 1, 'b': 2, 'c': 'Hello', 'd': '파이썬'}
==============================
1
2
Hello
파이썬
==============================
dict_keys(['a', 'b', 'c', 'd'])
==============================
dict_values([1, 2, 'Hello', '파이썬'])
==============================
dict_items([('a', 1), ('b', 2), ('c', 'Hello'), ('d', '파이썬')])
==============================
{'a': 1, 'b': 2, 'c': 'Hello', 'd': '파이썬', 'phone': '010-1234-5678'}
==============================
{'a': 1, 'c': 'Hello', 'd': '파이썬', 'phone': '010-1234-5678'}
==============================
{}
==============================
<class 'dict'>
<class 'set'>
<class 'dict'>
'''










