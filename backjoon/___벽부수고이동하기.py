from collections import deque

INF = float('inf')
n, m = map(int, input().split())
board = list(list(map(int, input())) for _ in range(n))
walk_board = list(list([INF,INF] for _ in range(m)) for _ in range(n))
# n,m까지 최단경로로 이동
# 벽 하나까지 꺨 수 있음.
# 벽을 깬다는 건 = 그 쪽 방향으로 2번 이동한다.
# 그 방향으로 벽 2개가 있으면 안된다.
# 2번째 방향까지 체크해야함.

stack = deque([(0, 0, True)])

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
walk_board[0][0][0] = 1
walk_board[0][0][1] = 1

while stack:
    x, y, crush_flag = stack.popleft()
    if x == 3 and y == 8 and walk_board[x][y][0] == 14:
        print("a")
        print(crush_flag)
    for d in delta:
        dx, dy = x + d[0], y + d[1]
        if 0 <= dx < n and 0 <= dy < m:
            if board[dx][dy] == 0:
                if walk_board[dx][dy][0] > walk_board[x][y][0] + 1:
                    stack.append((dx, dy, True))
                    walk_board[dx][dy][0] = walk_board[x][y][0] + 1

                if walk_board[dx][dy][1] > walk_board[x][y][1] + 1:
                    stack.append((dx, dy, False))
                    walk_board[dx][dy][1] = walk_board[x][y][1] + 1
            if x == 3 and y == 8 and walk_board[x][y][0] == 14:
                print(board[dx][dy])
                print(crush_flag)
                print()
            # 벽 부수는 경우
            if board[dx][dy] == 1 and crush_flag:
                if x == 3 and y == 8 and walk_board[x][y][0] == 14:
                    print("a")
                    print(crush_flag)
                for d2 in delta:
                    dx2, dy2 = dx + d2[0], dy + d2[1]
                    if 0 <= dx2 < n and 0 <= dy2 < m and walk_board[dx2][dy2][1] > walk_board[x][y][0] + 2:
                        if board[dx2][dy2] == 0:
                            stack.append((dx2, dy2, False))
                            walk_board[dx2][dy2][1] = walk_board[x][y][0] + 2

for i in walk_board:
    for j in i:
        print(j[0],end=" ")
    print()

print()
for i in walk_board:
    for j in i:
        print(j[1],end=" ")
    print()

print()

result = min(walk_board[n-1][m-1])
print(-1 if result == INF else result)




# INF = float('inf')
# n,m = map(int,input().split())
# board = list( list(map(int,input())) for _ in range(n))
# walk_board = list(list(INF for _ in range(m)) for _ in range(n))
# walk_board_2 = list(list(INF for _ in range(m)) for _ in range(n))
# # n,m까지 최단경로로 이동
# # 벽 하나까지 꺨 수 있음.
# # 벽을 깬다는 건 = 그 쪽 방향으로 2번 이동한다.
# # 그 방향으로 벽 2개가 있으면 안된다.
# # 2번째 방향까지 체크해야함.
#
# stack = [(0,0,True)]
# stack2 = [(n-1,m-1,True)]
#
# delta = [(1,0),(0,1),(-1,0),(0,-1)]
# walk_board[0][0] = 1
# walk_board_2[n-1][m-1] = 1
# # result = []
#
#
# print(board)
# while stack:
#     x,y,crush_flag = stack.pop()
#
#     # if x == n-1 and y == m-1:
#     #     result.append(walk)
#     #     continue
#
#     for d in delta:
#         dx, dy = x + d[0], y + d[1]
#         if 0 <= dx < n and 0 <= dy < m:
#             if board[dx][dy] == 0 and walk_board[dx][dy] > walk_board[x][y] + 1:
#                 stack.append((dx, dy, crush_flag))
#                 walk_board[dx][dy] = walk_board[x][y] + 1
#             if board[dx][dy] == 1:
#                 for d2 in delta:
#                     dx2, dy2 = dx + d2[0], dy + d2[1]
#                     if 0 <= dx2 < n and 0 <= dy2 < m and crush_flag and walk_board[dx2][dy2] > walk_board[x][y] + 2:
#                         if board[dx2][dy2] == 0:
#                             stack.append((dx2, dy2, False))
#                             walk_board[dx2][dy2] = walk_board[x][y] + 2
#
# while stack2:
#     x,y,crush_flag = stack2.pop()
#
#     for d in delta:
#         dx, dy = x + d[0], y + d[1]
#         if 0 <= dx < n and 0 <= dy < m:
#             if board[dx][dy] == 0 and walk_board_2[dx][dy] > walk_board_2[x][y] + 1:
#                 stack2.append((dx, dy, crush_flag))
#                 walk_board_2[dx][dy] = walk_board_2[x][y] + 1
#             if board[dx][dy] == 1:
#                 for d2 in delta:
#                     dx2, dy2 = dx + d2[0], dy + d2[1]
#                     if 0 <= dx2 < n and 0 <= dy2 < m and crush_flag and walk_board_2[dx2][dy2] > walk_board_2[x][y] + 2:
#                         if board[dx2][dy2] == 0:
#                             stack2.append((dx2, dy2, False))
#                             walk_board_2[dx2][dy2] = walk_board_2[x][y] + 2
#
#
#     # 벽을 하나 깻을 경우 더욱 빠른 속도로 갈 수 있는 경우(깻을 경우와 안깻을 경우 2개로 나눠서 진행?
#     # 벽이 있을경우 그 뒤에 벽이 없으면 벽을 깨고 2개 넣어주고, flag를 세워주는 것과 그냥 아무것도 안하고 넘어가는 단계
#
# for i in walk_board:
#     print(i)
#
# print()
# for i in walk_board_2:
#     print(i)
#
# if walk_board[n-1][m-1] == INF:
#     print(-1)
# else:
#     print(walk_board[n-1][m-1])
#
#
#
#
