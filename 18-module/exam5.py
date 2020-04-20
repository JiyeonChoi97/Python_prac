from datetime import datetime

# 현재 시각 확인
print(datetime.now())
print('-' * 30)

# 년, 월, 일, 시, 분, 초 설정
d1 = datetime(2020, 10, 4, 20, 30, 30)
print(d1)
print("{}/{}/{}".format(d1.year, d1.month, d1.day))
print("{}:{}:{}".format(d1.hour, d1.minute, d1.second))
print("{:%Y/%m/%d %H:%M:%S}".format(d1))
print("{:%D}".format(d1))
print('-' * 30)

# 일 수 계산
day1 = datetime(2020, 1, 1)
day2 = datetime.now()
day_num = day2 - day1
print("일수 :", day_num)











