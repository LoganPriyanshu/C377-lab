s = 'aabbccddee'
d = {}
for i in s:
    if i in d:
        d[i] += 1
        continue
    d[i] = 1
key = ''
flag = 0
count = 1
for i in d.keys():
    if d[i]==1:
        key = i
        flag = 1
        break
if flag == 1:
    for i in s:
        if i == key:
            print(count)
            break
        count += 1
else:
    print(-1)        