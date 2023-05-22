
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(N)]

def combinations(arr, n):

    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        element = arr[i]
        for combi in combinations(arr[i+1:], n-1):
            result.append([element] + combi)

    return result

def single_chicken_distance(chickens, single_home):
    min_distance = 2 * N
    for chicken in chickens:
        distance = abs(chicken[0] - single_home[0]) + abs(chicken[1] - single_home[1])
        min_distance = min(min_distance, distance)

    return min_distance

def total_chicken_distance(chickens, home):
    total = 0
    for single_home in home:
        total += single_chicken_distance(chickens, single_home)
    return total

chicken = []
home = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            chicken.append((i,j))
        elif grid[i][j] == 1:
            home.append((i,j))

min_val = 2 * N * len(home)
for combi in combinations(chicken, M):
    temp = total_chicken_distance(combi, home)
    min_val = min(temp, min_val)

print(min_val)