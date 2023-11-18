# 이 코드는 세상 누구여도 이렇게 했어. 완벽
def count_board(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                count += 1

    return count


def down_box(board):
    for i in range(len(board[0])):
        for j in range(len(board) - 1, -1, -1):
            if board[j][i] == 0:
                for k in range(j, -1, -1):
                    board[k][i] = board[k - 1][i]

    # return temp_board


def start_brake(board, i, j):
    num = board[i][j]
    for k in range(num):  # 높이
        if i - k >= 0:
            board[i - k][j] = 0
        if j - k >= 0:
            board[i][j - k] = 0
        if i + k < len(board):
            board[i + k][j] = 0
        if j + k < len(board[i]):
            board[i][j + k] = 0

    for row in board:
        print(row)

    print("finish start_brake")
    return down_box(board)


# import copy
# def one_gusle(board):
#     board_list = []
#
#     for i in range(w):
#         for j in range(h):
#             if board[j][i] != 0:
#                 temp_board = copy.deepcopy(board)
#                 old_board = start_brake(temp_board, i, j)
#                 board_list.append(old_board)
#                 break
#
#     print("finish one_gisle")
#     return board_list

def shoot(col, board):
    # 특정 열에서 구슬을 쏘아 벽돌을 깨는 함수
    for row in range(h):
        if board[row][col] != 0:
            start_brake(board, row, col)
            down_box(board)
            break


def simulate_shooting(n, board):
    # N번의 구술 발사를 시뮬레이션하는 함수
    global result
    if n == 0:
        remaining_boxs = count_board(board)
        result = min(result, remaining_boxs)
        return

    # 핵심
    for col in range(w):
        temp_board = [row[:] for row in board]
        shoot(col, temp_board)
        simulate_shooting(n - 1, temp_board)


T = int(input())
for test_case in range(1, T + 1):
    n, w, h = map(int, input().split())
    board = list(list(map(int, input().split())) for i in range(h))

    print(board)
    result = float('inf')
    simulate_shooting(n, board)
    print(f"#{test_case} {result}")
