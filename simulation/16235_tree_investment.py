# 나무 재테크 - https://www.acmicpc.net/problem/16235
# pypy3으로 제출

from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

A = []
for i in range(N):
    A.append(list(map(int,input().split())))

food = [[5 for i in range(N)] for j in range(N)]
tree = [[deque() for i in range(N)] for j in range(N)]
for i in range(M):
    x, y, age = map(int, input().split())
    tree[x-1][y-1].append(age)

di = [-1,-1,0,1,1,1,0,-1]
dj = [0,1,1,1,0,-1,-1,-1]

for year in range(K):
    for i in range(N):
        for j in range(N):
            # 봄
            count = 0
            for k in range(len(tree[i][j])):
                tmp_age = tree[i][j][k]
                if tmp_age <= food[i][j]:
                    food[i][j] -= tmp_age
                    tree[i][j][k] += 1
                    count += 1
                else: 
                    break
            
            # 여름
            for k in range(len(tree[i][j]) - count):
                tmp_age = tree[i][j].pop()
                food[i][j] += tmp_age // 2
    
    for i in range(N):
        for j in range(N):       
            # 가을
            for tree_age in tree[i][j]:
                if tree_age % 5 == 0:
                    for k in range(len(di)):
                        tmp_i = i + di[k]
                        tmp_j = j + dj[k]
                        if tmp_i < 0 or tmp_i >= N or tmp_j < 0 or tmp_j >= N:
                            continue
                        tree[tmp_i][tmp_j].appendleft(1)
                        
            # 겨울
            food[i][j] += A[i][j]

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])

print(answer)           