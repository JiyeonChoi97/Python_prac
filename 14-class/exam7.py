class Score:
    def set(self):
        print(self)
        self.num = int(input('학번 : '))
        self.name = input('이름 : ')
        self.kor = int(input('국어 : '))
        self.eng = int(input('영어 : '))
        self.mat = int(input('수학 : '))
        self.tot = self.kor + self.eng + self.mat
        self.avg = self.tot / 3
        
    def output_title(self):
        print(self)
        print('*** 성적 출력 ***')
        print('%3s %6s %3s %3s %3s %3s %3s'  %(
            '학번', '이름', '국어', '영어', '수학', '총점', '평점'))
        
    def output(self):
        print(self)
        print('%3s %6s %3s %3s %3s %3s %3s'  %(
            self.num, self.name, self.kor, self.eng, self.mat, self.tot, self.avg))
        
s1 = Score()
s2 = Score()
print("s1 = ", s1)
print("s2 = ", s2)
print('-'*30)

s1.set()    # s1.set(s1) : 멤버함수를 호출하면, 호출하는 객체가 전달
s2.set()    # s2.set(s2) : 멤버함수를 호출하면, 호출하는 객체가 전달
s1.output_title()
s1.output()
s2.output()

'''
s1 =  <__main__.Score object at 0x0000021CB641E048>
s2 =  <__main__.Score object at 0x0000021CB641E188>
------------------------------
<__main__.Score object at 0x0000021CB641E048>

학번 : 1

이름 : 홍길동

국어 : 90

영어 : 80

수학 : 70
<__main__.Score object at 0x0000021CB641E188>

학번 : 2

이름 : 고길동

국어 : 80

영어 : 70

수학 : 60
<__main__.Score object at 0x0000021CB641E048>
*** 성적 출력 ***
 학번     이름  국어  영어  수학  총점  평점
<__main__.Score object at 0x0000021CB641E048>
  1    홍길동  90  80  70 240 80.0
<__main__.Score object at 0x0000021CB641E188>
  2    고길동  80  70  60 210 70.0
'''