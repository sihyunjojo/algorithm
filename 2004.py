n,m = map(int,input().split())

def count_a(a,n):


print(count_a(2,8)) #7
print(min(count_a(2,n)-count_a(2,m)-count_a(2,n-m),count_a(5,n)-count_a(5,m)-count_a(5,n-m)))
