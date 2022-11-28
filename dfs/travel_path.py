# 프로그래머스 - 여행경로 https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 성공 - 테스트 케이스 여러가지 생각해 볼 필요 있는 문제

total = []

def dfs(start, tickets, path):
    
    if len(path)==len(tickets)+1:
        # total.append(path)만 해주면 path가 변함에 따라 total 내의 값도 변함. 즉 path를 참조하지 않고 복제한 것을 append 해야 함.
        total.append(list(path))
        return


    for i in range(len(tickets)):
        if used[i]==0 and tickets[i][0]==start:
            used[i] = 1
            path.append(tickets[i][1])
            dfs(tickets[i][1],tickets,path)
            path.pop()
            used[i] = 0

    
def solution(tickets):
    global used
    
    used = [0 for i in range(len(tickets))]
    
    dfs("ICN",tickets,["ICN"])
    
    total.sort()
    
    return total[0]

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))
