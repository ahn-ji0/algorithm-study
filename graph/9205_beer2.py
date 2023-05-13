import heapq
INF = int(1e9)
T = int(input())
def possible(a, b):
    if abs(a[0] - b[0]) + abs(a[1]-b[1]) <= 20 * 50:
        return True
    return False

def dijkstra(N):
    distance = [INF for i in range(N + 2)]
    queue = [(0,0)]
    distance[0] = 0
    while queue:
        curr, dist = heapq.heappop(queue)
        if dist > distance[curr]:
            continue

        for n_idx, weight in grid[curr]:
            if dist + weight < distance[n_idx]:
                distance[n_idx] = dist + weight
                heapq.heappush(queue, (n_idx, distance[n_idx]))
    return distance[-1]


for t in range(T):
    N = int(input())
    places = [list(map(int, input().split())) for _ in range(N + 2)]

    grid = [[] for i in range(N + 2)]
    for i in range(N + 2):
        for j in range(i + 1, N + 2):
            if possible(places[i], places[j]):
                grid[i].append((j, 1))
                grid[j].append((i, 1))

    if dijkstra(N) != INF:
        print("happy")
    else:
        print("sad")