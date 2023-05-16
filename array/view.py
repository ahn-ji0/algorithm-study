# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1

T = 10
for t in range(T):
    N = int(input())
    buildings = list(map(int, input().split()))

    total = 0
    for i in range(len(buildings)):
        left = max(buildings[i-1], buildings[i-2]) if i >= 2 else 0
        right = max(buildings[i+1], buildings[i+2]) if i < len(buildings) - 2 else 0

        if left >= buildings[i] or right >= buildings[i]:
            continue

        total += buildings[i] - max(left, right)
    print("#{} {}".format(t+1, total))
