jumsu = []

for i in range(1,6):
    jumsu.append(int(input(str(i) + '번 학생의 점수를 입력 : ')))

jumsu2 = []
jumsu2 = (sorted(jumsu, reverse=True))

print('*** 결과 ***')
for i in range(0,5):
    print(jumsu[i], '점 : ',jumsu2.index(jumsu[i])+1, '등')


