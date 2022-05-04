def max_sequence(arr):
    sum= 0
    max_sum = 0
    for i in range(0,len(arr)):
        sum = sum + arr[i]
        if sum < 0:
            sum = 0
        if sum > max_sum:
            max_sum = sum
    return max_sum