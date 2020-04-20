import random

class Lotto:
    def __init__(self):
        self.m = 0          # 로또번호 1세트 저장
        self.buyNum = 0     # 구매회수 저장
        
    def inputBuyNum(self):
        self.buyNum= int(input('구매 횟수를 입력하세요 : '))
        
    # 번호 생성, 정렬
    def selectLotto(self):
        for i in range(0, self.buyNum):
            self.m = random.sample([a for a in range(1, 46)], 6)
            self.m.sort()
            self.outputResult() 
            
    def outputResult(self):
        for a in range(0, 6):
            print('%2s' %self.m[a], end=' ')
        print()
            

lotto = Lotto()
lotto.inputBuyNum()
lotto.selectLotto()

'''
구매 횟수를 입력하세요 : 5
 4 10 24 29 33 45 
19 23 29 35 38 45 
 6  7 17 29 36 39 
13 15 18 32 33 39 
14 20 22 39 40 41 
'''