from datetime import date

# 오늘 날짜 확인
print(date.today())
print('-' * 30)

# 년, 월, 일 설정
d = date(2020, 10, 4)
print(d)
print("{}/{}/{}".format(d.year, d.month, d.day))
print('-' * 30)

# 일수 계산 (1/1~오늘까지 총 일수)
day1 = date(2019, 12, 31)
day2 = date(2020, 12, 31)
#day2 = date.today()
day_num = day2 - day1
print("일수 :", day_num)
