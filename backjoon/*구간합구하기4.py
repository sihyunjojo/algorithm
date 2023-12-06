n,m = map(int,input().split())
arr = [0]
for i in input().split():
    arr.append(arr[-1] + int(i))
for _ in range(m):
    start, end = map(int, input().split())
    print(arr[end]-arr[start-1])


