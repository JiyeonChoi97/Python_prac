def add(first=1, end=100):
    tot = 0        
    for x in range(first,end+1):
        tot += x
    return tot

print('1~100 사이의 함 : ', add())
print('30~100 사이의 함 : ', add(30))
print('20~200 사이의 함 : ', add(20,200))

'''
1~100 사이의 함 :  5050
30~100 사이의 함 :  4615
20~200 사이의 함 :  19910
'''