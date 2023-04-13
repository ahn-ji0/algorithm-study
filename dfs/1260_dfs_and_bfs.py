from collections import deque
import heapq
N, M, start = map(int, input().split())
grid = [[] for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    heapq.heappush(grid[a-1],b-1)
    heapq.heappush(grid[b-1],a-1)

def dfs(start):
    visited = [0 for i in range(N)]
    stack = deque()
    stack.append(start)
    order = []
    while stack:
        curr = stack.pop()
        if not visited[curr]:
            visited[curr] = 1
            order.append(curr + 1)
            for i in reversed(grid[curr]):
                stack.append(i)
    print(order)

def dfs2(curr, visited, n, order):
    if n >= N:
        print(order)
        return

    for i in grid[curr]:
        if not visited[i]:
            visited[i] = 1
            dfs2(i, visited, n + 1, order + [i + 1])
            visited[i] = 0
            break

def bfs(start):
    visited = [0 for i in range(N)]
    visited[start] = 1
    queue = deque()
    queue.append(start)
    order = [start+1]
    while queue:
        curr = queue.popleft()
        for i in grid[curr]:
            if not visited[i]:
                visited[i] = 1
                order.append(i + 1)
                queue.append(i)

    print(order)

# dfs(start - 1)
visited = [0 for i in range(N)]
visited[start-1] = 1
dfs2(start - 1, visited, 1, [start])
bfs(start - 1)