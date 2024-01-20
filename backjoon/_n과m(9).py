n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr = []
# visited = [False] * n
arr1 = []
dp = []
def per(count):
    if len(arr) == m:
        dp.append(arr[:])
        print(* arr)
        return
    for i in range(n):
        if i not in arr1:
            arr.append(nums[i])
            arr1.append(i)
            per(i)
            arr.pop()
            arr1.pop()

per(0)
print(dp)
dp = sorted(list(set(map(tuple,dp))))
print(dp)

for i in dp:
    print(*i)

