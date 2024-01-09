n,m = map(int,input().split())

arr = []


def per(count):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(count,n+1):
        arr.append(i)
        per(i)
        arr.pop()


per(1)