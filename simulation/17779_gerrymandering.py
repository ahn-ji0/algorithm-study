# 게리맨더링 2 - https://www.acmicpc.net/problem/17779

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

def calculate(x, y, d1, d2):
    vals = [0 for i in range(5)]
    total = 0
    for i in range(N):
        for j in range(N):
            if i >= 0 and i < x + d1 and j >= 0 and j <= y and j < - i + x + y:
                vals[0] += arr[i][j]
            elif i >= 0 and i <= x + d2 and i < j + x - y and j > y and j < N:
                vals[1] += arr[i][j]
            elif i >= x + d1 and i < N and j >= 0 and j < y - d1 + d2 and j < i + y - x - 2 * d1:
                vals[2] += arr[i][j]
            elif i >= x + d2 and i > -j + x + y + 2 * d2 and i < N and j >= y - d1 + d2 and j < N:
                vals[3] += arr[i][j]

            total += arr[i][j]

    vals[-1] = total - sum(vals[:-1])
    vals.sort()

    return vals[-1] - vals[0]


min_val = 100 * N * N
for x in range(0, N-2):
    for y in range(1, N-1):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if y - d1 < 0 or y + d2 >= N or x + d1 + d2 >= N:
                    continue

                val = calculate(x,y,d1,d2)
                min_val = min(val, min_val)

print(min_val)

