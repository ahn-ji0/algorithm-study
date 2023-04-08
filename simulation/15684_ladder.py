# 사다리 조작 - https://www.acmicpc.net/problem/15684

import copy

N, M, H = map(int, input().split())
grid = [[0 for i in range(N)] for j in range(H)]

for i in range(M):
    a, b = map(int, input().split())
    grid[a-1][b-1] = 1

def possible(x, y, grid):
    for n_x, n_y in [(x,y-1), (x,y+1)]:
        if n_x < 0 or n_x >= H or n_y < 0 or n_y >= N:
            continue
        if grid[n_x][n_y] == 1:
            return False

    return True
def check(grid):
    for i in range(N):
        tmp_y = i
        for j in range(H):
            if grid[j][tmp_y] == 1:
                tmp_y += 1
            elif tmp_y - 1 >= 0:
                if grid[j][tmp_y - 1] == 1:
                    tmp_y -= 1

        if tmp_y != i:
            return False

    return True

def dfs(num, x, y):
    global min_val
    if num > 3:
        return

    if check(grid):
        min_val.append(num)
        return
    if num == 3:
        return
    # 하나 추가하는 건데
    for i in range(x, H):
        k = y if i == x else 0
        for j in range(k, N - 1):
            if grid[i][j] == 0 and possible(i,j, grid):
                grid[i][j] = 1
                dfs(num + 1, i, j + 2)
                grid[i][j] = 0


min_val = []
dfs(0, 0, 0)
if min_val == []:
    print(-1)
else:
    print(min(min_val))
