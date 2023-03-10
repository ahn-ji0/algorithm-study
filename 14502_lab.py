# https://www.acmicpc.net/problem/14502
# 연구소

from itertools import combinations

import copy

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(loc, N, M):
    global visited, tmp_map

    x, y = loc
    visited[x][y] = 1
    
    for i in range(len(dx)):
        tmp_x = x + dx[i]
        tmp_y = y + dy[i]
        
        if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= M:
            continue
        
        # 0 이 아닌 경우, 방문한 경우
        if tmp_map[tmp_x][tmp_y] != 0 or visited[tmp_x][tmp_y]:
            continue
        
        tmp_map[tmp_x][tmp_y] = 2
        dfs((tmp_x, tmp_y), N, M)
        
N, M = map(int, input().split())


original_map = []
for _ in range(N):
    original_map.append(list(map(int,input().split())))

empty_idx = []
for i in range(N):
    for j in range(M):
        if original_map[i][j] == 0:
            empty_idx.append((i,j))

safe = []
for combo in combinations(empty_idx, 3):
    tmp_map = copy.deepcopy(original_map)
    for i in combo:
        tmp_map[i[0]][i[1]] = 1

    visited = [[0] * M for _ in range(N)]
    for x in range(N):
        for y in range(M):
            if tmp_map[x][y] == 2 and not visited[x][y]:
                dfs((x,y),N, M)
    count = 0
    
    for x in range(N):
        for y in range(M):
            if tmp_map[x][y] == 0:
                count += 1
                
    safe.append(count)
    
print(max(safe))
         
            