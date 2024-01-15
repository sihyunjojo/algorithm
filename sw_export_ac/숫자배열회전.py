t = int(input())
for tc in range(1,t+1):
    result = 0

    n = int(input())
    board = list(list(input().split()) for _ in range(n))

    print('#'+str(tc))

    board1 = [[0 for _ in range(n)] for _ in range(n)]
    board2 = [[0 for _ in range(n)] for _ in range(n)]
    board3 = [[0 for _ in range(n)] for _ in range(n)]


    for i in range(n):
        for j in range(n):
            board3[(n-1) - j][i] = board[i][j]
            board2[(n-1) - i][(n-1) - j] = board[i][j]
            board1[j][(n-1) - i] = board[i][j]

    for i in range(n):
        for j in board1[i]:
            print(j,end ="")
        print(" ",end ="")
        for j in board2[i]:
            print(j,end ="")
        print(" ",end ="")
        for j in board3[i]:
            print(j,end ="")
        print()

        # for j in i:
        #     print(j,end="")
        # print()
    # for i in board2:
    #     print(*i)
    # for i in board3:
    #     print(*i)
    # a + b = (n-1)
    # a = (n-1) - b
    # 0 0 - > 0 2 / 0 1 -> 1 2 / 0 2 -> 2 2

            # 0 0 -> 2 0 / 1 0 -> 2 1 / 2 0 -> 2 2
            # 0 1 -> 1 0 / 1 1 -> 1 1 / 2 1 -> 1 2
            # 0 2 -> 0 0 / 1 2 -> 0 1 / 2 2 -> 0 2