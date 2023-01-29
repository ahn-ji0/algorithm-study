answer=0
def solution(numbers, target):
    
    def dfs(sum_,indx):
        global answer
        if(indx==len(numbers)):
            if(sum_==target):
                answer = answer+ 1
            return
        dfs(sum_+numbers[indx],indx+1)
        dfs(sum_-numbers[indx],indx+1)
    
    dfs(0,0)
    return answer

print(solution([1,1,1,1,1],3))

answer = 0
print(solution([4,1,2,1],4))

