# 치킨 배달 - https://www.acmicpc.net/problem/15686
# 1. 처음 DFS로 접근 -> 시간초과 (조합이 아닌 순열로 접근 때문으로 추정)
# 2. 조합 함수 만들어서 사용 -> 정답

N, M = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(N)]

def get_chicken_distance(house, chickens):
    min_distance = 2 * N
    for i in range(len(chickens)):
        distance = abs(house[0] - chickens[i][0]) + abs(house[1] - chickens[i][1])
        if distance < min_distance:
            min_distance = distance

    return min_distance

def total_chicken_distance(chickens):
    total = 0
    for i in range(len(houses)):
        total += get_chicken_distance(houses[i], chickens)

    return total

def combinations(chickens, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(chickens)):
        element = chickens[i]
        for combi in combinations(chickens[i+1:], n - 1):
            result.append([element] + combi)

    return result

houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            houses.append((i,j))
        elif grid[i][j] == 2:
            chickens.append((i,j))

visited = [False for i in range(len(chickens))]
min_total = len(houses) * (2 * N)
for selected_chickens in combinations(chickens, M):
    total = total_chicken_distance(selected_chickens)
    if total < min_total:
        min_total = total

print(min_total)