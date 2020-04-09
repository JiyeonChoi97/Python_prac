for a in range(1, 100, 10):
    sum=0
    for b in range(a,a+10):
        sum+=b
    print('%2s~%3s=%3s' %(a, a+9, sum))


