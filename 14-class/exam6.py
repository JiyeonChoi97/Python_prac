# 다른 파일에 포함된 명령어를 사용하는 방법1
# import 파일명
import calcurator

c = calcurator.Calc()       # 클래스명 앞에 파일이름을 붙인다. 
print(c.plus(100, 50))
print(c.minus(100, 50))
print(c.multiply(100, 50))
print(c.divide(100, 50))
print(c.f(100, 50))
print('-'*30)

# 다른 파일에 포함된 명령어를 사용하는 방법2
# from 파일명 import 클래스명 또는 함수
from calcurator import Calc

c = Calc()                  # 클래스명 앞에 파일이름을 붙이지 않는다. 
print(c.plus(100, 50))
print(c.minus(100, 50))
print(c.multiply(100, 50))
print(c.divide(100, 50))
print(c.f(100, 50))

'''
150
50
5000
2.0
5150
------------------------------
150
50
5000
2.0
5150
'''