# 1,2,3 더하기 5 - https://www.acmicpc.net/problem/15990

import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for i in range(N)]
max_num = max(nums)
dp = [[0 for i in range(3)] for j in range(max_num + 1)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, max_num + 1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009

for num in nums:
    print(sum(dp[num]) % 1000000009)