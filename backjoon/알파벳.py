from collections import deque

r, c = map(int, input().split())
arr = list(input() for _ in range(r))

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [False for _ in range(26)]
max_walk = 0


def dfs(x, y, visited, walk):
    global max_walk
    visited[ord(arr[x][y]) - 65] = True
    max_walk = max(max_walk, walk)

    for d in delta:
        dx = d[0] + x
        dy = d[1] + y
        if 0 <= dx < r and 0 <= dy < c:
            if not visited[ord(arr[dx][dy]) - 65]:
                dfs(dx, dy, visited, walk + 1)
                visited[ord(arr[dx][dy]) - 65] = False


dfs(0, 0, visited, 1)

print(max_walk)
