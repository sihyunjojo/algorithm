import itertools
n,m = map(int,input().split())

a = itertools.permutations(list(i for i in range(1,n+1)),m)

for i in a:
    print(*i,sep=" ")
