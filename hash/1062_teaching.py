# 백준 1062 가르침 - https://www.acmicpc.net/problem/1062
# 먼저 다 set에 넣고, 합집합을 구한 후 antic 다섯개를 제외한 것 중에서 combination을 한 것들을 돌며 최댓값을 출력 -> 시간초과

from itertools import combinations


def solution(N, K, letters, all_letters):
    if(K - 5 < 0):
        return 0
    
    num_read = []
    for combi in combinations(all_letters, K - 5):
        count = 0
        for j in range(len(letters)):
            if not letters[j] - set(combi):
                count += 1
        num_read.append(count)
    
    return max(num_read)

N, K = map(int, input().split())

letters = []
all_letters = set()

for i in range(N):
    tmp_set = set(input())-set("antatica")
    
    if len(tmp_set) > K - 5 : continue
    
    all_letters = all_letters.union(tmp_set)
    letters.append(tmp_set)


print(solution(N,K,letters,all_letters))
