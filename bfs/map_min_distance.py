# 프로그래머스-게임 맵 최단거리 https://school.programmers.co.kr/learn/courses/30/lessons/1844


from collections import deque

# 북 동 남 서(시계방향)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

queue = deque()

def bfs(maps,depth):
    global queue
    
    if(not queue):
        return -1
    
    x,y = queue.popleft()
    
    visited[x][y] = 1
    
    for i in range(len(dx)):
        x_tmp = x + dx[i]
        y_tmp = y + dy[i]
        
        if(x_tmp < 0  or x_tmp >= n or y_tmp < 0 or y_tmp >= m or visited[x_tmp][y_tmp]==1 or maps[x_tmp][y_tmp]==0):
            continue
        
        if x_tmp==n-1 and y_tmp==m-1:
            return depth + 1
        
        queue.append([x_tmp,y_tmp])
    
    bfs(maps,depth+1)    
    
def solution(maps):
    global n, m, visited, queue
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for i in range(n)]
    queue.append([0,0])
    return bfs(maps,0)
    

game_map = [[1,1,1],[1,1,1],[1,0,1]]
print(solution(game_map))
