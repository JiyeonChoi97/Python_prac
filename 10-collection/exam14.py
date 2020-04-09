dic = {'a':1, 'b':2, 'c':'Hello', 'd':'파이썬'}

print(dic)
print('='*30)

print('{} {} {} {}'.format(*dic)) ## key값만 읽어들임
print('{a} {b} {c} {d}'.format(**dic)) ## value값만 읽어들임

'''
{'a': 1, 'b': 2, 'c': 'Hello', 'd': '파이썬'}
==============================
a b c d
1 2 Hello 파이썬
'''









