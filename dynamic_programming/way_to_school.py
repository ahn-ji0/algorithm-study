# 프로그래머스 등굣길 - https://school.programmers.co.kr/learn/courses/30/lessons/42898

def paths(info, x, y):
    if x == 0 and y == 0:
        return 1
    elif x < 0 or x >= len(info) or y < 0 or y >= len(info[0]):
        return 0
    elif info[x][y]: 
        return 0
    
    return paths(info, x - 1, y) + paths(info, x, y-1)
    
def solution(m, n, puddles):
    info = [[0 for i in range(m)] for j in range(n)]
    
    for coord in puddles:
        x, y = coord
        info[y-1][x-1] = 1
    
    return paths(info, n - 1, m - 1) % 1000000007

print(solution(4,3,[[2,2]]))