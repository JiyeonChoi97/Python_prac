dic = {101: '사과', 102:'복숭아', 103:'감', 104:'바나나'}
print(dic)
print('-'*30)

# 리스트 형태로 변환해서 사용
list_keys = list(dic.keys())
print(dic.keys(), type(dic.keys()))
print(list_keys, type(list_keys))
print('-'*30)

list_values = list(dic.values())
print(dic.values(), type(dic.values()))
print(list_values, type(list_values))
print('-'*30)

list_items = list(dic.items())
print(list_items, type(list_items))
print('-'*30)

'''
{101: '사과', 102: '복숭아', 103: '감', 104: '바나나'}
------------------------------
dict_keys([101, 102, 103, 104]) <class 'dict_keys'>
[101, 102, 103, 104] <class 'list'>
------------------------------
dict_values(['사과', '복숭아', '감', '바나나']) <class 'dict_values'>
['사과', '복숭아', '감', '바나나'] <class 'list'>
------------------------------
[(101, '사과'), (102, '복숭아'), (103, '감'), (104, '바나나')] <class 'list'>
------------------------------
'''


