# 13549 숨바꼭질 3 https://www.acmicpc.net/problem/1697

from queue import PriorityQueue

def solution(start, end):
    queue = PriorityQueue((0, start))
    
    visited = [False] * 1000001
    
    while queue:
        depth, x = queue.get()
        
        if x == end:
            return depth
        
        visited[x] = True
        
        for tmp_x in (x+1, x-1, 2*x):
            
            if tmp_x < 0 or tmp_x > 100000 or visited[tmp_x] == True:
                continue
            if tmp_x == end:
                return depth + 1
            queue.put((depth, tmp_x)) if tmp_x == 2*x else queue.put((depth + 1, tmp_x))
            
# start, end = map(int, input().split())
print(solution(5 , 6))