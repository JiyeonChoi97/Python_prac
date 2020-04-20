'''\
문자열 도움말입니다.
문서 문자열은 각 블럭의 첫줄에 위치함.
by hong
'''

class AAA :
    '안녕하세요. AAA 클래스입니다.'
    
    def ex(self) :
        '안녕하세요 ex 메소드 입니다.'
        pass
    
print(__doc__)
print(AAA.__doc__)
print(AAA.ex.__doc__)
