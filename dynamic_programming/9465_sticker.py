# 스티커 - https://www.acmicpc.net/problem/9465

T = int(input())
for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for i in range(2)]

    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue

    dp = [[0 for i in range(n)] for j in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[0][1] = sticker[0][1] + dp[1][0]
    dp[1][1] = sticker[1][1] + dp[0][0]

    for j in range(2, n):
        for i in range(2):
            dp[i][j] = max(dp[(i+1) % 2][j-1], dp[i][j-2], dp[(i+1) % 2][j-2]) + sticker[i][j]

    max_val = 0
    for i in range(2):
        max_val = max(max_val, max(dp[i]))
    print(max_val)