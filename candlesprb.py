arr = [3, 2, 1, 3]
m = (max(arr))
c = 0
for i in range(len(arr)):
    if arr[i] == m:
        c += 1
print(c)
