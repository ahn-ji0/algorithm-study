from itertools import product

N, K = map(int, input().split())

count = 0
for case in product(set(range(N+1)), repeat =K):
    if sum(case) == N:
        count += 1
        
print(count)