def digital_root(n):
    result= 0
    result2=0
    while n >0: 
        remainder = n % 10
        result= result + remainder
        n = n//10
    print (result)
    if len(str(result)) > 1:
        result2= digital_root(result)
        return result2    
    else:
        return result