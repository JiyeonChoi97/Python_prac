'''멤버 변수만으로 클래스 만들기'''
class Character:
    name = 0        # 클래스 변수
    age = 0
    
d = Character()
d.name = '둘리'       # 인스턴스 변수
d.age = 19
print('이름 : ', d.name, ', 나이 : ', d.age)
print('-'*30)

print('이름 : ', Character.name, ', 나이 : ', Character.age)

Character.name = '길동'
Character.age = 40
print('이름 : ', Character.name, ', 나이 : ', Character.age)
print('-'*30)

h = Character()
h.name = '희동'
h.age = 3
print('이름 : ', h.name, ', 나이 : ', h.age)

'''
이름 :  둘리 , 나이 :  19
------------------------------
이름 :  0 , 나이 :  0
이름 :  길동 , 나이 :  40
------------------------------
이름 :  희동 , 나이 :  3
'''