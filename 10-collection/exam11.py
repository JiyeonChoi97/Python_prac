tup1 = (1,2,3,4,5)
list1 = [10,20,30,40,50]

print("{} {} {} {}".format(*tup1))
print("{} {} {} {}".format(*list1))


print("{1} {2} {3} {4}".format(*tup1))
print("{4} {2} {3} {1}".format(*list1))

# 일반 변수에 튜플 저장하기
# unpacking : 튜플의 데이터 개수와 변수의 개수는 일치해야 한다.
a, b, c, d, e = tup1
print(a, b, c, d, e)

# a, b, c, d = tup1 --> 개수 일치(x)
print(a, b, c, d)

'''
1 2 3 4
10 20 30 40
2 3 4 5
50 30 40 20
1 2 3 4 5
1 2 3 4
'''