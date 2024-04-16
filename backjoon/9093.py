n = input()
for i in range(int(n)):
    s = list(input().split())
    for i in s:
        print(i[::-1],end =" ")
    print()