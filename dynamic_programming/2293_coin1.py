N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]
coins.sort()

dp = [0 for i in range(K+1)]
dp[0] = 1
for coin in coins:
    for i in range(0, K - coin + 1):
        dp[i + coin] += dp[i]

print(dp[K])