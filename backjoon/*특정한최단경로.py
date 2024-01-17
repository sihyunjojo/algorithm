import heapq

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))


a,b = map(int,input().split())


def cut(start):
    v = [float('inf')] * n
    heap = []
    heapq.heappush(heap,[0,start])
    v[start] = 0

    while heap:
        dist, end= heapq.heappop(heap)
        if dist > v[end]:
            continue

        for i in graph[end]:
            now_dist = i[1] + dist
            if now_dist < v[i[0]]:
                heapq.heappush(heap,[now_dist, i[0]])
                v[i[0]] = now_dist

    return v

v_0 = cut(0)
v_a = cut(a-1)
v_b = cut(b-1)
# print(graph)


aa = v_0[a-1] + v_a[b-1] + v_b[n-1]
bb = v_0[b-1] + v_b[a-1] + v_a[n-1]

# print(v_0,v_a,v_b)
result = min(aa,bb)
print(result if result < float('inf') else -1)

# print(v[-1] if v[-1] != 0 else -1)

