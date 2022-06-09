def next_bigger(n):
    r = [int(x) for x in str(n)]
    w = [int(x) for x in str(n)]
    w.sort(reverse=True)
    print(w)
    print(r)
    if r == w:
        return -1
    else:
        new= []
        result= ""
        for i in range (len(r)-1, -1, -1):
            print(r[i])
            print(r[i-1])
            if r[i] == r[i-1] or r[i] < r[i-1]:
                new.append(r[i])
            elif r[i] > r[i-1]:
                new.append(r[i])
                new.sort()
                for j in range(0,len(new)):
                    print (i-1)
                    if r[i-1] < new[j]:
                        temp = r[i-1]
                        r[i-1] = new[j]
                        new[j] = temp
                        print(new)
                        final = r[:i]
                        for y in range(0,len(new)):
                            final.append(new[y])
                        for i in final:
                            result += str(i)
                        return int(result)
