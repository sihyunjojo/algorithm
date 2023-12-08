# bfs시 deque를 쓰면 먼저 들어왔던걸 먼저 처리하면서, 처음 계산하는 값이 가장 작은 값으로 됨.
from collections import deque

INF = float('inf')
n,m = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
# n는 세로의 크기
walk_arr = list([INF for _ in range(m)] for _ in range(n))

delta = [(1,0),(0,1),(-1,0),(0,-1)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            stack = deque([(i,j)])
            walk_arr[i][j] = 0

while stack:
    row, col = stack.popleft()
    walk = walk_arr[row][col]

    for d in delta:
        dx = row + d[0]
        dy = col + d[1]
        if 0 <= dx < n and 0 <= dy < m and board[dx][dy] == 1 and walk_arr[dx][dy] > walk + 1:
            walk_arr[dx][dy] = walk + 1
            stack.append((dx,dy))

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            walk_arr[i][j] = 0
        if walk_arr[i][j] == INF:
            walk_arr[i][j] = -1
        print(walk_arr[i][j],end=" ")
    print()

# for i in walk_arr:
#     print(*i)







