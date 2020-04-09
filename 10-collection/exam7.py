name = ['홍길동', '김철수', '이영희']
score = [[] for j in range(3)]   # 리스트 내포

print(score)

score[0].append(95)
score[0].append(75)
score[0].append(70)

score[1].append(88)
score[1].append(64)
score[1].append(70)

score[2].append(100)
score[2].append(95)
score[2].append(90)

tot=[0, 0, 0]
for a in range(len(tot)):
    tot[a] = sum(score[a])

for x in range(len(score)):
    print("{}, 총점={}, 평균={}".format(name[x], tot[x], tot[x]/3))

'''
홍길동, 총점=240, 평균=80.0
김철수, 총점=222, 평균=74.0
이영희, 총점=285, 평균=95.0
'''