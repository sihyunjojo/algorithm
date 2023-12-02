n = int(input())
arr = list(map(int,input().split()))

result = 0

arr.sort()

for i in range(n):
    result += (n-i) * arr[i]

print(result)
