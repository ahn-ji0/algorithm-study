# 뱀 https://www.acmicpc.net/problem/3190

from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

N = int(input())

# 사과의 위치
K = int(input())

grid = [[0 for i in range(N)] for j in range(N)]
for i in range(K):
    x, y = map(int, input().split())
    grid[x-1][y-1] = 1

# 뱀의 방향 변환 정보
L = int(input())

time = deque()
dir = deque()
for i in range(L):
    t, r = input().split()
    t = int(t)
    time.append(t)
    dir.append(r)

snake = deque()
snake.append((0,0))

grid[0][0] = 2

count = 0
rotate = time.popleft()
dir_idx = 0

h_x = 0
h_y = 0

while(True):
    
    if count == rotate:
        dir_key = dir.popleft()
        if dir_key == 'L':
            dir_idx = (dir_idx - 1) % 4
        elif dir_key == 'D':
            dir_idx = (dir_idx + 1) % 4

        if time:
            rotate = time.popleft()
        
    # 가는거야
    tmp_x = h_x + dx[dir_idx]
    tmp_y = h_y + dy[dir_idx]
    
    # 벽에 무딪히는 경우 / 뱀의 몸에 부딪히는 경우
    if tmp_x < 0 or tmp_x >= N or tmp_y <0 or tmp_y >=N or grid[tmp_x][tmp_y] == 2:
        break
    
    # 이동
    h_x = tmp_x
    h_y = tmp_y
    
    snake.append((h_x, h_y))
    
    if grid[h_x][h_y] != 1:
        (t_x, t_y) = snake.popleft()
        grid[t_x][t_y] = 0
    
    grid[h_x][h_y] = 2

    count += 1

print(count + 1)