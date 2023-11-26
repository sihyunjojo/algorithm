n = int(input())
arr = sorted(set(list(input() for _ in range(n))))

arr_len = [[] for i in range(len(max(arr, key=lambda a: len(a)))+1)]

print(arr)

for i in arr:
    arr_len[len(i)].append(i)

print(arr_len)

for i in arr_len:
    for j in i:
        print(j)

