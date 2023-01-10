# 프로그래머스 주식 가격 https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 완전탐색 - 성공

def solution(prices):
    N = len(prices)
    answer = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
    return answer       

print(solution([1,2,3,2,3]))