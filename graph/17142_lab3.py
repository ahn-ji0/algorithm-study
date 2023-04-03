# 연구소 3 - https://www.acmicpc.net/problem/17142

from collections import deque
import heapq

N, M = map(int, input().split())

def get_combinations(virus, n):
    
    if n == 0:
        return [[]]
    
    result = []
    for i in range(len(virus)):
        element = virus[i]
        for next in get_combinations(virus[i+1:], n-1):
            result.append([element] + next)
    
    return result

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs(combinations, grid):
    queue = deque(combinations)
    visited = [[0 for i in range(N)] for j in range(N)]
    max_time = 0
    while queue:
        x, y, time = queue.popleft()
        if grid[x][y] == 0 and time > max_time:
            max_time = time
            
        for i in range(len(dx)):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
            if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N or visited[tmp_x][tmp_y] or grid[tmp_x][tmp_y] == 1:
                continue
            
            visited[tmp_x][tmp_y] = 1
            queue.append((tmp_x, tmp_y, time + 1))
    
    return (visited, max_time)

def check_zero(visited, grid):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0 and visited[i][j] == 0:
                return False
            
    return True

grid = [list(map(int, input().split())) for i in range(N)]

virus = []
wall_cnt = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            virus.append((i,j,0))
        elif grid[i][j] == 1:
            wall_cnt += 1

impossible = True
cases = []
for combinations in get_combinations(virus, M):
    visited, time = bfs(combinations, grid)
    if check_zero(visited,grid):
        impossible = False
        heapq.heappush(cases, time)

if impossible:
    print(-1)
else:
    print(heapq.heappop(cases))
    