num1 = float(input('첫 번째 수 : '))
num2 = float(input('두 번째 수 : '))
op = input('연산자 : ')

if op == '+' : result = num1 + num2
elif op == '-' : result = num1 - num2
elif op == '*' : result = num1 * num2
elif op == '/' : result = num1 / num2

print('%s %s %s = %s' %(num1, op, num2, result))