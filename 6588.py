import sys
input = sys.stdin.readline

MAX = 1000000
case = 100,000
print(50000000 < 1000000//2 * 100000)


#소수 고르기 소수 ==True
arr = [True for i in range(MAX+1)]
print(len(arr))
for i in range(2, int(MAX**1/2)+1):
    j = 2
    while i * j <= MAX:
        arr[i*j] = False
        j += 1


n = int(input())
while n != 0:
    flag = 0
    for i in range(3, int(n/2+1)):
        print(i,arr[i])
        if arr[i] == True and arr[n-i] == True:
            flag = 1
            print(n,' = ',i," + ",n-i)
            break;
    if flag == 0:
        print("\"Goldbach's conjecture is wrong.\" ")

    n = int(input())


    


    