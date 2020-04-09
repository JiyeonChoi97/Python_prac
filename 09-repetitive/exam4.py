#방법1
total = 0
i = 1

while i<=10:
    total += i
    i += 1
    
print('sum = ',total)

#방법2
total = 0
i = 1

while True:
    if i>10 : break
    total += i
    i += 1
    
print('sum = ',total)




