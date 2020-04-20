# 생성자2 : 디폴트 매개변수 설
class Car :
    # 생성자 : 객체가 생성될 때, 자동으로 호출되는 특수한 메솓
    def __init__(self, speed=0, color=0, model=0):
        print('생성자 실행됨')
        self.speed = speed
        self.color = color
        self.model = model
        
    def drive(self, speed):
        self.speed = speed
        
    def output(self):
        print('속도 : ', self.speed)
        print('색상 : ', self.color)
        print('모델 : ', self.model)

myCar = Car(10, 'blue', 'E-class')
myCar.output()

myCar2 = Car(10, 'yellow')
myCar2.output()

myCar3 = Car(20)
myCar3.output()

myCar4 = Car()
myCar4.output()

myCar4.__init__(100, 'red', 'D-class')
myCar4.output()

