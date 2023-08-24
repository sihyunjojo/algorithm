a = int(input())
n = 2

while(a > 1):
    if a % n == 0:
        a /= n
        print(n)
    else:
        n += 1
