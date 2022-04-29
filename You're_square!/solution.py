def is_square(n):
    for i in range(n+1): 
        if i * i > n: 
            return False
        elif i * i == n:
            return True
    return False