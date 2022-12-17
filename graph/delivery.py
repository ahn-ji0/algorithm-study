#프로그래머스 배달 https://school.programmers.co.kr/learn/courses/30/lessons/12978
# 다익스트라 알고리즘
MAX_DISTANCE = 10001

def find_min_distance(visited, distance):
    min_distance = MAX_DISTANCE
    min_idx = -1
    
    for idx in range(len(distance)):
        if visited[idx] == 0 and distance[idx] < min_distance:
            min_distance = distance[idx]
            min_idx = idx
            
    return min_idx
        
def solution(N, road, K):
    graph = [[] for _ in range(N)]
    distance = [MAX_DISTANCE for _ in range(N)]
    visited = [0 for _ in range(N)]
    for edge in road:
        start, end, weight = edge
        graph[start-1].append((end-1,weight))
        graph[end-1].append((start-1,weight))
    
    visited[0] = 1
    for neighbor in graph[0]:
        end, weight = neighbor
        distance[end] = weight
        
    for _ in range(N-1):
        # distance 중 가장 작은 거 골라서 방문하고
        min_idx = find_min_distance(visited, distance)
        visited[min_idx] = 1
        # 이웃 distance 비교해서 update 해줘
        for neighbor in graph[min_idx]:
            end, weight = neighbor
            if end!=0 and distance[min_idx] + weight < distance[end]:
                distance[end] = distance[min_idx] + weight
                
    return sum(1 for i in distance if i <= K) + 1
    
        

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

print(solution(N,road,K))

N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4

print(solution(N,road,K))