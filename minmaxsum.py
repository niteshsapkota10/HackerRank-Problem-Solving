arr = [1, 2, 3, 4, 5]
sumarr = 0
addarr = []
a = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if j == a:
            continue
        sumarr += arr[j]
    addarr.append(sumarr)
    sumarr = 0
    a += 1
print(min(addarr))
print(max(addarr))
