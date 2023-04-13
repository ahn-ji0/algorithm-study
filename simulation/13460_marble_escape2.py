import copy

N, M = map(int, input().split())
grid = [list(input()) for i in range(N)]

r_x, r_y, b_x, b_y = 0,0,0,0
for i in range(1, N-1):
    for j in range(1, M-1):

        if grid[i][j] == 'R':
            r_x, r_y = i, j
        elif grid[i][j] == 'B':
            b_x, b_y = i, j

dx = [0,1,0,-1]
dy = [1,0,-1,0]
# def move_marble(x, y, d, tmp_grid, color):
#     tmp_grid[x][y] = '.'
#     while tmp_grid[x][y] == '.':
#         x, y = x + dx[d], y + dy[d]
#         if tmp_grid[x][y] == 'O':
#             return x, y, True
#
#     x, y = x - dx[d], y - dy[d]
#
#     tmp_grid[x][y] = color
#     return x, y, False
#
# def blue_in_line(red, blue, d):
#     while red[0] >= 0 and red[0] < N and red[1] >= 0 and red[1] < M:
#         red = (red[0] + dx[d], red[1] + dy[d])
#         if red == blue:
#             return True
#     return False
def move(n, red, blue, visited):
    global answer

    if n > 10:
        return

    for i in range(len(dx)):

        r_tmp_x, r_tmp_y = red
        b_tmp_x, b_tmp_y = blue

        r_cnt = 0
        while grid[r_tmp_x + dx[i]][r_tmp_y + dy[i]] != '#' and grid[r_tmp_x][r_tmp_y] != 'O':
            r_tmp_x += dx[i]
            r_tmp_y += dy[i]
            r_cnt += 1

        b_cnt = 0
        while grid[b_tmp_x + dx[i]][b_tmp_y + dy[i]] != '#' and grid[b_tmp_x][b_tmp_y] != 'O':
            b_tmp_x += dx[i]
            b_tmp_y += dy[i]
            b_cnt += 1


        if grid[b_tmp_x][b_tmp_y] != 'O':
            if grid[r_tmp_x][r_tmp_y] == 'O':
                answer.append(n)
                return
        else:
            continue

        if (r_tmp_x, r_tmp_y) == (b_tmp_x, b_tmp_y):
            # 앞에 있는 애가 어떤 앤지
            if b_cnt > r_cnt:
                # R이 앞이야
                b_tmp_x -= dx[i]
                b_tmp_y -= dy[i]
            else:
                r_tmp_x -= dx[i]
                r_tmp_y -= dy[i]

        if not visited[r_tmp_x][r_tmp_y][b_tmp_x][b_tmp_y]:
            visited[r_tmp_x][r_tmp_y][b_tmp_x][b_tmp_y] = 1
            move(n+1, (r_tmp_x, r_tmp_y), (b_tmp_x, b_tmp_y), visited)
            visited[r_tmp_x][r_tmp_y][b_tmp_x][b_tmp_y] = 0




        # if blue_in_line(red, blue, i):
        #     # 파랑 움직이고
        #     blue_x, blue_y, blue_in = move_marble(blue[0], blue[1], i, new_grid, 'B')
        #     # 빨강 움직이고
        #     red_x, red_y, red_in = move_marble(red[0], red[1], i, new_grid, 'R')
        # else:
        #     # 빨강 움직이고
        #     red_x, red_y, red_in = move_marble(red[0], red[1], i, new_grid, 'R')
        #     # 파랑움직이고
        #     blue_x, blue_y, blue_in = move_marble(blue[0], blue[1], i, new_grid, 'B')

        # if blue_in:
        #     return
        # elif red_in:
        #     answer.append(n)
        #     return
        #
        # move(n + 1, i, (red_x,red_y), (blue_x, blue_y), new_grid)


answer = []
visited =[[[[0 for i in range(M)] for j in range(N)] for k in range(M)] for l in range(N)]
visited[r_x][r_y][b_x][b_y] = 1
move(1, (r_x, r_y), (b_x, b_y), visited)
if not answer:
    print(-1)
else:
    print(min(answer))