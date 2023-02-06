# 백준 12026 BOJ 거리 https://www.acmicpc.net/problem/12026
# dfs 사용 - 시간 초과

rule = ["B", "O", "J"]

def dfs(depth, n, energy, block):

    global N, answer
    
    if n == N-1:
        answer.append(energy)
        return
    elif rule[(depth + 1) % 3] not in block :
        return
    
    for i in range(1, len(block)):
        if block[i] == rule[(depth+1)%3]:
            energy += i * i
            dfs(depth + 1, n + i, energy, block[i:])
            energy -= i * i

N = int(input())
block = input()
answer = list()
dfs(0, 0, 0, block)
if not answer:
    print(-1)
else:
    print(min(answer))