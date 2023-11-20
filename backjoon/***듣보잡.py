import sys

n,m = map(int,sys.stdin.readline().split())
no_listen = set(sys.stdin.readline().strip() for i in range(n))
no_watch = set(sys.stdin.readline().strip() for i in range(m))

result = [i for i in no_listen if i in no_watch]


print(len(result))
print(*sorted(result),sep="\n")

