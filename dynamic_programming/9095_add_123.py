# 1,2,3 더하기 - https://www.acmicpc.net/problem/9095
T = int(input())

dp = [0 for i in range(11)]
dp[1], dp[2], dp[3] = 1, 1, 1
for i in range(2, 11):
    dp[i] += dp[i-1] + dp[i-2]
    if i - 3 >= 0:
        dp[i] += dp[i-3]

for i in range(T):
    num = int(input())
    print(dp[num])
