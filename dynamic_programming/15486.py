import sys
input = sys.stdin.readline

N = int(input())

time = []
price = []

for i in range(N):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)

dp = [0 for i in range(N + 1)]

max_val = 0
for i in range(N-1, -1, -1):
    if i + time[i] > N:
        dp[i] = max_val
        continue


    dp[i] = max(dp[i + time[i]] + price[i], max_val)
    max_val = max(dp[i], max_val)
print(dp[0])

