n = int(input())
answer = [0]
result = []
arr = [i for i in range(1,n+1)][::-1]
flag_answer = []

for i in range(n):
    result.append(int(input()))

for i in result:
    flag = True
    while(True):
        if i == answer[-1]:
            flag_answer.append('-')
            answer.pop()
            break;
        if not arr:
            flag = False
            break;
        tmp = arr.pop()
        answer.append(tmp)
        flag_answer.append('+')
    if flag == False:
        break
    
if flag == False:
    print('NO')
else:
    for i in flag_answer:
        print(i)