# 1309 https://www.acmicpc.net/problem/1309
# 

# 배열 N x 2
# 사자 최대 N마리 배치 가능할 듯.
# 사자 0마리 ~ N마리 배치하는 경우의 수 합
# 가로, 세로 붙어있을 수 없다면 방법은 대각선 밖에 없을 듯

#N = 4일때  배열은 4 x 2
# 0마리 배치하는 경우의 수 =1
# 1마리 = 8
# 2마리 
#      = 1100 1010 1001 0110 0101 0011
#      = 2    4     4    2    4    2 = 18
# 3마리 = 1110 1101 1011 0111
#      =  2    2*2  2*2  2   = 12
# 4마리 = 1111 = 2

import itertools

def count_group(values):
    all_values = itertools.permutations(values,len(values))
    all_count = 0
    
    for value in all_values:
        print(value)
        if(value[0]==1): count = 1
        else: count = 0
        
        for i in range(1,len(value)):
            if value[i] == 1 and value[i] != value[i-1]:
                count+=1
        
        print('count: ',count) 
        all_count += 2**count 
    return all_count

def cases_for_M(M,N):
    tmp = [0] * (N-M) + [1] * (M)
    cases = count_group(tmp) 
    return cases

N = int(input())

count = 0
for M in range(N):
    count+=cases_for_M(M,N)

print(count)