# nlogn 
n = int(input())

dp = [0] + [1] + [100 for i in range(n-1)]
dp_sq =[i*i for i in range(1000)]

for i in range(2,n+1):
    cnt = 1 #제곱 늘려줄 
    num = i #실제 빼기 당할 수 
    while True:
        if num > dp_sq[cnt]:
            cnt += 1
        elif num == dp_sq[cnt]:
            dp[i] = 1
            break;
        elif num < dp_sq[cnt]:
            for j in range(cnt,0,-1):
                dp[i] = min(dp[dp_sq[j-1]] + dp[num - dp_sq[j-1]], dp[i])
                if n == num:
                    print(dp[i],dp_sq[j-1],dp[j])
            break;
            
            
print(dp)

print(dp[n])


