# 문자열의 특성 유무 확인
# 결과값은 True, False로 나옴
st1 = '1234'
st2 = 'HelloPython'
st3 = 'Hello Python'
st4 = '홍길동'
st5 = '1234abcd'

# 문자열이 숫자만으로 구성되었는 지 확인
print(st1)
print(st2)
print(st1.isdigit())
print(st2.isdigit())
print('-' * 30)

# 문자열이 문자만으로 구성되었는 지 확인
print(st1)
print(st2)
print(st3)
print(st4)
print(st1.isalpha())
print(st2.isalpha())
print(st3.isalpha())
print(st4.isalpha())
print('-' * 30)

# 문자열이 숫자와 문자로 구성되었는 지 확인
print(st1)
print(st2)
print(st3)
print(st5)
print(st1.isalnum())
print(st2.isalnum())
print(st3.isalnum())
print(st5.isalnum())
print('-' * 30)

# 문자열이 소문자인지 확인
st6 = st2.lower()
print(st2)
print(st6)
print(st2.islower())
print(st6.islower())
print('-' * 30)

# 문자열이 대문자인지 확인
st6 = st2.upper()
print(st2)
print(st6)
print(st2.isupper())
print(st6.isupper())
print('-' * 30)

# 단어의 첫글자가 대문자인지 확인
st6 = st2.title()
print(st2)
print(st6)
print(st2.istitle())
print(st6.istitle())
print('-' * 30)







