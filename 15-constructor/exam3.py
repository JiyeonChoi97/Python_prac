class Member:
    def __init__(self, name=0, age=0):
        self.name = name
        self.age = age
    
    # setter : 변수에 데이터 저장
    def setName(self, name):
        self.__name = name
        def getAge(self):
            return self.__age

    def setAge(self, age):
        self.__age = age
    
mem = Member() # mem.__init__()
#print(mem.__name)  ==> error 발생, private 변수이기 때문에
#print(mem.__age)  
print(mem.getName())
print(mem.getAge())

#값 변경
mem.setName('홍길동')
mem.setAge(25)
print(mem.getName())
print(mem.getAge())
print('-'*30)


# 인스턴스 변수 추가
# -> 클래스 밖에서는 __를 붙여도 public으로 동작함
mem.__name = '이영화'
mem.__age = 30

print(mem.__name)
print(mem.__age)
print('-'*30)
print(mem.getName())
print(mem.getAge())
print('-'*30)