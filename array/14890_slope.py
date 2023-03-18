# 14890 경사로 https://www.acmicpc.net/problem/14890
# 배열, 구현

def check_scope(arr):
    global L
    
    count = [1]
    height = []
    idx = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            count[idx] += 1
        elif arr[i] == arr[i-1] + 1:
            count.append(1)
            idx += 1
            height.append('U')
        elif arr[i] == arr[i-1] - 1:
            count.append(1)
            idx += 1
            height.append('D')
        else:
            return 0
        
    for i in range(len(height)):
        if height[i] == 'U':
            if count[i] < L:
                return 0
        elif height[i] == 'D':
            if count[i+1] < L:
                return 0
            count[i+1] -= L
    
    return 1

N, L = map(int, input().split())

grid = []
for i in range(N):
    grid.append(list(map(int, input().split())))
    
count = 0
for i in range(N):
    count += check_scope(grid[i])
    count += check_scope(list(zip(*grid))[i])
    
print(count)