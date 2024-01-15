t = int(input())
for tc in range(t):
    board = [list(map(int,input().split())) for _ in range(9)]

    nice = [i for i in range(1,10)]
    result = 1

    hei = [[] for _ in range(9)]
    sq = [[] for _ in range(3)]
    sq2 = []

    for i in range(9):
        for j in range(9):
            hei[j].append(board[i][j])
            sq[j//3].append(board[i][j])

    for i in range(3):
        sq2.append(sq[i][:9])
        sq2.append(sq[i][9:18])
        sq2.append(sq[i][18:27])

    for i in range(9):
        # print(sorted(board[i]))
        # print(sorted(hei[i]))
        # print(sorted(sq2[i]))
        if sorted(board[i]) != nice:
            result = 0
            break
        if sorted(sq2[i]) != nice:
            result = 0
            break
        if sorted(hei[i]) != nice:
            result = 0
            break


    print('#'+str(tc+1) +" "+ str(result))




