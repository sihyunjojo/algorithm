r, c = map(int,input().split())
arr = list(input() for _ in range(r))

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [False for _ in range(26)]
stack = [(0, 0)]
walk = 0

while stack:
    x, y = stack.pop()
    visited[ord(arr[x][y])-65] = True

    for d in delta:
        dx = d[0] + x
        dy = d[1] + y
        if 0 <= dx < r and 0 <= dy < c:
            if not visited[ord(arr[dx][dy])-65]:
                stack.append((dx, dy))

print(visited.count(True))
