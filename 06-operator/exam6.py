'''
논리연산자
<진리표>
x       y       x and y    x or y     not x
True   True     True       True       False
True   False    False      True       False
False  True     False      True       True
False  False    False      False      True
'''

r1 = 100 >= 200
r2 = 5 >= 3

print(r1 and r2)
print(r1 or r2)
print(not(r1 or r2))



