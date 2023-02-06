# 프로그래머스 피로도 https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 완전탐색 - dfs

def dfs(k,visited):  
    for i in range(len(map)):
        if not visited[i] and k >= map[i][0]:
            visited[i] = 1
            dfs(k-map[i][1], visited)
            visited[i] = 0
    
    cases.append(sum(visited))          
    return

def solution(k, dungeons):
    global map, cases
    map = dungeons
    cases = list()
    
    visited = [0] * len(dungeons)
    dfs(k, visited)
    return max(cases)

print(solution(80,[[80,20],[50,40],[30,10]]))