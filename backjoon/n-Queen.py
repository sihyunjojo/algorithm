n = int(input())
count = 0

#핵심
board = [0 for i in range(n)]


def check(line):

    #핵심 = line을 넣는 것 N이 아니라
   for i in range(line):
        if (board[line] == board[i]) or (abs(board[line] - board[i]) == abs(line - i)):
            print('a')
            return False
    return True


def n_queen(line):
    global count
    if line == n:
        print('good = ', board)
        count += 1
        return

    for space in range(n):
        board[line] = space
        if check(line):
            n_queen(line + 1)


n_queen(0)
print(count)

# def check(temp_board, line, space):
#     for i in range(line):
#         # if i == line:
#         #     continue
#         if (space == temp_board[i]) or (abs(space - temp_board[i]) == abs(line - i)):
#             print('a')
#             return False
#     return True
#
#
# def n_queen(board, line):
#     global count
#     if line == n:
#         print('good = ',board)
#         count += 1
#         return
#
#     for space in range(n):
#         board[line] = space
#         if check(board, line, space):
#             n_queen(board, line + 1)
#
#
# init_board = [[0 for _ in range(n)] for _ in range(n)]
#
# print(15 ** 15)
#
# print(15 * 15)
#
#
# def checking(temp_board, line, space):
#     print('temp =', temp_board)
#     for i in range(n):
#         for j in range(n):
#             if i == line and j == space:
#                 continue
#             if j == space and temp_board[i][j] == 1:
#                 print('b')
#                 return False
#             elif abs(line - i) == abs(space - j) and temp_board[i][j] == 1:
#                 print('c')
#                 return False
#     return True
#
#
# def n_queen(board, line):
#     global count
#     if line == n:
#         count += 1
#         return
#     print(board)
#
#     for space in range(n):
#         print(1)
#         board[line][space] = 1
#         if checking(board, line, space):
#             print(2)
#             n_queen(board, line + 1)
#         board[line][space] = 0
#
#
# n_queen(init_board, 0)
#
# print(count)
