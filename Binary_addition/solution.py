def add_binary(a,b):
    num = a + b
    result= ""
    while num > 0:
        remainder = num % 2
        num = num//2
        result= str(remainder) + result
    return result   
