import sys
sys.setrecursionlimit(1000000)
N, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(N)]


dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x, y):
    global countries, total

    visited[x][y] = 1
    countries.append((x, y))
    total += grid[x][y]

    for i in range(len(dx)):
        tmp_x = x + dx[i]
        tmp_y = y + dy[i]
        if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N or visited[tmp_x][tmp_y]:
            continue

        diff = abs(grid[x][y] - grid[tmp_x][tmp_y])
        if diff >= L and diff <= R:
            dfs(tmp_x, tmp_y)

day = 0
while True:
    stop = True
    visited = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                countries = []
                total = 0
                dfs(i, j)

                if len(countries) == 1:
                    continue

                stop = False
                for a, b in countries:
                    grid[a][b] = total // len(countries)

    if stop:
        break

    day += 1

print(day)