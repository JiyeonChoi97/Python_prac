class Gugudan:
    def setGugudan(self, start, end):
        self.start = start
        self.end = end        
        
    def dispGugudan(self):
        for j in range(self.start, self.end+1):
            for i in range(1, 10):
                print('%s*%s=%2s' %(j, i, j*i), end=' ')
            print()

gugudan = Gugudan()

s = int(input('시작단 : '))
e = int(input('끝단 : '))

gugudan.setGugudan(s, e)
gugudan.dispGugudan()

'''
시작단 : 3
끝단 : 7
3*1= 3 3*2= 6 3*3= 9 3*4=12 3*5=15 3*6=18 3*7=21 3*8=24 3*9=27 
4*1= 4 4*2= 8 4*3=12 4*4=16 4*5=20 4*6=24 4*7=28 4*8=32 4*9=36 
5*1= 5 5*2=10 5*3=15 5*4=20 5*5=25 5*6=30 5*7=35 5*8=40 5*9=45 
6*1= 6 6*2=12 6*3=18 6*4=24 6*5=30 6*6=36 6*7=42 6*8=48 6*9=54 
7*1= 7 7*2=14 7*3=21 7*4=28 7*5=35 7*6=42 7*7=49 7*8=56 7*9=63
'''