from collections import deque
N, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(N)]


dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(i, j):
    total = grid[i][j]
    countries = [(i, j)]
    queue = deque([(i, j)])
    visited[i][j] = 1
    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
            if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N or visited[tmp_x][tmp_y]:
                continue

            diff = abs(grid[x][y] - grid[tmp_x][tmp_y])
            if diff >= L and diff <= R:
                visited[tmp_x][tmp_y] = 1
                queue.append((tmp_x, tmp_y))
                countries.append((tmp_x, tmp_y))
                total += grid[tmp_x][tmp_y]

    return total, countries
def dfs(i, j, visited):
    global c
    for i in range(len(dx)):
        tmp_x = x + dx[i]
        tmp_y = y + dy[i]
        if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N or visited[tmp_x][tmp_y]:
            continue

        diff = abs(grid[x][y] - grid[tmp_x][tmp_y])
        if diff >= L and diff <= R:
            visited[tmp_x][tmp_y] = 1
            dfs(tmp_x, tmp_y, visited)
            visited[tmp_x][tmp_y] = 0

day = 0
while True:
    stop = True
    visited = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                total, countries = bfs(i, j)

                if len(countries) == 1:
                    continue

                stop = False
                for a, b in countries:
                    grid[a][b] = total // len(countries)

    if stop:
        break

    day += 1

print(day)