def largenum( list ):
    max = list[ 0 ]
    for i in list:
        if i > max:
            max = i
    return max
print(largenum([1, 8, -8, 0]))
