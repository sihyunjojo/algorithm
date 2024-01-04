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
