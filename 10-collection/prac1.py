jumsu = []

for i in range(1,6):
    jumsu.append(int(input(str(i) + '번 학생의 점수를 입력 : ')))


tot = 0
for i in jumsu:
    tot += i

print('총점 : ', tot, ', 평균 : ', tot/len(jumsu))


