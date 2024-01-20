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
# r =1
# while (b != a):
#     r += 1
#     temp = b
#     if b % 10 == 1:
#         b //= 10
#     elif b % 2 == 0:
#         b //= 2
#
#     if temp == b:
#         print(-1)
#         break
# else:
#     print(r)
# cnt=1
# while True:
#     if b%2==0:b=b//2;cnt+=1
#     elif b%10==1:b=(b-1)//10;cnt+=1
#     else:
#         if a!=b:cnt=-1;break
#     if a==b:break
#     if a>b:cnt=-1;break
# print(cnt)
print(dp[b])





