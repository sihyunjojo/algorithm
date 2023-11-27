def change_block(board):
    # color = ['B', 'W']
    # min_count = float('inf')

    # for i in range(8):
    #     print(board[i])

    # for c in color:
    count = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0 and board[i][j] == 'B':
                # print(i, j, 'not ',c)
                count += 1
            if (i+j) % 2 == 1 and board[i][j] == 'W':
                # print(i, j, c)
                count += 1
    print(count)

    return min(64-count, count)

    return min_count


def create_chase_board(board, a, b):
    print(a,b)
    start = a, b
    end = a + 7, b + 7
    new_board = []

    for i in range(start[1], end[1]+1):
        row = board[i]
        new_board.append(row[start[0]:end[0]+1])

    return new_board


# 8 <= n, m <= 50

n, m = map(int, input().split())
init_board = list(list(input()) for _ in range(n))

min_change_count = float('inf')

for i in range(m - 7):
    for j in range(n - 7):
        new_chase_board = create_chase_board(init_board, i, j)
        min_count = change_block(new_chase_board)
        min_change_count = min(min_change_count, min_count)

print(min_change_count)
