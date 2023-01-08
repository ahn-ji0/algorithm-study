# 2003 https://www.acmicpc.net/problem/2003
# 완료

N, M = map(int, input().split())
A = list(map(int, input().split()))

count = 0
sum_of_num = A[0]
left = 0
i = 1
while(True):
    if sum_of_num == M:
        count+=1
        sum_of_num -= A[left]
        left += 1
    elif sum_of_num > M:
        sum_of_num -= A[left]
        left += 1
    else:
        if i < N:
            sum_of_num += A[i]
            i +=1
        else:
            break

print(count)