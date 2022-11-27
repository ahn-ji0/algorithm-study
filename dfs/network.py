# 프로그래머스 - 네트워크 https://school.programmers.co.kr/learn/courses/30/lessons/43162

def dfs(i,n,computers):
    global visited
    visited[i] = 1
    for j in range(n):
        if(i != j and computers[i][j] == 1 and visited[j]==0):
            dfs(j,n,computers)
            
def solution(n,computers):
    global visited 
    
    visited = [0 for i in range(n)]
    count = 0
    
    for i in range(n):
        if(visited[i]==1):
            continue
        dfs(i,n,computers)
        count += 1
    
    return count

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n,computers))