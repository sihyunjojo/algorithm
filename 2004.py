MAX = 2000000000

print('time: ', 200000000 >= MAX * 2 )

def count_2(n):

n,m = map(int,input().split())

# def fac(n):
#     if n == 1:
#         return 1
#     return n * fac(n-1)


# #    2*5가 몇개 들어이나 확인해보면 되겠네.

# tmp_1 = 1
# tmp_2 = 1
# for i in range(m+1,n+1):
#     tmp_1 *= i

# for i in range(1,n-m+1):
#     tmp_2 *= i


# print(tmp_1 == fac(n) // fac(m))
# print(tmp_2 == fac(n-m))
# print(tmp_2)

# result = tmp_1/tmp_2
# print(result)

# # result = fac(n)// (fac(m) * fac(n-m))

# cnt = 1
# for i in range(len(str(result))):
#     tmp = 10 ** cnt
#     if result % cnt == 0:
#          cnt += 1
#     else:
#         print(cnt - 1)
#         break

