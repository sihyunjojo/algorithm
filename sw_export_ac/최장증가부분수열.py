T = int(input())
for test_case in range(1, T + 1):
    result = 0
    count = int(input())
    arr = list(map(int, input().split()))

    dp = [1 for i in range(count)]

    for i in range(count):
        for j in range(i):
            # print(i,j)
            if arr[i] > arr[j]:
                dp[i] = max(dp[j]+1, dp[i])
                # print(arr[i],arr[j],dp[i])

    result = max(dp)
    print(max(dp))
    print('#' + str(test_case), result)

