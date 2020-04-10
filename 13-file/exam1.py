# 파일 열기 -> 파일 객체 생성
f = open('test.txt', 'w')   # 쓰기 모드
# 파일에 데이터 저장
for i in range(1,11):
    data = str(i) + '번째 줄입니다.\n'
    f.write(data)

# 파일 닫기
f.close()

print('쓰기완료')
