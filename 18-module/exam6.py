import calendar

# 달력 출력
print(calendar.calendar(2020))
print('-' * 30)

print(calendar.month(2020, 4))
print('-' * 30)

# 시작 요일과 일수 출력
a = calendar.monthrange(2020, 4)
print(a)
print('-' * 30)

if a[0]==0 : day = '월요일'
elif a[0]==1 : day = '화요일'
elif a[0]==2 : day = '수요일'
elif a[0]==3 : day = '목요일'
elif a[0]==4 : day = '금요일'
elif a[0]==5 : day = '토요일'
elif a[0]==6 : day = '일요일'
print('시작 요일 : {}, 일수 : {}'.format(day, a[1]))
print('-' * 30)

# 일주일의 시작요일 출력 및 설정
print('시작요일 :', calendar.firstweekday())
calendar.setfirstweekday(calendar.SUNDAY)
print('시작요일 :', calendar.firstweekday())
print(calendar.month(2020, 4))
print('-' * 30)

# 특정날짜의 요일출력
b = calendar.weekday(2020, 4, 15)
print(b)

if b==0 : day = "월요일"
elif b==1 : day = "화요일"
elif b==2 : day = "수요일"
elif b==3 : day = "목요일"
elif b==4 : day = "금요일"
elif b==5 : day = "토요일"
elif b==6 : day = "일요일"
print("2020년 4월 15일 {}".format(day))
print("------------")













