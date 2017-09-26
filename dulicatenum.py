def remove_duplicates(t):
    xlist=[]

    for i in t:
        if not i in xlist:
            xlist.append(i)
    return xlist



print remove_duplicates(['a', 'b', 'b', 'd'])
