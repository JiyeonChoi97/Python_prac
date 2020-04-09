'''
아이덴티티 연산자
is : 레퍼런스 변수의 주소값이 같은지 검사
    --> 연산 결과는 True 또는 False
    --> True : 레퍼런스 값이 같음
    --> False : 레퍼런스 값이 다름
is not : 레퍼런스 변수의 주소값이 같은지 검사
    --> 연산 결과는 True 또는 False
    --> True : 레퍼런스 값이 다름
    --> False : 레퍼런스 값이 같음
'''

a = 1
b = 2
c = 1
d = a

print('a is b : ', a is b)
print('a is c : ', a is c)
print('a is d : ', a is d)

print('id(a) : ', id(a))
print('id(b) : ', id(b))
print('id(c) : ', id(c))
print('id(d) : ', id(d))

print('a is not b : ', a is not b)
print('a is not c : ', a is not c)
print('a is not d : ', a is not d)



