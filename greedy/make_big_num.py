# 프로그래머스 - 큰 수 만들기 https://school.programmers.co.kr/learn/courses/30/lessons/42883

#내림차순으로 되어있는 숫자 제거

def solution(number, k):
    
    while(k>0):
        i = 0
        while number[i] >= number[i+1] and i<=len(number)-2 : i+=1
        number = number[0:i]  + number[i+1:]
        k -= 1

    return number

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
