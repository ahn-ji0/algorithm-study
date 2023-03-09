# 톱니바퀴 https://www.acmicpc.net/problem/14891

gear = []
for _ in range(4):
    gear.append(input())

K = int(input())

info = []
for _ in range(K):
    info.append(tuple(map(int, input().split())))

def update_status():
    global gear

    status = []
    for i in range(1, 4):
        if gear[i][6] != gear[i-1][2]:
            status.append(1)
        else:
            status.append(0)
    return status

def rotate_gear(idx, direction, visited, status):
    global gear
    
    visited[idx] = True

    if idx > 0 and idx < 4 and status[idx-1] and not visited[idx-1]:
        rotate_gear(idx - 1, (-1) * direction, visited, status)
    if idx < 3 and idx > -1 and status[idx] and not visited[idx + 1]:
        rotate_gear(idx + 1, (-1) * direction, visited, status)
        
    # rotate
    if direction == 1:
        gear[idx] = gear[idx][-1] + gear[idx][:-1]
    else:
        gear[idx] = gear[idx][1:] + gear[idx][0]
        
for i in range(len(info)):
    idx = info[i][0] - 1
    direction = info[i][1]
    status = update_status()
    rotate_gear(idx, direction, [False] * 4, status)

answer = 0
for i in range(4):
    answer += int(gear[i][0]) * (2 ** i)
    
print(answer)