# 나무 자르기 - https://www.acmicpc.net/problem/2805

def check(height):
    global heights
    
    count = 0
    for h in heights:
        if h > height:
            count += h - height
    
    return count

N, M = map(int, input().split())

heights = list(map(int, input().split()))

max = max(heights)
min = 0

while(min<=max):
    mid = (max + min) // 2
    
    cut = check(mid)
    if cut < M:
        max = mid - 1
    elif cut >= M:
        min = mid + 1
    else:
        max = mid
        break
print(max)
