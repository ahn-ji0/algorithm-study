# 7562 https://www.acmicpc.net/problem/7562
# 

from collections import deque
dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

def bfs(graph,queue,end,count):
    # print(queue.popleft())
    if(not queue):
        return
    x, y = queue.popleft()
    
    for i in range(len(dx)):
        x_tmp = x + dx[i]
        y_tmp = y + dy[i]
    
        if(x_tmp == end[0] and y_tmp == end[1]):
            print("yes")
            return count
        
        if(x_tmp < 0 or x_tmp >= len(graph) or y_tmp < 0 or y_tmp >= len(graph)):
            return
        elif graph[x_tmp][y_tmp] == 1 :
            return
        else:
            queue.append((x_tmp,y_tmp))
            graph[x_tmp][y_tmp]=1
            return bfs(graph,queue,end,count+1)
    
def solution(l,start,end):
    graph = []
    queue = deque([start])
    for i in range(l):
        graph.append([0] * l)
    graph[start[0]][start[1]] = 1
    return bfs(graph,queue,end, 0)

l = int(input())
start = tuple(map(int,input().split()))
end= tuple(map(int,input().split()))
print(solution(l,start,end))
