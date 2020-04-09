korea = int(input('국어 점수 입력 : '))
eng = int(input('영어 점수 입력 : '))

sum = korea + eng
avg = sum /2

print('총점 = %s' %sum)
print('평균 = %s' %avg)

if avg>=90 : print('학점 = A')
elif avg>=80 : print('학점 = B')
elif avg>=70 : print('학점 = C')
elif avg>=60 : print('학점 = D')
else : print('학점 = F')
