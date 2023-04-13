N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]
MAX = 10001
dp = [MAX for i in range(K+1)]
dp[0] = 0
for coin in coins:
    for i in range(0, K-coin+1):
        dp[i + coin] = min(dp[i] + 1, dp[i + coin])

if dp[K] == MAX:
    print(-1)
else:
    print(dp[K])