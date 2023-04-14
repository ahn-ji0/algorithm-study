# 맥주 마시면서 걸어가기 - https://www.acmicpc.net/problem/9205

import heapq
INF = int(1e9)
def get_distance(a, b):
    a_x, a_y = a
    b_x, b_y = b
    return abs(a_x - b_x) + abs(a_y - b_y)

def dijkstra(start, end):
    queue = []
    distance = [INF for i in range(N+2)]
    distance[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        dist, curr = heapq.heappop(queue)

        if dist > distance[curr]:
            continue

        for neighbor in range(N+2):
            if grid[curr][neighbor] == 0:
                continue

            if dist + grid[curr][neighbor] < distance[neighbor]:
                distance[neighbor] = dist + grid[curr][neighbor]
                heapq.heappush(queue, (distance[neighbor], neighbor))

    return distance[end]

T = int(input())

for t in range(T):
    N = int(input())
    stops = [list(map(int, input().split())) for i in range(N + 2)]
    grid = [[0 for i in range(N+2)] for j in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            if i != j:
                dist = get_distance(stops[i], stops[j])
                if dist <= 20 * 50:
                    grid[i][j] = 1

    val = dijkstra(0, N+1)
    if val == INF:
        print("sad")
    else:
        print("happy")