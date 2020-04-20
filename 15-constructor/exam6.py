from random import sample

class Lotto:
    def lotto_ran(self):
        li = [a for a in range(1, 46)]
        li2 = sorted(sample(li, 6), reverse=True)
        
        for a in range(1, 7):
            print('%2s' %li2.pop(), end=' ')

num= int(input('구매 횟수를 입력하세요 : '))

lotto = Lotto()
for i in range(1, num+1):
    lotto.lotto_ran()
    print()
    
'''
구매 횟수를 입력하세요 : 5
 4 10 24 29 33 45 
19 23 29 35 38 45 
 6  7 17 29 36 39 
13 15 18 32 33 39 
14 20 22 39 40 41 
'''