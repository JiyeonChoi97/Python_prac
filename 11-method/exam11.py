# 일반 함수 
def square1(x):
    return x**2

print(square1(5))
print('-'*30)

# 람다 함수 1
square2 = lambda x : x**2
print(square2(3))
print('-'*30)

# 람다 함수 2
print((lambda x : x**2)(4))

'''
25
------------------------------
9
------------------------------
16
'''