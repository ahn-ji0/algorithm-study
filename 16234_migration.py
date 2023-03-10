# 인구이동 https://www.acmicpc.net/problem/16234
# DFS 

dx = [1,0,-1,0]
dy = [0,1,0,-1]

import sys

sys.setrecursionlimit(10000)

def dfs(loc, population, N, min, max):
    global stop, visited, country
    
    country.append(loc)
    
    x, y = loc
    
    visited[x][y] = 1

    
    for i in range(len(dx)):
        tmp_x = x + dx[i]
        tmp_y = y + dy[i]
        
        if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N or visited[tmp_x][tmp_y]:
            continue
        
        diff = abs(population[x][y] - population[tmp_x][tmp_y])
        if diff >= min and diff <= max:
            stop = False
            dfs((tmp_x, tmp_y), population, N, min, max)
    
N, L, R = map(int, input().split())
population = []
for _ in range(N):
    population.append(list(map(int,input().split())))


stop = False
count = 0
while not stop:
    visited = [[0] * N for _ in range(N)]
    stop = True
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                country = []
                line = dfs((x,y), population, N, L, R)
                sum = 0
                for c in country:
                    c_x, c_y = c
                    sum += population[c_x][c_y]
                
                for c in country:
                    c_x, c_y = c
                    population[c_x][c_y] = sum // len(country)
    if not stop:
        count += 1
    
print(count)
