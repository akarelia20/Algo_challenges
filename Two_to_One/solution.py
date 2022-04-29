def longest(a1, a2):
    str = sorted (sorted(a1)+ sorted(a2))
    new_str = ""
    for i in str:
        if i not in new_str:
            new_str+= i
    return new_str