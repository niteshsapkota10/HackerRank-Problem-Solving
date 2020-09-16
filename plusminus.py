arr = [-4, 3, -9, 0, 4, 1]

pos_count = 0
neg_count = 0
zerocount = 0

for i in range(len(arr)):
    if arr[i] > 0:
        pos_count += 1
    elif arr[i] < 0:
        neg_count += 1
    else:
        zerocount += 1
print("{0:.6f}".format(pos_count/len(arr)))
print("{0:.6f}".format(neg_count/len(arr)))
print("{0:.6f}".format(zerocount/len(arr)))
