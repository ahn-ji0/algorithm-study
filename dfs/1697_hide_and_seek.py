from collections import deque
N, K = map(int, input().split())

def bfs(N, K):
    if N == K:
        return 0

    queue = deque([(0, N)])
    visited = [False for i in range(100001)]
    visited[N] = True

    while queue:
        time, curr = queue.popleft()

        for next in [curr + 1, curr - 1, curr * 2]:
            if next < 0 or next > 100000 or visited[next]:
                continue

            if next == K:
                return time + 1

            queue.append((time+1, next))
            visited[next] = True

    return -1

print(bfs(N, K))
