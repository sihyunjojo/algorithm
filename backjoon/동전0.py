n, k = map(int, input().split())
arr = list(int(input()) for _ in range(n))

cnt = 0
for i in reversed(range(n)):
    cnt += k//arr[i]
    k = k % arr[i]

print(cnt)
