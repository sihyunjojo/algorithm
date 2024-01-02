n,m = map(int,input().split())
board = [[] for _ in range(n)]
people = []
count = 0
for i in range(n):
    line = input()
    for j in range(m):
        board[i].append(line[j])
        if line[j] == "I":
            doyeon = i,j
        if line[j] == "P":
            people.append([i,j])

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# print(doyeon)
# print(people)

stack = [doyeon]

while stack:
    y,x = stack.pop()
    board[y][x] = "V"

    for d in delta:
        dx = x + d[0]
        dy = y + d[1]
        if 0 <= dx < m and 0 <= dy < n:
            if board[dy][dx] == "P":
                count += 1
                board[dy][dx] = "V"
                stack.append([dy,dx])
            if board[dy][dx] == "O":
                stack.append([dy,dx])

# print("count = ",count)
print(count if count != 0 else "TT")


