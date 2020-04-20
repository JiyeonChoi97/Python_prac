class CalcParent:
    def plus(self, x, y):
        return x+y
    def minus(self, x, y):
        return x-y

class CalcChild (CalcParent):
    def multiply(self, x, y):
        return x*y
    def divide(self, x, y):
        return x/y
    

calcP = CalcParent()
print(calcP.plus(100, 50))
print(calcP.minus(100, 50))
print('-'*40)

calcP = CalcChild()
print(calcP.plus(100, 50))
print(calcP.minus(100, 50))
print(calcP.multiply(100, 50))
print(calcP.divide(100, 50))

'''
150
50
----------------------------------------
150
50
5000
2.0
'''