# 프로그래머스 카펫 - https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 수식 구현하는 방법으로 풀이 작성

# M x N 인 카펫의 노란색은 (M-2) * (N-2) = M*N -2M - 2N + 4 , 갈색은  2* M + 2* N - 4

import math

def solution(brown, yellow):
    a = (brown + 4) / 2
    b = brown + yellow
    
    answer = [int((a + math.sqrt(a**2 - 4*b))/2)]
    answer.append(int(b/answer[0]))
    
    return answer

print(solution(8,1))