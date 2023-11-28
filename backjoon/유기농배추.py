def find_start_point(new_board):
    for i in range(len(new_board)):
        for j in range(len(new_board[i])):
            if new_board[i][j] == 1:
                return i, j


def bfs(a, b, new_board):
    stack = [[a, b]]
    delta_list = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while stack:
        x, y = stack.pop()
        new_board[y][x] = 0
        print(x,y,new_board[y][x])
        for delta in delta_list:
            dx = x + delta[0]
            dy = y + delta[1]
            if 0 <= dx < m and 0 <= dy < n:
                print(dy,dx)
                if new_board[dy][dx] == 1:
                    stack.append([dx, dy])

    for i in new_board:
        print(i)

    return new_board


def make_board():
    board = list(list(0 for _ in range(m)) for _ in range(n))

    for x,y in place_arr:
        board[y][x] = 1

    return board


for test_case in range(int(input())):
    m, n, k = map(int, input().split())  # 밭 가로길이, 세로길이, 위치개수
    place_arr = list(list(map(int, input().split())) for _ in range(k))
    # 배추위치 x,y가 주어짐. (위치가 같은경우는 없다)
    # 서로 인접해있어야함.
    count = 0

    init_board = make_board()
    temp_board = init_board

    # print(place_arr)


    while place_arr:
        x, y = place_arr.pop()
        print(x,y,temp_board[y][x])
        if temp_board[y][x] == 1:
            for i in temp_board:
                print(i)
            new_temp_board = bfs(x,y,temp_board)
            temp_board = new_temp_board
            count += 1

    print(count)
