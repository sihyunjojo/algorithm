import math
s = int(input())

MAX = 200000000

log  = math.sqrt(s)
n2 = s*s
n3 = s*s*s

print(log * 200 <= MAX)