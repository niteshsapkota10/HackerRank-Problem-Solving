alice=[17,28,30]
bob=[99,16,8]
def comparetriplets(a,b):
    points=[0,0]
    for i in range(len(a)):
        if a[i]>b[i]:
            points[0]+=1
        elif a[i]<b[i]:
            points[1]+=1
    return points

print(comparetriplets(alice,bob))