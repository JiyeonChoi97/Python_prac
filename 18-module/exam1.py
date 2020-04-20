# 모듈 사용법 1
# import 모듈명
import my_module1

my_module1.my_func()
print('-' * 30)

# 모듈 사용법 2
# import 모듈명 as 별명
import my_module1 as my1

my1.my_func()
my_module1.my_func()
print('-' * 30)

# 모듈 사용법 3
# from 모듈명 import 함수명 또는 클래스명
from my_module1 import my_func

my_func()
print('-' * 30)

# 모듈 사용법 4
# from 모듈명 import 함수명 또는 클래스명 as 별명
from my_module1 import my_func as mf

mf()










