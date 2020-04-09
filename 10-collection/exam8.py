tup1 = (10, 20, 30, 40, 50)
tup2 = ('c언어', 'python', 'java', 'jsp')
tup3 = ('파이썬', )

print('tup1 = ', tup1, type(tup1))
print('tup2 = ', tup2, type(tup2))
print('tup3 = ', tup3, type(tup3))

print('=' * 30)

print(tup1[0])
#tup1[0] = 1  --> error 발생, 데이터변경 안됨

tup1.append(60)
#print(tup1)  --> error 발생, 데이터추가 안됨 

