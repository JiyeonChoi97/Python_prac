a = {1, 2, 3}
b = {1, 2, 3, 3}

print(a, len(a))
print(b, len(b))
print('-'* 30)

# 데이터 추가
a.add(5)
print(a, len(a))
print('-'* 30)

# 개별 데이터 확인
# --> 인덱싱으로 확인 안됨, error 발생
# print(a[0])

# 1. for문
for v in a :
    print(v, end=' ')

print()
print('-'* 30)

# 2. pop : 확인한 데이터는 삭제됨
print(a, len(a))
print(a.pop())
print(a, len(a))
print('-'* 30)

# 데이터 유무 확인
print(2 in a)
print(2 not in a)

'''
{1, 2, 3} 3
{1, 2, 3} 3
------------------------------
{1, 2, 3, 5} 4
------------------------------
1 2 3 5 
------------------------------
{1, 2, 3, 5} 4
1
{2, 3, 5} 3
------------------------------
True
False
'''