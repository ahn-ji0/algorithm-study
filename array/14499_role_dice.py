# 주사위 굴리기 - 공간과 배열
dx = [0,0,-1,1]
dy = [1,-1,0,0]
N, M, x, y, K = map(int, input().split())

grid = list()
for i in range(N):
    grid.append(list(map(int, input().split())))
    
inst = list(map(int, input().split()))

# 나, 반대편, 위, 아래, 왼쪽, 오른쪽
curr = [[0, 0], [0, 0], [0, 0]]

# 오른쪽 1, 왼쪽 2, 위쪽 3, 아래쪽 4
for dir in inst:
    tmp_x = x + dx[dir-1]
    tmp_y = y + dy[dir-1]
    
    if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= M:
        continue
    
    x = tmp_x
    y = tmp_y
    
    if dir == 1:
        curr = [curr[2][::-1], curr[1], curr[0]]
    elif dir == 2:
        curr = [curr[2], curr[1], curr[0][::-1]]
    elif dir == 3:
        curr = [curr[1], curr[0][::-1], curr[2]]
    else:
        curr = [curr[1][::-1], curr[0],  curr[2]]

    if grid[x][y] == 0:
        grid[x][y] = curr[0][0]
    else:
        curr[0][0] = grid[x][y]
        grid[x][y] = 0
        
    print(curr[0][1])