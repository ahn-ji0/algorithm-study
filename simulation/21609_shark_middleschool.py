# 상어 중학교 - https://www.acmicpc.net/problem/21609

from collections import deque
import heapq

CLEAR = -2
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j, color):
    new_group = []
    rainbow_cnt = 0
    queue = deque()
    zero_visited = [[False for i in range(N)] for j in range(N)]
    queue.append((i, j))
    new_group.append((i, j))
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
            if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N:
                continue

            if visited[tmp_x][tmp_y] or zero_visited[tmp_x][tmp_y] or grid[tmp_x][tmp_y] == CLEAR or grid[tmp_x][tmp_y] == -1 or (grid[tmp_x][tmp_y] > 0 and grid[tmp_x][tmp_y] != color):
                continue

            if grid[tmp_x][tmp_y] == 0:
                zero_visited[tmp_x][tmp_y] = True
                rainbow_cnt += 1
            else:
                visited[tmp_x][tmp_y] = True

            queue.append((tmp_x, tmp_y))
            new_group.append((tmp_x, tmp_y))

    return len(new_group), new_group, rainbow_cnt
def gravity():

    for j in range(N):
        bottom = deque()
        for i in range(N-1, -1, -1):
            if grid[i][j] == CLEAR:
                bottom.append((i,j))
            elif grid[i][j] != -1:
                if bottom:
                    tmp_i, tmp_j = bottom.popleft()
                    grid[i][j], grid[tmp_i][tmp_j] = grid[tmp_i][tmp_j], grid[i][j]
                    bottom.append((i,j))
            else:
                bottom = deque()

def rotate():
    new_grid = [[0 for i in range(N)] for j in range(N)]

    for i in range(N):
        for j in range(N):
            new_grid[i][j] = grid[j][N-1-i]

    return new_grid

total = 0
while True:
    # 최대 그룹 추출
    groups = []
    for c in range(1, M + 1):
        visited = [[False for i in range(N)] for j in range(N)]
        for i in range(N):
            for j in range(N):
                if grid[i][j] == c and not visited[i][j]:
                    num_blocks, group, r_cnt = bfs(i, j, c)
                    heapq.heappush(groups, (-num_blocks, -r_cnt, -i, -j, group))

    if not groups:
        break

    max_num, i, j, k, max_group = heapq.heappop(groups)
    max_num = - max_num

    if max_num <= 1:
        break

    total += max_num * max_num

    for block in max_group:
        i, j = block
        grid[i][j] = CLEAR

    gravity()

    grid = rotate()

    gravity()


print(total)