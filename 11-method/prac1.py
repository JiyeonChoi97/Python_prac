def doubleNum(a, b):
    if a%b==0:
        return True
    else:
        return False
    
a = int(input('정수 입력 : '))
b = int(input('정수 입력 : '))

if doubleNum(a,b):
    print(str(a) + "(은)는 " + str(b) +"의 배수입니다.")
else:
    print(str(a) + "(은)는 " + str(b) +"의 배수가 아닙니다.")
    
'''
정수 입력 : 20

정수 입력 : 5
20(은)는 5의 배수입니다.
'''
'''
정수 입력 : 22

정수 입력 : 3
22(은)는 3의 배수가 아닙니다.
'''

