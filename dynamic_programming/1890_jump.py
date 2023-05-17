from collections import deque
N = int(input())
grid = [list(map(int, input().split())) for i in range(N)]

dp = [[0 for i in range(N)] for j in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if (i, j) == (N-1, N-1):
            continue

        jump = grid[i][j]
        if i + jump < N:
            dp[i+jump][j] += dp[i][j]
        if j + jump < N:
            dp[i][j + jump] += dp[i][j]

print(dp[N-1][N-1])
