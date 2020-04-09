stadium = input('경기장은 어디입니까? ')
winner = input('이긴 팀은 어디입니까? ')
loser = input('진 팀은 어디입니까? ')
score = input('스코어는 몇대몇 입니까?')
print('=' * 30)
result='''\
오늘 %s에서 야구경기가 열렸습니다.
%s과 %s의 치열한 공방전이 펼쳤습니다.
결국 %s은 %s를 %s로 이겼습니다. \
''' %(stadium, winner, loser, winner, loser, score)
print(result)
print('=' * 30)

print("오늘 %s에서 야구경기가 열렸습니다." %stadium)
print('%s과 %s의 치열한 공방전이 펼쳤습니다.' %(winner, loser))
print('결국 %s은 %s를 %s로 이겼습니다. ' %(winner, loser, score))
print('=' * 30)
