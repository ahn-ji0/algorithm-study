# 공통 부분 문자열 - https://www.acmicpc.net/problem/5582

import sys
input = sys.stdin.readline

string1 = input()
string2 = input()
N = len(string1)
M = len(string2)
dp = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    for j in range(M):
        if string1[i] == string2[j]:
            dp[i][j] = 1
max_cnt = 0
for i in range(N):
    for j in range(M):
        if dp[i][j] == 1:
            cnt = 0
            tmp_i, tmp_j = i, j
            while dp[tmp_i][tmp_j] == 1:
                dp[tmp_i][tmp_j] = 0
                cnt += 1
                tmp_i += 1
                tmp_j += 1
                if tmp_i >= N or tmp_j >= M:
                    break
            max_cnt = max(max_cnt, cnt)

print(max_cnt)

