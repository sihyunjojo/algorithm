cnt = int(input())

for i in range(1,cnt+1):
    for j in range(cnt-i):
        print(" ",end="");
    for k in range(i):
        print("*",end="");
    print();
for i in range(cnt-1,0,-1):
    for j in range(cnt-i):
        print(" ",end="");
    for k in range(i):
        print("*",end="");
    print();
