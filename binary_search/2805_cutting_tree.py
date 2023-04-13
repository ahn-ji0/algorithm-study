# 나무자르기 - https://www.acmicpc.net/problem/2805

N, M = map(int, input().split())
trees = list(map(int, input().split()))

def get_total(H):
    total = 0
    for tree in trees:
        total += tree - H if tree - H > 0 else 0
    return total
def binary_search():
    start = 0
    end = max(trees)
    while start <= end:
        mid = (start + end) // 2
        total = get_total(mid)
        if total < M:
            end = mid - 1
        elif total > M:
            start = mid + 1
        else:
            return mid
    return end

print(binary_search())


