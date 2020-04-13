class Car:
    def drive(self):
        self.speed = 10     # 클래스에 인스턴스 변수 추가 방법1
                            # -> 이 방법으로 변수를 추가할 경우, 
                            #    반드시 이 함수가 호출되어야만 한다.
        
    def output1(self):
        print('모델 : ', self.model)
        print('색상 : ', self.color)

    def output2(self):
        print('모델 : ', self.model)
        print('색상 : ', self.color)
        print('속도 : ', self.speed)
        
myCar = Car()
#myCar.output1() # error 발생. 아직 멤버변수 model, color가 없음
#myCar.output2() # error 발생. 아직 멤버변수 model, color, speed가 없음

# 클래스에 인스턴스 변수 추가 방법2
# -> myCar 객체에서만 사용 가능
myCar.model = 'E-Class'
myCar.color = 'Blue'
myCar.output1()
#myCar.output2() # error 발생. 아직 멤버변수 speed가 없음
print('-'*30)

myCar.drive()
myCar.output2()
print('-'*30)

print(myCar.model) # 객체명, 변수명으로도 사용할 수 있음 
print(myCar.color)
print(myCar.speed)

'''
모델 :  E-Class
색상 :  Blue
------------------------------
모델 :  E-Class
색상 :  Blue
속도 :  10
------------------------------
E-Class
Blue
10
'''