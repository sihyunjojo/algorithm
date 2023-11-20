import math
MAX = 1000000000
TIME = 10000000

print(TIME > math.log(MAX))
#logn

n,s = map(int,input().split())
a = list(map(int,input().split()))

# 1초 당 움직일 수 있는 최대 거리(D)를 찾아라
# 모든 동생을 찾기위해 D의 값을 정해야한다.
a.append(s)
a.sort()

place = []
for i in range(len(a)-1):
    place.append(a[i+1] - a[i])
# place.sort()

#logn
def GCD(x,y):
    while(y):
        x,y= y, x%y
    return x

#logn * 10^5
def arr_GCD(arr):
    if len(arr) == 1:
        return arr[0]
    result = GCD(arr[0],arr[1])
    for i in range(2,len(arr)):
        result = GCD(result,arr[i])
    return result 

# tmp들의 최대공약수 구하기
# tmp * tmp

# print(place)
print(arr_GCD(place))
# print(*[123.213,123]) 

#tmp중에서 제일 작은거부터 시작 ~ 1까지
# tmp가 다 나눠질 수 있으면 
