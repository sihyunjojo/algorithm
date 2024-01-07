import heapq

INF = float('INF')

v_count, e_count = map(int, input().split())
start_point = int(input())
# v = list([0 if j == i else INF for j in range(v_count+1)] for i in range(v_count+1))
# graph = dict.fromkeys(list(i for i in range(1, v_count + 1)), {})
graph = {}
for i in range(1,v_count+1):
    graph[i] = {}
distances = [0 if start_point == i else INF for i in range(v_count + 1)]


for i in range(e_count):
    a, b, c = map(int, input().split())

    # if a not in graph:
    #     graph[a] = {}

    graph[a][i] = [b, c]

print(graph)

queue = []
heapq.heappush(queue, [0, start_point])

while queue:
    now_distance, now_destination = heapq.heappop(queue)
    print(now_distance, now_destination)
    if now_distance > distances[now_destination]:
        continue

    for new_destination, new_distance in graph[now_destination].values():
        distance = now_distance + new_distance
        if distance < distances[new_destination]:
            distances[new_destination] = distance
            heapq.heappush(queue, [distance, new_destination])

for i in distances[1:]:
    if i != INF:
        print(i)
    elif i == INF:
        print('INF')
