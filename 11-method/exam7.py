# 매개변수에 *를 붙이면, 전달되는 값은 튜플이 된다.
def total(*args):
    tot = 0
    for a in args:
        tot += a
    return tot
    
print('total(2, 4, 6, 8, 10) : ', total(2, 4, 6, 8, 10))
print('total(20, 45, 67) : ', total(20, 45, 67))
print('total(20) : ', total(20))







