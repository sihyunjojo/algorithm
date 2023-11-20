from collections import deque

def bfs_maze(maze, start, end):
    N = len(maze)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 방향

    queue = deque([(start[0], start[1], 0)])  # 큐에 시작 지점을 넣음
    visited = [[False] * N for _ in range(N)]  # 방문 여부를 저장하는 2차원 리스트
    visited[start[0]][start[1]] = True  # 시작 지점을 방문했음을 표시

    min_distance = float('inf')  # 최소 이동 칸 수
    min_position = (float('inf'), float('inf'))  # 최소 이동 칸 수일 때의 위치

    while queue:
        x, y, distance = queue.popleft()

        # 도착 지점에 도달하면 최소 이동 칸 수와 해당 위치를 갱신
        if (x, y) == end and distance <= min_distance:
            min_distance = distance
            min_position = (x, y)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 미로 범위 내에서 이동 가능하고, 아직 방문하지 않았고, 벽이 아닌 경우
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maze[nx][ny] != 1:
                queue.append((nx, ny, distance + 1))
                visited[nx][ny] = True  # 방문했음을 표시

    # 도착 지점에 도달할 수 없는 경우
    return min_position

N = len(maze)
directrion [(-1,0),(1,0),(0,-1),(0,1)]

queue = deque([start[0], start[1],0)])
visited = [[False] * n for _ in range(N)]

min_distance =
min_posistion =

while queue:
    x,y,distance = queue.popleft()

    if (x,y) == end and distance <= min_distance:
        # 저장

    for dx, dy in directions:
        nx,ny =

        queue.append((nx,ny,distance+1))
        visited[nx][ny]


    return min_posistion


####
print(format(int("AAA", 16), '020b'))
print(format(int("AAA", 16), '020b'))

###
def is_safe(board, row, col):
    # 현재 위치에 퀸을 놓을 수 있는지 확인하는 함수
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_solution(board):
    # 현재 퀸의 배치를 출력하는 함수
    for row in range(len(board)):
        line = ["Q" if i == board[row] else "." for i in range(len(board))]
        print(" ".join(line))
    print()

def solve_n_queens_util(board, row):
    # 현재 행에 퀸을 놓을 수 있는지 여부를 확인
    # 이게 멈춰주는 그거네.
    n = len(board)

    if row == n:
        # 모든 행에 퀸을 놓았으면 현재 상태를 출력
        print_solution(board)
        return

    for col in range(n): # 열의 횟수만큼 진행시켜주는데,
        if is_safe(board, row, col): # 열의 횟수만큼 안전한지 파악 후
            # 퀸을 현재 위치에 놓고 재귀적으로 다음 행을 확인
            board[row] = col # 안전하다면 board[row]에 그 위치 나둔 후,
            solve_n_queens_util(board, row + 1)

board = [[0] * n for _ in range(n)]
board = [-1] * n  # 각 행에 퀸이 있는 열을 저장

# row는 진행시켜주는 거고 col은 그 안에서 답을 찾는 거니까. col은 항상 row안에 들어가기만함.
#이 로직 자체가 제일 중요.
solve_n_queens_util(board, now)
n = len(board)

if row == n:
    printboard()
    return
for col in range(n):
    if is_safe(board,row,col): # 중요
        board[row] = col # row에서 col위치 들어가 있다.
        solve_n_queens_util(board, row + 1) # row에서 넣어놓았으니 row +1을 찾으러간다.


