n = int(input())

arr = [i for i in range(1,n+1)]

start = 1
end = 1
cnt = 1
total = 1
while(end != n):
    if total == n:
        cnt += 1
        end += 1
        total += end
    elif total < n:
        end += 1
        total += end
    elif total > n:
        total -= start
        start += 1
    print('st',start,'end',end,'total',total)

print(cnt)
