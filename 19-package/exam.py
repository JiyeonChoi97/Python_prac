# 패키지 사용 방법 1
# import 패키지명.모듈명
import packages.image.io_file.imgRead

packages.image.io_file.imgRead.pngRead()
packages.image.io_file.imgRead.jpgRead()
print('-' * 30)

# 패키지 사용 방법 2
# import 패키지명.모듈명 as 별명
import packages.image.io_file.imgRead as img

img.pngRead()
img.jpgRead()
print('-' * 30)

# 패키지 사용 방법 3
# from 패키지명 import 모듈명
from packages.image.io_file import imgRead

imgRead.pngRead()
imgRead.jpgRead()
print('-' * 30)

# 패키지 사용 방법 4
# from 패키지명 import 모듈명 as 별명
from packages.image.io_file import imgRead as img1

img1.pngRead()
img1.jpgRead()
print('-' * 30)

# 패키지 사용 방법 5
# from 패키지명.모듈명 import 함수명 또는 클래스명
from packages.image.io_file.imgRead import pngRead
from packages.image.io_file.imgRead import jpgRead

pngRead()
jpgRead()
print('-' * 30)

# 패키지 사용 방법 6
# from 패키지명.모듈명 import 함수명 또는 클래스명
from packages.image.io_file.imgRead import pngRead as png
from packages.image.io_file.imgRead import jpgRead as jpg

png()
jpg()








