# 마법사 상어와 복제 - https://www.acmicpc.net/problem/23290

import copy
from collections import deque
import heapq

N = 4
M, S = map(int, input().split())
fish = [list(map(int, input().split())) for i in range(M)]
grid = [[deque() for i in range(N)] for j in range(N)]
smell = [[0 for i in range(N)] for j in range(N)]
s_x, s_y = map(int, input().split())
s_x, s_y = s_x - 1, s_y - 1
for x, y, d in fish:
    grid[x-1][y-1].append((d-1, 0))

fish_dx = [0,-1,-1,-1,0,1,1,1]
fish_dy = [-1,-1,0,1,1,1,0,-1]

shark_dx = [-1,0,1,0]
shark_dy = [0,-1,0,1]
def fish_move(n):
    global grid
    for x in range(N):
        for y in range(N):
            if grid[x][y]:
                num_fish = len(grid[x][y])
                for _ in range(num_fish):
                    move = False
                    dir, depth = grid[x][y].popleft()
                    if depth > n:
                        grid[x][y].append((dir,depth))
                        continue
                    for k in range(len(fish_dx)):
                        new_dir = (dir - k) % 8
                        tmp_x = x + fish_dx[new_dir]
                        tmp_y = y + fish_dy[new_dir]
                        if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N:
                            continue

                        if (tmp_x == s_x and tmp_y == s_y) or smell[tmp_x][tmp_y]:
                            continue

                        grid[tmp_x][tmp_y].append((new_dir, n + 1))
                        move = True
                        break

                    if not move:
                        grid[x][y].append((dir, n + 1))

def max_shark_move(s, n, total, dir, visited):
    global shark_move

    if n == 0:
        heapq.heappush(shark_move, (-total, dir))
        return

    s_x, s_y = s

    for i in range(len(shark_dx)):
        tmp_s_x = s_x + shark_dx[i]
        tmp_s_y = s_y + shark_dy[i]
        if tmp_s_x < 0 or tmp_s_x >= N or tmp_s_y < 0 or tmp_s_y >= N:
            continue

        grid_sum = 0
        if not visited[tmp_s_x][tmp_s_y]:
            grid_sum = len(grid[tmp_s_x][tmp_s_y])
        visited[tmp_s_x][tmp_s_y] = True
        max_shark_move((tmp_s_x, tmp_s_y), n - 1, total + grid_sum, dir + [i], copy.deepcopy(visited))
        visited[tmp_s_x][tmp_s_y] = False


for s in range(S):
    grid_copy = copy.deepcopy(grid)

    fish_move(s)
    # print('---')
    # print('fishmove', grid)

    shark_move = []
    visited = [[False for i in range(N)] for j in range(N)]
    max_shark_move((s_x,s_y), 3, 0, [], visited)
    # print('sharkmove',shark_move)

    _, max_move = heapq.heappop(shark_move)

    # 그리드에서 없애고 smell 처리
    for i in max_move:
        # print(max_move)
        s_x += shark_dx[i]
        s_y += shark_dy[i]
        if grid[s_x][s_y]:
            grid[s_x][s_y] = deque()
            smell[s_x][s_y] = 3

    # 남은 smell -1
    for i in range(N):
        for j in range(N):
            if smell[i][j]:
                smell[i][j] -= 1

    for i in range(N):
        for j in range(N):
            grid[i][j] = grid[i][j] + grid_copy[i][j]

    # print('grid',grid)
    # print('smell', smell)
    # print('shark', (s_x, s_y))

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(grid[i][j])
print(answer)
