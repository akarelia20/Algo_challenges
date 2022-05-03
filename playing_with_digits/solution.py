def dig_pow(n, p):
    sum = 0
    j=0
    for i in str(n):
        x= int(i) ** (p+j)
        j+=1
        sum += x 
    if sum/n - int(sum/n) == 0: 
        return int(sum/n)
    else:
        return -1