n = int(input())

dp = [0] + [1 for _ in range(n)]

for i in range(2,n+1):
    if (i ** 0.5) % 1 == 0.0:
        dp[i] = 1
        continue
    half = i // 2 + 1
    # half = (i ** 0.5) + 1
    min_count = float('inf')
    a = int(i ** 0.5)
    print("a=",a)
    while True:
        b = i - (a ** 2)
        min_count = min(min_count, dp[b] + 1)
        if half >= (a ** 2):
            break
        a -= 1
        # print(a)

    dp[i] = min_count


print(dp)
print(dp[n])
23 == 16 + 7