from collections import deque
INF = float('inf')

m,n = map(int,input().split())
board = list([] for _ in range(n))
delta = [(1,0),(0,1),(-1,0),(0,-1)]
result = 0

ik = deque()

for i in range(n):
    tomatos = list(map(int,input().split()))
    board[i] = tomatos
    for j in range(m):
        if tomatos[j] == 1:
            ik.append((i,j))

for i in range(n):
    for j in range(m):
        if tomatos[j] == 0:
            flag = 0
            for d in delta:
                dx = j + d[0]
                dy = i + d[1]
                if 0 <= dx < m and 0 <= dy < n:
                    if board[dy][dx] != -1:
                        flag += 1
            # if flag == 0:
            #     print(i,j)
            #     result = -1
        if board[i][j] == 0:
            board[i][j] = INF


max_answer = 0

while ik:
    y,x = ik.popleft()

    for d in delta:
        dy = y + d[0]
        dx = x + d[1]
        if 0 <= dx < m and 0 <= dy < n:
            if board[dy][dx] != 0:
                if board[dy][dx] > board[y][x] + 1:
                    board[dy][dx] = board[y][x] + 1
                    ik.append((dy,dx))
                    max_answer = max(max_answer,board[y][x])


for i in board:
    if INF in i:
        result = -1
    # print(i)

if result == -1:
    print(result)
else:
    print(max_answer)








