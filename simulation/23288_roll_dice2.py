# 주사위 굴리기 2 - https://www.acmicpc.net/problem/23288

from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]
dice = [1,2,3,4,5,6]
N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(N)]

def out_of_range(x, y, N, M):
    if x < 0 or x >= N or y < 0 or y >= M:
        return True

    return False
def get_score(x, y):
    visited = [[0 for i in range(M)] for j in range(N)]
    queue = deque()
    visited[x][y] = 1
    queue.append((x,y))
    cnt, num = 1, grid[x][y]
    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            tmp_x, tmp_y = x + dx[i], y + dy[i]
            if out_of_range(tmp_x,tmp_y,N,M) or visited[tmp_x][tmp_y] or grid[tmp_x][tmp_y] != num:
                continue
            cnt += 1
            visited[tmp_x][tmp_y] = 1
            queue.append((tmp_x, tmp_y))

    return cnt
def roll(dir, bottom_idx, up_idx, right_idx):
    if dir == 0:
        return right_idx, up_idx, 5 - bottom_idx
    elif dir == 1:
        return 5 - up_idx, bottom_idx, right_idx
    elif dir == 2:
        return 5 - right_idx, up_idx, bottom_idx
    elif dir == 3:
        return up_idx, 5 - bottom_idx, right_idx

x, y, dir = 0, 0, 0
bottom_idx, up_idx, right_idx = 5, 1, 2
total = 0

for _ in range(K):
    tmp_x, tmp_y = x + dx[dir],  y + dy[dir]
    if out_of_range(tmp_x,tmp_y,N,M):
        dir = (dir + 2) % 4
        tmp_x, tmp_y = x + dx[dir], y + dy[dir]

    bottom_idx, up_idx, right_idx = roll(dir, bottom_idx, up_idx, right_idx)
    score = get_score(tmp_x, tmp_y) * grid[tmp_x][tmp_y]
    total += score
    bottom_value = dice[bottom_idx]

    if bottom_value > grid[tmp_x][tmp_y]:
        dir = (dir + 1) % 4
    elif bottom_value < grid[tmp_x][tmp_y]:
        dir = (dir - 1) % 4
    x, y = tmp_x, tmp_y

print(total)







