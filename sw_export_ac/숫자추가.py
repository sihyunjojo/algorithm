n,m,l = map(int,input().split())
arr = list(map(int,input().split()))
for _ in range(m):
    index, value = map(int,input().split())
    arr.insert(index, value)
print(arr[l])
