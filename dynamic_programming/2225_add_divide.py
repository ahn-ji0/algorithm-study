# 합 분헤 - https://www.acmicpc.net/problem/2225
N, K = map(int, input().split())

# def dfs(n, sum):
#     global cnt
#     if n == K - 1:
#         if N - sum >= 0 and N - sum <= N:
#             cnt += 1
#         return
#
#     for i in range(N+1):
#         dfs(n + 1, sum + i)
#
# cnt = 0
# dfs(0, 0)
# print(cnt)

if K == 1:
    print(1)
else:
    prev = [1 for i in range(N+1)]
    for k in range(K-1):
        curr = [0 for i in range(N+1)]
        for i in range(N+1):
            for j in range(N+1):
                if i + j <= N:
                    curr[i + j] += prev[i]
        prev = curr
    print(curr[N] % 1000000000)