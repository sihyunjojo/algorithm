n, m = map(int, input().split())
nums = sorted(set(map(int, input().split())))

arr = []
print(nums)

def per(count):
    if m == len(arr):
        print(* arr)
        return
    for i in range(count,len(nums)):
        arr.append(nums[i])
        per(i)
        arr.pop()

print(len(nums))
per(0)
