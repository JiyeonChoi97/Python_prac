num = int(input('1~100 사이의 배수를 구할 숫자 입력 : '))

count = 0
for x in range(1,101):
    if x%num == 0:
        print(x, end=' ')
        count+=1

print('')
print('1~100 사이의 %s의 배수 개수 = %s' %(num, count))