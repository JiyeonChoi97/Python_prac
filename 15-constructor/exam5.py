#아나콘다의 라이브러리 폴더의 위치
#- 내장 라이브러리 : C:\Users\ezen\anaconda3\Lib
#- 설치한 라이브러리 : C:\Users\ezen\anaconda3\Lib\site-packages

# 모듈 선언
from random import random
from random import randint
from random import randrange
from random import sample

# 0.0~1.0미만의 임의 실수값 1개 생성
print(random())

# 시작~끝 사이의 임의 정수값 1개 생성
# 0~9 임의 정수값 생성
print(randint(0,9))

# 시작~끝 사이의 임의 정수값 1개 생성
# 스텝값을 지정할 수 있다. 
print(randrange(0,9,3))

# 임의의 문자 생성
# 소문자 아스키 코드 : 97~122
# 대문자 아스키 코드 : 65~90
print(chr(randint(65,90)))
print(chr(randint(97,122)))

# 리스트에서 임의값을 선택 추출하기
print(sample([1,2,3,4,5], 2))
# 1~45 사이의 정수 6개 추출
li = [a for a in range(1, 46)]
print(li)
print(sample(li, 6))
