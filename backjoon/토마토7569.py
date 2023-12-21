from collections import deque
INF = float('inf')

m,n,h = map(int,input().split())
board = list(list([] for _ in range(n)) for _ in range(h))
delta = [(1,0,0),(0,1,0),(-1,0,0),(0,-1,0),(0,0,1),(0,0,-1)]
result = 0

ik = deque()

for i in range(h):
    for j in range(n):
        tomatos = list(map(int, input().split()))
        board[i][j] = tomatos
        for k in range(m):
            if tomatos[k] == 1:
                ik.append((i,j,k))
            if board[i][j][k] == 0:
                board[i][j][k] = INF

# for i in board:
#     for j in i:
#         print(j)

max_answer = 0

while ik:
    z,y,x = ik.popleft()

    for d in delta:
        dz = z + d[0]
        dy = y + d[1]
        dx = x + d[2]
        if 0 <= dx < m and 0 <= dy < n and 0 <= dz < h:
            if board[dz][dy][dx] != 0:
                if board[dz][dy][dx] > board[z][y][x] + 1:
                    board[dz][dy][dx] = board[z][y][x] + 1
                    ik.append((dz,dy,dx))
                    max_answer = max(max_answer,board[z][y][x])


for i in board:
    for j in i:
        if INF in j:
            result = -1

if result == -1:
    print(result)
else:
    print(max_answer)








