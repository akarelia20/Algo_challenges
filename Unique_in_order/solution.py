def unique_in_order(arg):
    list = []
    for i in arg:
        if len(list) == 0 or list[len(list)-1] != i :
            list.append(i)        
    return list