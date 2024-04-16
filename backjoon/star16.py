# cnt = int(input())

# for i in range(cnt):
#     print(' '*(cnt-i-1),end='');
#     print('*',end='');
#     for j in range(i):
#         print(' '+'*',end='');
#     print("")

cnt = int(input())
for i in range(1,cnt+1):
    print((cnt-i)*" "+ '*' + " *"*(i-1))