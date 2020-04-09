num1 = 5
num2 = 7.7
num3 = True

# + 결합
# 정수 + 실수 -> 실수
# 문자열 + 숫자 -> error
# 문자열 + str(숫자)
print(num1 + num2)
print("합 : " + str(num1+num2))
print('진실 : ' + str(num3))

# 문자열을 숫자로 바꾸기 : 문자열은 숫자로만 구성되어야 한다.
string1 = '123'
string2 = '5.567'
n1 = int(string1)
n2 = float(string2)
print(n1, type(n1))
print(n2, type(n2))


