MAX = 1000000000
TIME = 100000000

# nlogN

n,s = map(int,input().split())
a = list(map(int,input().split()))

# 1초 당 움직일 수 있는 최대 거리(D)를 찾아라
# 모든 동생을 찾기위해 D의 값을 정해야한다.
a.append(n)
a.sort()

tmp = []
for i in range(len(a)-1):
    tmp.append(a[i+1] - a[i])
print(a)
print(tmp)

#tmp중에서 제일 큰거부터 나머지 tmp로 나눠질 수 있는지,
# 다 나눠질 수 있으면 그게 제일 큰 값.

    
