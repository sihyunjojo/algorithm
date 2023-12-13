n,r,c = map(int,input().split())
count = 0
#분할시 n과r과c(입력값)를 직접 +-하여서 활용하면 좋다.
# 2 3 1 -> 11
# 3 7 7 -> 63

# 2 1
while n != 0:
    n -= 1

    if r < 2 ** n and c < 2 ** n:
        count += (2**n) * (2**n) * 0
    elif r < 2 ** n and c >= 2 ** n:
        count += (2**n) * (2**n) * 1
        c -= (2**n)
    elif r >= 2 ** n and c < 2 ** n:
        count += (2**n) * (2**n) * 2
        r -= (2**n)
    else:
        count += (2**n) * (2**n) * 3
        r -= (2**n)
        c -= (2**n)

print(count)




# board = list([0 for _ in range(n)] for _ in range(n))
# two_ze = [2**i for i in range(n)]
#
# # 무조건 x가 증가하는데
# #x 가 2의 배수고 y 가 홀수 일때는 왼쪽 아래로 조건만큼 가주고
# #x가  2의 배수고 y가 짝수일때는 조건만큼 위로 가주네
#
# def z(x,y):
#     x_flag, y_flag = 0, 0
#     if x in two_ze:
#         x_flag = x ** 1/2
#     if y in two_ze:
#         y_flag = y ** 1/2
#     if x_flag != 0 and y_flag != 0:
#         return x+1, y + (y_flag ** 2) - 1
#     elif x_flag != 0 and y_flag == 0:
#         return x - (x_flag ** 2) + 1, y+1
#     elif x_flag == 0 and y_flag != 0:
#         return x+1, y
#     else:
#         return x+1, y
#
# stack = [(0,0)]
# count = 0
#
# while stack:
#     x,y = stack.pop()
#     dx, dy = z(x,y)
#     count += 1
#     print(dx,dy)
#     if dy == r and dx == c:
#         break
#     stack.append(z(dx,dy))
#
#
# print(count)
#


