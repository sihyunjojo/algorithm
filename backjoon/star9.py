cnt = int(input())
for i in range(cnt):
    print(' '*(i) + '*' * (2*(cnt-i)-1))
for j in range(1,cnt):
    print(' ' * (cnt-j-1) + '*' * (j*2+1))