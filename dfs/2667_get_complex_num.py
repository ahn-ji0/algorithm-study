N = int(input())

grid = [list(input()) for i in range(N)]
total = []

dx = [1, 0 ,-1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y):
    global cnt
    visited[x][y] = 1
    cnt += 1

    for i in range(len(dx)):
        tmp_x = x + dx[i]
        tmp_y = y + dy[i]
        if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N or visited[tmp_x][tmp_y] or grid[tmp_x][tmp_y] == '0':
            continue

        dfs(tmp_x, tmp_y)

visited = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j] and grid[i][j] == '1':
            cnt = 0
            dfs(i,j)
            total.append(cnt)

total.sort()
print(len(total))
for val in total:
    print(val)