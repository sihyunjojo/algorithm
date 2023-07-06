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

tmp = []
for i in range(len(a)-1):
    tmp.append(a[i+1] - a[i])
tmp.sort()
print('a = ',a)
print('tmp = ', tmp)

#logn
def GCD(x,y):
    while(y):
        x,y=y,x%y
    return x

# tmp들의 최대공약수 구하기
# tmp * tmp

def tmp_GCD(tmp):
    while tmp:
        if len(tmp) == 1:
            return tmp
        temp = []
        for i in range(len(tmp)-1):
            print(tmp[i],tmp[i+1],GCD(tmp[i],tmp[i+1]))
            temp.append(GCD(tmp[i],tmp[i+1]))
        tmp = temp

print(tmp_GCD(tmp).pop())
        

    
        
    
    
for i in range(min(tmp),0,-1):
    flag = 0
    for j in tmp:
        if j % i != 0:
            flag = 1
    if flag == 0:
        print(i)
        break;


# tmp들의 약수

#tmp중에서 제일 작은거부터 시작 ~ 1까지
# tmp가 다 나눠질 수 있으면 
