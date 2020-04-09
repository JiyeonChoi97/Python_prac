monthList = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print('*** 일수 구하기 ***')
year = int(input('년 : '))

if (year%4 ==0) and (year%100!=0) or (year%400==0):
    monthList[2] = 29;

month = int(input('월 : '))
day = int(input('일 : '))

sum = 0
for x in monthList[:month]:
    sum += x

sum += day
print('1월 1일부터 %s월 %s일까지는 %s일 입니다' %(month, day, sum))


