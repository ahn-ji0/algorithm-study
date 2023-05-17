T = int(input())
for t in range(T):
    N = int(input())
    corridor = [0 for i in range(200)]
    for i in range(N):
        curr, to = map(int, input().split())
        curr = (curr + 1) // 2 - 1
        to = (to + 1) // 2 - 1

        if curr >= to:
            curr, to = to, curr

        for j in range(curr, to + 1):
            corridor[j] += 1


    print("#{} {}".format(t + 1, max(corridor)))