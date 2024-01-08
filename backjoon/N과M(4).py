n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

print(nums)
arr = []


def per():
    if len(arr) == m:
        print(*arr)
        return
    for i in nums:
        if i not in arr:
            arr.append(i)
            per()
            arr.pop()


per()
