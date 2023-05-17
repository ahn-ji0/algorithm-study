n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]

dp = [0 for i in range(k + 1)]

dp[0] = 1
for coin in coins:
    for i in range(k + 1 - coin):
        dp[i + coin] += dp[i]

print(dp[-1])