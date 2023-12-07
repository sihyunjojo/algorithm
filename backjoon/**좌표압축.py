from collections import deque

n = int(input())
arr = list(map(int,input().split()))


sorted_arr = sorted(list(set(arr)))

#index() = O(n)
#**
dict = {sorted_arr[i]: i for i in range(len(sorted_arr))}

result = []


for i in arr:
    result.append(dict[i])

print(*result,sep=" ")


