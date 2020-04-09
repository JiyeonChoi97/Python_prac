a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8, 9, 10}

c = a.intersection(b)   # 교집합
d = a.union(b)          # 합집합
e = a.difference(b)     # 차집합

print(a)
print(b)
print(c)
print(d)
print(e)

'''
{1, 2, 3, 4, 5}
{4, 5, 6, 7, 8, 9, 10}
{4, 5}
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
{1, 2, 3}
'''