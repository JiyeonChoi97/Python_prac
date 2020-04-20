# 모듈 사용 방법 1
# import 폴더명.모듈명
import modules.my_module2

modules.my_module2.my_func2()
print('-' * 30)

# 모듈 사용 방법 2
# import 폴더명.모듈명 as 별명
import modules.my_module2 as my2

my2.my_func2()
print('-' * 30)

# 모듈 사용 방법 3
# from 폴더명.모듈명 import 함수명 또는 클래스명
from modules.my_module2 import my_func2

my_func2()
print('-' * 30)

# 모듈 사용 방법 4
# from 폴더명.모듈명 import 함수명 또는 클래스명
from modules.my_module2 import my_func2 as mf2

mf2()







