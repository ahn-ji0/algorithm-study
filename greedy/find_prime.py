# 프로그래머스 소수 찾기 https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 완료!

from itertools import permutations

def isPrime(number):
    num = int("".join(list(number)))
    if num == 1:
        return False
    prime = True
    i = 2
    while(i * i <= num):
        if num % i == 0:
            prime = False
        i += 1
    return prime
    
    
def solution(numbers):
    n = len(numbers)
    cases = set()
    for i in range(1,n+1):
        for tup in permutations(numbers,i):
            if(tup[0] != '0'):
                s = ''.join(tup)
                cases.add(s)
    
    count = 0
    print(cases)
    for case in cases:
        count+= isPrime(case)
    
    return count

print(solution("17") == 3)
print(solution("011") == 2)

