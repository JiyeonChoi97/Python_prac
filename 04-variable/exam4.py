# 위치값 '0123456' -> 양수로 위치값 표시
#       '7654321' -> 음수로 위치값 표시
st1 = 'abcdefg'

# 인덱싱 : [k] -> 특정 위치의 문자 1개 읽기
print('st1 = ', st1)
print('st1[0] = ', st1[0])
print('st1[3] = ', st1[3])
print('st1[6] = ', st1[6])
print('st1[-1] = ', st1[-1])
print('st1[-4] = ', st1[-4])
print('st1[-7] = ', st1[-7])
print('-' * 30)

# 슬라이싱 : [s:t] -> s부터 t앞부분 문자열 추출
print('st1 = ', st1)
print('st1[1:4] = ', st1[1:4])  # 1~3
print('st1[:4] = ', st1[:4])    # 0~3
print('st1[1:] = ', st1[1:])    # 1~
print('st1[-3:-1] = ', st1[-3:-1])    # -3~-2
print('st1[:-1] = ', st1[:-1])    # 0~-2
print('st1[-3:] = ', st1[-3:])    # -3~
print('-' * 30)

# 문자열의 길이
print(len(st1))

# 특정 위치의 문자 변경
#st1[0] = 'x' ----> 인덱싱으로 문자 변경 불가
print('st1 = ', st1)
st2 = 'x' + st1[1:]
print('st2 = ', st2)



