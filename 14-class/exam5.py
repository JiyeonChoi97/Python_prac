'''멤버함수 사용하기'''

# 메소드1 : 인스턴스 메소드
class Calc:
    def plus(self, x, y):
        print('메소드 plus() 호출')
        return x + y
    
    def minus(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        return x / y
    
    def f(self, x, y):
        result1 = plus(x,y)
        result2 = self.plus(x,y)
        result3 = result1 + result2
        return result3
    
def plus(x, y):
    print('함수 plus() 호출')
    return x + y

c = Calc()
p = c.plus(100, 50)     # c.plus(c, 100, 50) 실제로 전달되는 모습
print(p)

print(c.minus(100, 50))
print(c.multiply(100, 50))
print(c.divide(100, 50))
print(c.f(100, 50))
print('-'* 30)

# 메소드2 : 스태틱 메소드
class Calc2:
    @staticmethod
    def plus(x, y):
        return x + y
    @staticmethod
    def minus(x, y):
        return x - y
    @staticmethod
    def multiply(x, y):
        return x * y
    @staticmethod
    def divide(x, y):
        return x / y

print(Calc2.plus(100, 50))      # 클래스명으로 사용
print(Calc2.minus(100, 50))
print(Calc2.multiply(100, 50))
print(Calc2.divide(100, 50))
print('-'* 30)

calc2 = Calc2()                 # 객체명으로 사용
print(calc2.plus(100, 50))      # @staticmethod 붙여서 사용해야함 
print(calc2.minus(100, 50))
print(calc2.multiply(100, 50))
print(calc2.divide(100, 50))
print('-'* 30)

# 메소드3 : 클래스 메소드
class Calc3:
    count = 0                   # 클래스 변수 
    
    @classmethod
    def plus(cls, x, y):
        return x + y
    @classmethod
    def minus(cls, x, y):
        return x - y
    @classmethod
    def multiply(cls, x, y):
        return x * y
    @classmethod
    def divide(cls, x, y):
        return x / y
    @classmethod
    def output(cls):
        print('count = ', cls.count)    # 클래스 변수 사용
        print('count = ', Calc3.count)  # 클래스 변수 사용

print(Calc3.plus(100, 50))      # 클래스명으로 사용
print(Calc3.minus(100, 50))
print(Calc3.multiply(100, 50))
print(Calc3.divide(100, 50))
print('-'* 30)

calc3 = Calc3()                 # 객체명으로 사용
print(calc3.plus(100, 50))      # @staticmethod 붙여서 사용해야함 
print(calc3.minus(100, 50))
print(calc3.multiply(100, 50))
print(calc3.divide(100, 50))
print('-'* 30)


'''
메소드 plus() 호출
150
50
5000
2.0
함수 plus() 호출
메소드 plus() 호출
300
------------------------------
150
50
5000
2.0
------------------------------
150
50
5000
2.0
------------------------------

'''