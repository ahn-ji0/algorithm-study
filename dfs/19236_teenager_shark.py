# 청소년 상어 - https://www.acmicpc.net/problem/19236
# DeepCopy에 대한 생각.

import copy

CLEAR = (-1,-1)
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
def fish_move(grid, fish, fish_visited, shark):
    for i in range(16):
        
        if fish_visited[i]:
            continue

        x, y, dir = fish[i]
        
        for j in range(8):
            tmp_dir = (dir + j) % 8
            tmp_x = x + dx[tmp_dir]
            tmp_y = y + dy[tmp_dir]
            if tmp_x < 0 or tmp_x >= 4 or tmp_y < 0 or tmp_y >=4:
                continue
            
            if tmp_x == shark[0] and tmp_y == shark[1]:
                continue
            if grid[tmp_x][tmp_y] == CLEAR:
                grid[tmp_x][tmp_y] = (i, tmp_dir)
                grid[x][y] = CLEAR
                fish[i] = (tmp_x,tmp_y, tmp_dir)
            else:
                change_num, change_dir = grid[tmp_x][tmp_y]
                grid[tmp_x][tmp_y] = (i, tmp_dir)
                grid[x][y] = (change_num, change_dir)
                fish[i] = (tmp_x, tmp_y, tmp_dir)
                fish[change_num] = (x,y,change_dir)
            break
            
    return grid

def do_something(shark, total, grid, fish, fish_visited):
    global answer
    
    new_grid = fish_move(grid, fish, fish_visited, shark)

    shark_x, shark_y, shark_dir = shark

    done = True
    for i in range(4):
        tmp_x = shark_x + (i+1) * dx[shark_dir]
        tmp_y = shark_y + (i+1) * dy[shark_dir]
        if tmp_x < 0 or tmp_x >= 4 or tmp_y < 0 or tmp_y >= 4:
            break
        
        # 빈칸
        if new_grid[tmp_x][tmp_y] == CLEAR:
            continue
        
        done = False
        tmp_num, tmp_dir = new_grid[tmp_x][tmp_y]
        new_grid[tmp_x][tmp_y] = CLEAR
        fish_visited[tmp_num] = True
        do_something((tmp_x, tmp_y, tmp_dir), total + tmp_num + 1, copy.deepcopy(new_grid), copy.deepcopy(fish), fish_visited)
        fish_visited[tmp_num] = False
        new_grid[tmp_x][tmp_y] = (tmp_num, tmp_dir)
    
    if done:
        answer.append(total)
    
grid = []
fish = [0 for i in range(16)]
for i in range(4):
    tmp = list(map(int, input().split()))
    
    tmp_grid = []
    for j in range(4):
        fish_num, fish_dir = tmp[2*j:2*j+2]
        tmp_grid.append((fish_num - 1, fish_dir - 1))
        fish[fish_num - 1] = (i, j, fish_dir - 1)
        
    grid.append(tmp_grid)
    
total, dir = grid[0][0]
grid[0][0] = CLEAR
fish_visited = [False for i in range(16)]
fish_visited[total] = True
answer = []
do_something((0, 0, dir), total + 1, grid, fish, fish_visited)
print(max(answer))