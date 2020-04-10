def grade(avg):
    if avg>=90: return 'A'
    elif avg>=80: return 'B'
    elif avg>=70: return 'C'
    elif avg>=60: return 'D'
    else : return 'F'
    
def inputJumsu():
   kor = int(input('국어 점수 입력 : '))
   eng = int(input('영어 점수 입력 : '))
   return kor, eng
 
def calc(kor, eng):
    tot = kor + eng
    return tot/2

def output(avg):
    print(grade(avg), '학점입니다.')
    

kor, eng = inputJumsu()
avg = calc(kor, eng)
output(avg)

'''
국어 점수 입력 : 78

영어 점수 입력 : 75
C 학점입니다.
'''