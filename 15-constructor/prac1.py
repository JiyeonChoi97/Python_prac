class Triangle :
    def __init__(self, b=0, h=0):
        self.b = b
        self.h = h
        
    def setTriangle(self, b, h):
        self.b = b
        self.h = h
    
    def getArea(self):
        return self.b *  self.h /2
        
t1 = Triangle(45, 7)
print('삼각형의 넓이 : ', t1.getArea())

t2 = Triangle()
t2.setTriangle(5,12)
print('삼각형의 넓이 : ', t2.getArea())

'''
삼각형의 넓이 :  157.5
삼각형의 넓이 :  30.0
'''