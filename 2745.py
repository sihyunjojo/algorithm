N,B = input().split()
cnt = len(N) - 1
answer = 0
for i in N:
    if i.isnumeric():
        answer += int(i) * (int(B) ** cnt)
    if i.isupper():
        answer += (ord(i) - 55) * (int(B) ** cnt)
    print('cnt',cnt)
    print('곱해지는 뒤에' , int(B)**cnt)
    cnt -= 1

print(answer)

