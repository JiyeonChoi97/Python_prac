class HelloWorld:
    message = 0                               # 클래스 변수
    def setEng(self):
        self.message = 'Hello Python'   # 인스턴스 변수
        
    def setKor(self):
        self.message = '안녕하세요. 파이썬'
        
    def setKor2(self):
        message = '파이썬 파이팅!!!'      # 지역 변수
        
    def sayHello(self):
        print(self.message)
        
hello = HelloWorld()
# 메소드 호출
hello.setEng()
hello.sayHello()
print('-'*30)

hello.setKor()
hello.sayHello()
print('-'*30)

hello.setKor2()
hello.sayHello()
print('-'*30)

print(hello.message)
print(HelloWorld.message)

'''
Hello Python
------------------------------
안녕하세요. 파이썬
------------------------------
안녕하세요. 파이썬
------------------------------
안녕하세요. 파이썬
0
'''