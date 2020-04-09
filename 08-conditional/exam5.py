# if 삼항 연산식 사용 : 문자열이 회문인가?
# 회문? 왼쪽에서 읽었을 때와 오른쪽으로 읽었을때 같은 문자열

a = 'abcdcba'
print(a, ': 회문' if a==a[::-1] else ': 회문아님')

# if-else 사용
if a==a[::-1]:
    print(a, ': 회문')
else:
    print(a, ': 회문 아님')

'''
b = 'abcdefg'
print(b[1:4])
print(b[4:1:-1])
print(b[:4])
print(b[1:])
print(b[:])
print(b[::-1])
'''
