'''
클래스에 클래스 변수, 인스턴스 변수 사용하기
- 클래스 변수와 인스턴스 변수는 완전히 별개이다. 이름이 같더라도 각각 따로 만들어진다.
- 클래스 변수는 프로그램이 시작될 때, 메모리에 만들어진다.
- 인스턴스 변수는 객체가 생성된 이후에 메모리에 만들어진다.
'''

class Car:
    speed = 5               # 클래스에 클래스 변수 추가
    
    def drive(self):
        self.speed = 10     # 클래스에 인스턴스 변수 추가
    
    def output(self):
        print('Car.speed = ', Car.speed)
        print('self.speed = ', self.speed)

print(Car.speed)
print('-' *30)

myCar = Car()
myCar.output()
print('-' *30)

myCar.drive()
myCar.output()
print('-' *30)

'''
5
------------------------------
Car.speed =  5
self.speed =  5
------------------------------
Car.speed =  5
self.speed =  10
------------------------------
'''
