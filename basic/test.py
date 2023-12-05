import heapq
import sys

input = sys.stdin.readline
INF = float('inf')

def daik(start):
    q = []
    distance = [INF] * (n + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, point = heapq.heappop(q)
        if distance[point] < dist:
            continue

        for node_index, node_cost in doro[point]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance

n, m, x = map(int, input().split())
doro = list([] for _ in range(n + 1))

for _ in range(m):
    start, end, time = map(int, input().split())
    doro[start].append((end, time))

result = []
for i in range(1, n+1):
    in_time = daik(i)
    out_time = daik(x)
    result.append(in_time[x] + out_time[i])

print(max(result))
