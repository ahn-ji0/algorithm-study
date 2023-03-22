# 기타 레슨 - https://www.acmicpc.net/problem/2343

def check(limit):
    global videos, M
    
    m_count = 0
    tmp_sum = 0
    
    for i in range(len(videos)):
        tmp_sum += videos[i]
        
        if tmp_sum > limit:
            tmp_sum = videos[i]
            m_count += 1
            
    if m_count <= M - 1: return 0
    else: return 1
    
N, M = map(int, input().split())

videos = list(map(int, input().split()))

total = sum(videos)

start = max(videos)
end = sum(videos)

while(start<=end):
    mid = (start + end) // 2
    
    val = check(mid)
    
    if val == 0:
        end = mid - 1
    else:
        start = mid + 1

print(start)
        
    