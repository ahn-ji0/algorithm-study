# 백준 10026 적록색약 - https://www.acmicpc.net/problem/10026

def num_regions(grid):
    
    return 0

N = int(input())

grid = []

for _ in range(N):
    row = input()
    grid.append(row)

# 보통 사람
general = num_regions(grid)

# 적록 색맹인 사람
for i in range(N):
    grid[i] = grid[i].replace("G", "R")

daltonism = num_regions(grid)
