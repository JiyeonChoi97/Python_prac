# 검색 관련
st1 = "He likes apples, she likes too"

# 문자열에 특정 단어의 갯수 구하기
print(st1)
print(st1.count('like'))
print('-' * 30)

# 문자열에서 왼쪽에서 오른쪽으로 특정 문자열의 위치 구하기
# find
print(st1)
print(st1.find('like', 10))
print(st1.find('love'))
print('-' * 30)

# 문자열에서 오른쪽에서 왼쪽으로 특정 문자열의 위치 구하기
print(st1)
print(st1.rfind('like'))
print(st1.rfind('love'))
print('-' * 30)

# 문자열에서 왼쪽에서 오른쪽으로 특정 문자열의 위치 구하기
# index
# 없는 단어를 찾으면 error 발생
try :
    print(st1)
    print(st1.index('like', 10))
    print(st1.index('love')) 
except :
    print('그런 단어 없음')
print('-' * 30)

# 문자열에서 오른쪽에서 왼쪽으로 특정 문자열의 위치 구하기
# rindex
# 없는 단어를 찾으면 error 발생
try :
    print(st1)
    print(st1.rindex('like'))
    print(st1.rindex('love')) 
except :
    print('그런 단어 없음')
print('-' * 30)

# 시작되는 단어인지 검사
print(st1)
print(st1.startswith('likes'))
print(st1.startswith('likes', 3))
print('-' * 30)

# 끝나는 단어인지 검사
print(st1)
print(st1.endswith('likes'))
print(st1.endswith('likes', 0, 26))
print('-' * 30)





