a,b = map(int,input().split())

arr = [i for i in range(1,a+1)][::-1]
tmp = []
answer = []
cnt = 0
print(arr)

while arr:
    while arr:
        cnt += 1
        if arr and cnt != b:
            tmp.append(arr.pop())
        elif arr and cnt == b:
            answer.append(arr.pop())
            cnt = 0
    arr = tmp[::-1]
    tmp = []
    print(arr)
print(answer)
print('<' , end="")
for i in answer[:-1]:
    print(str(i)+', ', end='')
print(answer[-1],end='')
print('>')
