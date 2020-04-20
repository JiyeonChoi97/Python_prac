# 생성자1
class Car :
    # 생성자 : 객체가 생성될 때, 자동으로 호출되는 특수한 메솓
    def __init__(self, speed, color, model):
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

myCar = Car(0, 'blue', 'E-class') # myCar.__init__(0, 'blue', 'E-class')
myCar.output()
myCar.drive(60)
myCar.output()

'''
생성자 실행됨
속도 :  0
색상 :  blue
모델 :  E-class
속도 :  60
색상 :  blue
모델 :  E-class
'''