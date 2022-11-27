# 프로그래머스 - 여행경로 https://school.programmers.co.kr/learn/courses/30/lessons/43164
def dfs(start, tickets):
    
    path.append(start)

    if sum(used)==len(tickets):
        return

    min_end = "ZZZ"
    min_idx = 0

    for i in range(len(tickets)):
        if used[i]==0 and tickets[i][0]==start:
            if tickets[i][1] <= min_end:
                min_end = tickets[i][1]
                min_idx = i

    used[min_idx] = 1
    end = min_end
    dfs(end,tickets)
    
def solution(tickets):
    global used
    global path

    used = [0 for i in range(len(tickets))]
    path = list()
    
    dfs("ICN",tickets)
    return path

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))
