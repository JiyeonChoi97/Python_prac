
while True:
    dan = int(input('몇 단을 출력할지 입력하시오 : '))
    for x in range(1,10):
        print('%s * %s = %s' %(dan, x, dan*x))
    choice= input('선택하시오(y:계속)')
    if choice != 'y': break


