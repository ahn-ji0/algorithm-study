N = int(input())
roads = list(map(int, input().split()))
price = list(map(int, input().split()))

buy = [0]
curr = price[0]
for i in range(1, N - 1):
    if price[i] < curr:
        buy.append(i)
        curr = price[i]
buy.append(N-1)
total = 0
for i in range(len(buy) - 1):
    total += price[buy[i]] * sum(roads[buy[i]:buy[i+1]])
print(total)