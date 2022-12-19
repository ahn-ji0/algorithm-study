# 1697 숨바꼭질 https://www.acmicpc.net/problem/1697

from collections import deque

def solution(start, end):
    queue = deque([(start, 0)])
    
    visited = [False] * 1000001
    
    while queue:
        x, depth = queue.popleft()
        
        if x == end:
            return depth
        
        visited[x] = True
        
        for i in range(3):
            if i == 0:
                tmp_x = x + 1
            elif i == 1:
                tmp_x = x - 1
            elif i == 2:
                tmp_x = 2 * x
            
            if tmp_x < 0 or tmp_x > 100000 or visited[tmp_x] == True:
                continue
            
            queue.append((tmp_x, depth + 1))

start, end = map(int, input().split())
print(solution(start, end))