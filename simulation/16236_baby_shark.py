# 아기 상어 - https://www.acmicpc.net/problem/16236

import heapq
from collections import deque

N = int(input())

grid = [list(map(int, input().split())) for i in range(N)]
queue = []

cnt = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            x, y = i, j
            grid[i][j] = 0
        elif grid[i][j] != 0:
            heapq.heappush(queue, (grid[i][j], i, j))
            cnt += 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def get_distance(start_x, start_y, end_x, end_y, shark_size):
    global grid
    
    visit = [[0 for i in range(N)] for j in range(N)]
    visit[start_x][start_y] = 1
    q = deque()
    q.append((start_x, start_y,0))
    while q:
        curr_x, curr_y, depth = q.popleft()
        for i in range(len(dx)):
            tmp_x = curr_x + dx[i]
            tmp_y = curr_y + dy[i]
            if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N or visit[tmp_x][tmp_y] or grid[tmp_x][tmp_y] > shark_size:
                continue
            
            if tmp_x == end_x and tmp_y == end_y:
                return depth + 1
            
            visit[tmp_x][tmp_y] = 1
            q.append((tmp_x, tmp_y, depth + 1))
    return -1
    
visited = [0 for i in range(cnt)]
time = 0
shark_size = 2
eat = 0
while sum(visited) < cnt:
    tmp_queue = []
    # 방문하지 않은 것 중 먹을 수 있는 물고기 확인
    for i in range(len(queue)):
        if visited[i]:
            continue
        tmp_size, tmp_i, tmp_j = queue[i]
        if tmp_size < shark_size:
            dist = get_distance(x, y, tmp_i, tmp_j, shark_size)
            if dist == -1:
                continue
            heapq.heappush(tmp_queue, (dist, tmp_i, tmp_j, i))
        
    
    if not tmp_queue:
        break

    eat_dist, eat_i, eat_j, eat_idx = heapq.heappop(tmp_queue)
    grid[eat_i][eat_j] = 0
    time += eat_dist
    visited[eat_idx] = 1
    eat += 1
    if shark_size == eat:
        shark_size += 1
        eat = 0
    x, y = eat_i, eat_j
    
print(time)
    
    
    
           
    
    
