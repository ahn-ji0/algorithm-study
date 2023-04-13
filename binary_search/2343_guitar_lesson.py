# 기타 레슨 - https://www.acmicpc.net/problem/2343

N, M = map(int, input().split())
lectures = list(map(int, input().split()))

start = max(lectures)
end = sum(lectures)

def get_num(d):
    cnt = 0
    total = 0
    for i in range(len(lectures)):
        total += lectures[i]
        if total > d:
            cnt += 1
            total = lectures[i]
    cnt += 1

    return cnt

while start <= end:
    mid = (start + end) // 2
    nums = get_num(mid)
    if nums > M:
        start = mid + 1
    elif nums <= M:
        end = mid - 1

print(start)
