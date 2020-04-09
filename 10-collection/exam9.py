tup1 = (10, 20, (30, 40, 50))
tup2 = ('c언어', 'python', 'java', 'jsp')

print(tup1)
print(tup2)
print('-' * 30)

# 인덱싱 : 데이터 1개 관리
print(tup1[0])
print(tup1[2])
print(tup1[2][1])
print('-' * 30)

# 슬라이싱 : 데이터 여러개 관리
print(tup2[1:3])
print(tup2[:3])
print(tup2[1:])
print('-' * 30)

# step 추가
print(tup2[::2])
print(tup2[1::2])
print('-' * 30)

'''
(10, 20, (30, 40, 50))
('c언어', 'python', 'java', 'jsp')
------------------------------
10
(30, 40, 50)
40
------------------------------
('python', 'java')
('c언어', 'python', 'java')
('python', 'java', 'jsp')
------------------------------
('c언어', 'java')
('python', 'jsp')
------------------------------
'''
