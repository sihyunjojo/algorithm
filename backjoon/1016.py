import math
min,max = map(int,input().split())


cnt = 1

a = [ i ** 2 for i in range(2,math.sqrt(max) + 1)]
dp = []