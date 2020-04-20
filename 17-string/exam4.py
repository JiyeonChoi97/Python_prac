# 분리와 결합 관련

st1 = "He likes apples, she likes too"

# 공백문자 기준으로 분리, 결과값은 리스트로 리턴
st2 = st1.split()
print(st1)
print(st2)
print('-' * 30)

# 콤마(',') 기준으로 분리, 결과값은 리스트로 리턴
st2 = st1.split(',')
print(st1)
print(st2)
print('-' * 30)

# 공백문자 기준으로 2번만 분리, 결과값은 리스트로 리턴
# 왼쪽에서 오른쪽으로
st2 = st1.split(" ", 2)
print(st1)
print(st2)
print('-' * 30)

# 공백문자 기준으로 2번만 분리, 결과값은 리스트로 리턴
# 오른쪽에서 왼쪽으로
st2 = st1.rsplit(" ", 2)
print(st1)
print(st2)
print('-' * 30)

# 라인 기준으로 분리, 결과값은 리스트로 리턴
st3 = '''\
첫번째 줄
두번째 줄
세번째 줄'''
st2 = st3.splitlines()
print(st3)
print(st2)
print('-' * 30)

# 문자열 결합하기 
# 리스트의 문자열을 특정문자로 결합
st2 = st1.split()
print(st1)
print(st2)

st3 = ':'.join(st2)
print(st3, type(st3))














