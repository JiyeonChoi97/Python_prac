students = []

with open('test.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        # '\n'처리    -> '\n' 지우기
        line = line.replace('\n', '')
        #print(line.split(','))
        students.append(line.split(','))

print('students:')
print(students)

for student in students:
    name, kor, eng, mat = student
    tot = int(kor) + int(eng) + int(mat)
    avg = tot/3
    result = '''\
        이름: {}, 국어: {}, 영어: {}, 수학: {}, 총점: {}, 평균: {:.1f}'''.format(name, kor, eng, mat, tot, avg)
    print(result)

'''
students:
[['홍길동', '90', '80', '72'], ['고길동', '85', '75', '96'], ['이영희', '87', '82', '96']]
        이름: 홍길동, 국어: 90, 영어: 80, 수학: 72, 총점: 242, 평균: 80.7
        이름: 고길동, 국어: 85, 영어: 75, 수학: 96, 총점: 256, 평균: 85.3
        이름: 이영희, 국어: 87, 영어: 82, 수학: 96, 총점: 265, 평균: 88.3
'''
