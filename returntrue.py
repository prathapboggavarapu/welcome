def common_data(xlist,ylist):
    for i in xlist:
        for j in ylist:
            if i == j:
                result = True
                return result


print(common_data([1,2,3,4,5],[5,6,7,8,9]))