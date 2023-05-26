# https://www.acmicpc.net/problem/7576
import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs():
    visited = [[0 for i in range(N)] for j in range(M)]

    for tomato in riped:
        t, x, y = tomato
        visited[x][y] = 1

    while riped:
        t, x, y = heapq.heappop(riped)

        for i in range(len(dx)):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
            if tmp_x < 0 or tmp_x >= M or tmp_y < 0 or tmp_y >= N or visited[tmp_x][tmp_y]:
                continue

            if time[tmp_x][tmp_y] == -1:
                continue

            visited[tmp_x][tmp_y] = 1
            time[tmp_x][tmp_y] = t + 1
            heapq.heappush(riped, (t+1, tmp_x, tmp_y))

def get_result():
    max_val = 0
    for i in range(M):
        for j in range(N):
            if time[i][j] == MAX_T:
                return -1

            if time[i][j] > max_val:
                max_val = time[i][j]

    return max_val

N, M = map(int, input().split())
boxes = [list(map(int, input().split())) for i in range(M)]
riped = []
MAX_T = M * N + 1
time = [[MAX_T for i in range(N)] for j in range(M)]
for i in range(M):
    for j in range(N):
        if boxes[i][j] == 1:
            riped.append((0, i, j))
            time[i][j] = 0
        elif boxes[i][j] == -1:
            time[i][j] = -1

bfs()
answer = get_result()
print(answer)