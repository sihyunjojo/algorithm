a, b= map(int,input().split())
dp = {b:-1}

def go(n, count):
    if n > b:
        return
    dp[n] = count
    # if list(dp.keys()).count(n) == 1:
    #     dp[n] = min(dp[n], count)

    go(int(str(n)+"1"), count+1)
    go(n * 2, count+1)

go(a,1)


# print(dp)

# print(dp)
# print(list(dp.keys()).count(21));
print(dp[b])





