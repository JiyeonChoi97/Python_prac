class Triangle():
    def setTriangle(self, b, h):
        self.b = b
        self.h = h
    
    def getArea(self):
        return self.b *  self.h /2
        
print('**** 삼각형 넓이 구하기 ****')
b = int(input('밑변 : '))
h = int(input('높이 : '))

t = Triangle()
t.setTriangle(b, h)

print('삼각형의 넓이 : ', t.getArea())

'''
**** 삼각형 넓이 구하기 ****
밑변 : 10
높이 : 20
삼각형의 넓이 :  100.0
'''