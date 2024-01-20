from collections import deque

n = int(input())

board = list(list(input()) for _ in range(n))
v = [[False] * n for _ in range(n)]

count,rg_count = 0,0
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

stack = deque()


def bfs(y, x):
    stack.append((y, x))
    v[y][x] = True
    while stack:
        y, x = stack.popleft()
        # v[y][x] = True

        for d in delta:
            dx = x + d[0]
            dy = y + d[1]
            if 0 <= dx < n and 0 <= dy < n:
                if board[dy][dx] == board[y][x] and not v[dy][dx]:
                    v[dy][dx] = True
                    stack.append((dy, dx))


for i in range(n):
    for j in range(n):
        if not v[i][j]:
            bfs(i, j)
            count += 1

v = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 'R':
            board[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not v[i][j]:
            bfs(i, j)
            rg_count += 1

print(count, rg_count)


# n = int(input())
#
# board = list(list(input()) for _ in range(n))
# v = [[False] * n for _ in range(n)]
#
# print(board)
#
# count = 0
# rg_count = 0
# delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# # visited = "Black"
#
# def bfs(y, x):
#     stack = deque([(y, x)])
#     while stack:
#         y, x = stack.popleft()
#         color = board[y][x]
#         v[y][x] = True
#
#         for d in delta:
#             dx = x + d[0]
#             dy = y + d[1]
#             if 0 <= dx < n and 0 <= dy < n:
#                 if board[dy][dx] == color and not v[dy][dx]:
#                     stack.append((dy, dx))
#
#
# for i in range(n):
#     for j in range(n):
#         if not v[i][j]:
#             bfs(i,j)
#             count += 1
#
# v = [[False] * n for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         if not v[i][j]:
#             bfs(i,j)
#             rg_count += 1
#
#
#
#
#
# for y in range(n):
#     for x in range(n):
#         if not v[y][x]:
#             stack = deque([(y, x)])
#
#             while stack:
#                 y, x = stack.popleft()
#                 color = board[y][x]
#                 # board[y][x] = visited
#                 v[y][x] = True
#
#                 for d in delta:
#                     dx = x + d[0]
#                     dy = y + d[1]
#                     if 0 <= dx < n and 0 <= dy < n:
#                         if board[dy][dx] == color and not v[dy][dx]:
#                             stack.append((dy, dx))
#             count += 1
#
# for i in range(n):
#     for j in range(n):
#         if board[i][j] == 'R':
#             board[i][j] = 'G'
#
# v = [[False] * n for _ in range(n)]
#
#
# for i in range(n):
#     for j in range(n):
#         if not v[j][i]:
#             stack = deque([(j, i)])
#             print(j,i)
#             for k in board:
#                 print(k)
#             for p in v:
#                 print(p)
#             color = board[j][i]
#             print(color)
#             while stack:
#                 y, x = stack.popleft()
#                 # color = board[y][x]
#                 # board[y][x] = visited
#                 v[y][x] = True
#
#                 for d in delta:
#                     dx = x + d[0]
#                     dy = y + d[1]
#                     if 0 <= dx < n and 0 <= dy < n:
#                         if board[dy][dx] == color and not v[dy][dx]:
#                             print(color)
#                             stack.append((dy, dx))
#
#             # while stack:
#             #     y, x = stack.popleft()
#             #     v[y][x] = True
#             #
#             #     # print(color,y,x)
#             #     for d in delta:
#             #         dx = x + d[0]
#             #         dy = y + d[1]
#             #         if 0 <= dx < n and 0 <= dy < n:
#             #             if color == board[dy][dx] and not v[dy][dx]:
#             #                 stack.append((dy, dx))
#
#             rg_count += 1
#
# for i in board:
#     print(i)
#
# print()
# # for i in rg_board:
# #     print(i)
#
# print(count)
# print(rg_count)
