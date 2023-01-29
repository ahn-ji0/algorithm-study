# 백준 10026 적록색약 - https://www.acmicpc.net/problem/10026
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def num_regions(i, j, N, grid, visited):
    queue = deque()
    
    group_color = grid[i][j]
    queue.append((i,j))
    visited[i][j] = 1
    while queue:
        x, y = queue.popleft()
        
        for i in range(len(dx)):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
            
            if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N: continue
            
            if visited[tmp_x][tmp_y] or grid[tmp_x][tmp_y] != group_color: continue
            
            visited[tmp_x][tmp_y] = 1
            queue.append((tmp_x, tmp_y))

    return 1

N = int(input())

grid = [input() for _ in range(N)]
# 보통 사람
visited = [[0] * N for _ in range(N)]
general_count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            general_count += num_regions(i, j, N, grid, visited)

# 적록 색맹인 사람
for i in range(N):
    grid[i]=grid[i].replace("G","R")

visited = [[0] * N for _ in range(N)]
daltonism_count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            daltonism_count += num_regions(i, j, N, grid, visited)
            
print(general_count, daltonism_count)