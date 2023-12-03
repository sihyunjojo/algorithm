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

        for new_start, new_dist in doro[point]:
            temp_dist = dist + new_dist

            if distance[new_start] > temp_dist:
                distance[new_start] = temp_dist
                heapq.heappush(q, (temp_dist, new_start))

    return distance

n, m, x = map(int, input().split())
doro = list([] for _ in range(n + 1))

for _ in range(m):
    start, end, time = map(int, input().split())
    doro[start].append((end, time))

print("doro = ", doro)

result = []
for i in range(1, n+1):
    in_time = daik(i)
    out_time = daik(x)
    result.append(in_time[x] + out_time[i])

print(max(result))
