class CalcParent1:
    def __init__(self):
        self.aa = 5
        self.bb = 7
    def plus(self, x, y):
        return x+y
    def minus(self, x, y):
        return x-y

class CalcParent2:
    def __init__(self):
        self.aa2 = 50
        self.bb2 = 70
    def plus(self, x, y):
        return x+y+1
    def minus(self, x, y):
        return x-y-1
    
class CalcChild (CalcParent1, CalcParent2):
    def multiply(self, x, y):
        return x*y
    def divide(self, x, y):
        return x/y
    def output(self):
        print(self.aa)
        print(self.bb)
        #print(self.aa2)
        #print(self.bb2)

child = CalcChild()
print(child.plus(200, 100))
print(child.minus(200, 100))
print(child.plus(200, 100))
print(child.minus(200, 100))
print(child.multiply(200, 100))
print(child.divide(200, 100))
print('-'*40)
child.output()
print(child.aa)
print(child.bb)

'''
300
100
300
100
20000
2.0
----------------------------------------
5
7
5
7
'''