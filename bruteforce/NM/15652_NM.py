# 15652 https://www.acmicpc.net/problem/15652
# 

s = []

def dfs(N,M):
    
    if len(s) == M:
        print(' '.join(s))
        return
    
    
    for i in range(1,N+1):
        s.append(i)
        dfs(N,M)
        s.pop()


def main():
    N, M = map(int, input().split())
    dfs(N,M)
    
main()        