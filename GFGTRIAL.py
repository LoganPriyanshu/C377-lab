# n = int(input())
# l = [int(x) for x in input().split()]
# # hm = {}
# count = 0
# for i in range(n):
#     for j in range(i+1 , n):
#         if l[i]+l[j] >= l[i]*l[j]:
#             count += 1
# print(count)
        
# n = int(input())
# l = [int(x) for x in input().split()]
# k = int(input())
# l.sort()
# # l1 = []
# c = 0
# if k in l:
#     for i in l:
#         if i <= k:
#             c += 1
#     print(c)
# else:
#     print(0)
# print(c)
# def compute_hcf(x, y):
#    while(y):
#        x, y = y, x % y
#    return x

# a , b = map(int,input().split())
# hcf = compute_hcf(a,b)
# print((a//hcf)+(b//hcf))
def MaxActivities(arr, n):
    selected = []
    l.sort(key = lambda x : x[1])
    i = 0
    selected.append(arr[i])
 
    for j in range(1, n):

      if arr[j][0] >= arr[i][1]:
          selected.append(arr[j])
          i = j
    return selected

n = int(input())
l = []
m = 0
for i in range(n):
    a , b = map(int,input().split())
    l.append([a,b])
selected = MaxActivities(l, n)
print(selected)


