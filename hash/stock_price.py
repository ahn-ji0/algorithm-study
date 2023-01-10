# 프로그래머스 주식 가격 https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 해시 - 시간초과

from collections import defaultdict

def solution(prices):
    N = len(prices)
    MAX_PRICE = max(prices)
    answer = [0] * N
    stock = defaultdict(list)
    
    stock[prices[0]].append(0)
    for i in range(1, N-1):
        for key in stock:
           if prices[i] >= key:
               continue
           
           while stock[key]!=[]:
               idx = stock[key].pop()
               answer[idx] = i - idx
        
        stock[prices[i]].append(i)
    
    for key in stock:
        while stock[key]!=[]:
            idx = stock[key].pop()
            answer[idx] = N - 1 - idx
    
    return answer
    
prices = [1,2,3,2,3]
print(solution(prices))
