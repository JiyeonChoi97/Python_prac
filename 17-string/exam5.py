# 정렬
st1 = "He likes apples, she likes too"

# 가운데 마춤
st2 = st1.center(50)
print(st1)
print(st2 + 'ttt')
print('-' * 30)

# 오른쪽 마춤
st2 = st1.rjust(50)
print(st1)
print(st2 + 'ttt')
print('-' * 30)

# 왼쪽 마춤
st2 = st1.ljust(50)
print(st1)
print(st2 + 'ttt')
print('-' * 30)

# 왼쪽 마춤
st2 = st1.ljust(50, '-')
print(st1)
print(st2 + 'ttt')
print('-' * 30)

# 탭문자(\t)를 8자 공백문자로 사용
st3 = '1\t2345\t6'
print(st3)
print(len(st3))

st4 = st3.expandtabs()
print(st4)
print(len(st4))
print('-' * 30)














