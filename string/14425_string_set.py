# https://www.acmicpc.net/problem/14425 문자열 집합

N, M = map(int, input().split())

S = []
for _ in range(N):
    S.append(input())

count = 0
for _ in range(M):
    word = input()
    if word in S:
        count += 1
        
print(count)