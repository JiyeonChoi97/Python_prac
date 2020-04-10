# 파일 읽기1
f = open('test.txt', 'r')
text = f.read()             # 통째로 읽어옴
f.close()
print(text)

# 파일 읽기2
f = open('test.txt', 'r')
while True:
    line = f.readline()     # 한줄씩 읽기, 첫글자부터  개행문자(\n)까지 읽어옴
    if not line : break
    print(line, end='')
f.close()
print()

# 파일 읽기3
f = open('test.txt', 'r')
lines = f.readlines()       # 모든 라인을 읽어서, 각각의 라인을 리스트로 줌.
f.close()
print(lines)

for line in lines :
    print(line, end='')

print()

# 파일 읽기4
f = open('test.txt', 'r')

for line in f :             # f만 사용하면, 기본동작은 f.readlines()
    print(line, end='')
    
print()
f.close()