# https://www.acmicpc.net/problem/10972

N = int(input())
arr = list(map(int, input().split()))
queue = list()

def solution(arr):
    if N == 1:
        return -1

    last = False
    while True:
        queue.append(arr.pop())
        if not arr:
            last = True
            break

        if arr[-1] < queue[-1]:
            break
    if last:
        return -1

    queue.sort()
    for i in range(len(queue)):
        if queue[i] > arr[-1]:
            break

    arr[-1], queue[i] = queue[i], arr[-1]

    arr = arr + sorted(queue)

    return ' '.join(str(i) for i in arr)

print(solution(arr))
