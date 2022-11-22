# 7562 https://www.acmicpc.net/problem/7562
# 
dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]
cnt = []
def solution(l,from_coord,to_coord,count):
    if(from_coord == to_coord):
        cnt.append(count-1)
        return
    
    x, y = from_coord
    for i in range(len(dx)):
        x_tmp = x + dx[i]
        y_tmp = y + dy[i]
        if(x_tmp < 0 or x_tmp >= l or y_tmp < 0 or y_tmp >= l):
            return
        solution(l,[x_tmp,y_tmp],to_coord,count+1)

    
l = int(input())
from_coord = list(map(int,input().split()))
to_coord= list(map(int,input().split()))
solution(l,from_coord,to_coord,1)
print(min(cnt))