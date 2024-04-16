n = int(input())

dp = [True,False,True,True]

for i in range(4,n):
    if (dp[i-1] and dp[i-3] and dp[i-4]) == False:
        dp.append(True)
    else:
        dp.append(False)

print(dp)
print(len(dp))

if dp[n-1] == True:
    print('SK')
else:
    print('CY')

