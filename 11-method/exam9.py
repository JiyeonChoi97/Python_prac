def calc_area(r):
    # 전역변수를 사용하기 위해서는 전역변수 선언을 먼저해야 함
    global area
    area = 3.14 * r**2
    
area = 0
r = float(input('원의 반지름 : '))
calc_area(r)
print('원의 넓이 : ', area)

'''
원의 반지름 : 5
원의 넓이 :  78.5
'''
