import sys

input = sys.stdin.readline

N_MAX = 258


def count_paper(count):
    global white_result, blue_result
    # 8 -> 4 -> 2 -> 1

    for i in board:
        print(i)
    print(count)

    for i in range(n):
        if i % count != count - 1:
            continue
        for j in range(n):
            if j % count == count - 1 and board[i][j] != 2:
                print(i,j)
                white_result += count_paper_white(i, j, count)
                blue_result += count_paper_blue(i, j, count)

    if count == 1:
        return

    if count != 0:
        count_paper(int(count ** 1/2))


def count_paper_white(row, col, c):
    answer = 1

    # print(row-c+1,row+1,col-c+1,col+1)
    for i in range(row-c+1, row+1):
        for j in range(col-c+1, col+1):
            if board[i][j] == 1 or board[i][j] == 2:
                answer = 0
                break

    if answer == 1:
        for i in range(row - c + 1, row + 1):
            for j in range(col - c + 1, col + 1):
                board[i][j] = 2

    return answer


def count_paper_blue(row, col, c):
    answer = 1

    for i in range(row-c+1, row+1):
        for j in range(col-c+1, col+1):
            if board[i][j] == 0 or board[i][j] == 2:
                answer = 0
                break

    if answer == 1:
        for i in range(row - c + 1, row + 1):
            for j in range(col - c + 1, col + 1):
                board[i][j] = 2
        print(row - c + 1, row + 1, col - c + 1, col + 1)

    return answer


n = int(input())
board = list(list(map(int, input().split())) for _ in range(n))
white_result, blue_result = 0,0

count_paper(n)
for i in board:
    print(i)
print(white_result, blue_result)
