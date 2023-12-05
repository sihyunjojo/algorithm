# n m

n,m = map(int,input().split())
v = list([] for _ in range(n+1))
for _ in range(m):
    start, end = map(int,input().split())
    v[start].append(end)
    v[end].append(start)

result = 0
visited = [False] * (n + 1)

for i in range(1,n+1):
    if not visited[i]:
        stack = [i]
        visited[i] = True
        result += 1

        while stack:
            point = stack.pop()

            for j in v[point]:
                if not visited[j]:
                    stack.append(j)
                    visited[j] = True

print(result)