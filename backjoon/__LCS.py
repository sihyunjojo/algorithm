s1 = ' ' + input()
s2 = ' ' + input()

MAX = 10000000 # 천만
print(MAX >= 1000000)

max_len = max(len(s1),len(s2))

dp = [[0 for _ in range(max_len)] for _ in range(max_len)]

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp)


