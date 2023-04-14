# 경로 찾기 - https://www.acmicpc.net/problem/11403

INF = int(1e9)
N = int(input())
grid = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
    for j in range(N):
        # if i == j:
        #     grid[i][j] = 0
        if grid[i][j] == 0:
            grid[i][j] = INF

for k in range(N):
    for i in range(N):
        for j in range(N):
            if grid[i][k] + grid[k][j] < grid[i][j]:
                grid[i][j] = grid[i][k] + grid[k][j]

for i in range(N):
    for j in range(N):
        if grid[i][j] != INF:
            grid[i][j] = 1
        else:
            grid[i][j] = 0

for i in range(N):
    print(' '.join(str(e) for e in grid[i]))
