# 10844 https://www.acmicpc.net/problem/10844
# 시간초과 ? 


'''길이가 n인 계단수(인접한 모든 자리의 차이가 1인 수)의 개수 구하기'''

# 첫째자리가 num으로 시작하는 계단수
def stair_num(n,num):
    if(num < 0 or num > 9):
        return 0
    if n == 1:
        return 1
    
    return stair_num(n-1, num+1) + stair_num(n-1, num-1)

#n은 100이하의 자연수. 즉 100자리까지 가능
def solution(n):
    count = 0
    for num in range(1,10):
        count += stair_num(n,num)
    return count % 1000000000

N = int(input())
print(solution(N))