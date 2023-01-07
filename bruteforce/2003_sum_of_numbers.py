# 2003 https://www.acmicpc.net/problem/2003

N, M = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(N):
    sum_of_num = 0
    for j in range(i,N):
        sum_of_num += A[j]
        if sum_of_num > M:
            break
        elif sum_of_num == M:
            count += 1
            break
        
print(count)