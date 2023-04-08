# 감시 - https://www.acmicpc.net/problem/15683
import copy

dx = [0,1,0,-1]
dy = [1,0,-1,0]
SAFE = 7
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(N)]

def check(x,y,dir, grid):
    while (x >= 0 and x < N and y >= 0 and y < M) and grid[x][y] != 6:
        if grid[x][y] == 0:
            grid[x][y] = SAFE
        x += dx[dir]
        y += dy[dir]

def check_cases(x, y, cctv_num, dir, grid):
    if cctv_num == 1:
        check(x,y,dir, grid)
    elif cctv_num == 2:
        check(x,y,dir, grid)
        check(x,y,(dir+2) % 4, grid)
    elif cctv_num == 3:
        check(x,y,dir, grid)
        check(x,y,(dir+1) % 4, grid)
    elif cctv_num == 4:
        for i in range(3):
            check(x,y,(dir+i) % 4, grid)
    elif cctv_num == 5:
        for i in range(4):
            check(x,y,i, grid)
def count_zero(grid):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                cnt +=1
    return cnt

cctv = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 5:
            check_cases(i,j,grid[i][j], 0, grid)
        elif grid[i][j] != 0 and grid[i][j] != 6 and grid[i][j] != SAFE:
            cctv.append((i,j,grid[i][j]))

num_cctv = len(cctv)

def dfs(n, grid):
    global min_cnt

    if n == num_cctv:

        cnt = count_zero(grid)
        min_cnt = min(min_cnt, cnt)
        return

    for dir in range(len(dx)):
        new_grid = copy.deepcopy(grid)
        check_cases(cctv[n][0], cctv[n][1], cctv[n][2], dir, new_grid)
        dfs(n+1, new_grid)

min_cnt = N * M + 1
dfs(0, grid)
print(min_cnt)

