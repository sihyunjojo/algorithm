n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr = []
print(nums)


def per(count):
    if len(arr) == m:
        print(*arr)
        return
    # for i in nums[count:]:
    for i in range(count + 1, n):
        arr.append(nums[i])
        # print('a',i,count)
        # arr.append(i)
        per(i - 1)
        arr.pop()


print(nums[0:])
per(-1)
