n = int(input())
l = [i for i in input().split()]
# for i in range(n):
#     l.append(input())
ind = int(input())
i = ind
target = input()
count = 0
while True:
    if i == len(l):
        i = 0
    if l[i] == target:
        print(count)
        break
    i += 1
    if l[ind] == target:
        print(count)
        break
    ind -= 1
    count += 1


