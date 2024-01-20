n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

delta_wid = [(1,0,1,0,1),(1,0,1,1,3)]
delta_hei = [(0,1,0,1,2),(0,1,1,1,3)]
delta_dia = [(1,1,1,0,1),(1,1,0,1,2),(1,1,1,1,3)]


result = 0
stack = [(0,0,1,0,1)]
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

dp[0][0][1] = 1
for i in range(2,n):
    if board[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for i in range(1,n):
    for j in range(2,n):
        if board[i][j] == 0:
            dp[1][i][j] += dp[1][i - 1][j] + dp[2][i - 1][j]
            dp[0][i][j] += dp[0][i][j-1] + dp[2][i][j-1]
            if board[i][j-1] == 0 and board[i-1][j] == 0:
                print(i,j)
                dp[2][i][j] += dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

# print(dp)
for i in dp:
    print(i)
print(dp[0][-1][-1]+dp[1][-1][-1]+dp[2][-1][-1])


# for i in range(n):
    # for j in range(n):
        # if visited[i] ==

# def bfs():
#     global result
#
#     while stack:
#         fx,fy,sx,sy,sh = stack.pop()
#
#         if sx == n-1 and sy == n-1:
#             result += 1
#             continue
#
#         if sh == 1:
#             for d in delta_wid:
#                 dfx, dfy, dsx, dsy = fx+d[0],fy+d[1],sx+d[2],sy+d[3]
#                 if 0 <= dfx < n and 0 <= dfy < n and 0 <= dsx < n and 0 <= dsy < n:
#                     if board[dfy][dfx] == 0 and board[dsy][dsx] == 0:
#                         if d[4] == 3:
#                             if board[sy][sx+1] == 0 and board[sy+1][sx] == 0:
#                                 stack.append((dfx, dfy, dsx, dsy, d[4]))
#                         else:
#                             stack.append((dfx, dfy, dsx, dsy, d[4]))
#         elif sh == 2:
#             for d in delta_hei:
#                 dfx, dfy, dsx, dsy = fx+d[0],fy+d[1],sx+d[2],sy+d[3]
#                 if 0 <= dfx < n and 0 <= dfy < n and 0 <= dsx < n and 0 <= dsy < n:
#                     if board[dfy][dfx] == 0 and board[dsy][dsx] == 0:
#                         if d[4] == 3:
#                             if board[sy][sx+1] == 0 and board[sy+1][sx] == 0:
#                                 stack.append((dfx, dfy, dsx, dsy, d[4]))
#                         else:
#                             stack.append((dfx, dfy, dsx, dsy, d[4]))
#         elif sh == 3:
#             for d in delta_dia:
#                 dfx, dfy, dsx, dsy = fx+d[0],fy+d[1],sx+d[2],sy+d[3]
#                 if 0 <= dfx < n and 0 <= dfy < n and 0 <= dsx < n and 0 <= dsy < n:
#                     if board[dfy][dfx] == 0 and board[dsy][dsx] == 0:
#                         if d[4] == 3:
#                             if board[sy][sx+1] == 0 and board[sy+1][sx] == 0:
#                                 stack.append((dfx, dfy, dsx, dsy, d[4]))
#                         else:
#                             stack.append((dfx, dfy, dsx, dsy, d[4]))
#
#
# bfs()
print(result)



