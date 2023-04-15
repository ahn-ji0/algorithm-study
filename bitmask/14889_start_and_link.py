from itertools import combinations
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
total = 0
for i in range(N):
    total += sum(arr[i])

min_ability = 100 * N * N
for combi in combinations(range(N), N//2):
    ability = 0
    for i in combi:
        for j in combi:
            ability += arr[i][j]
    combi2 = set(range(N)) - set(combi)
    ability2 = 0
    for i in combi2:
        for j in combi2:
            ability2 += arr[i][j]

    min_ability = min(min_ability, abs(ability2 - ability))

print(min_ability)