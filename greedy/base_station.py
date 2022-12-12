# 프로그래머스 - 기지국 설치 https://school.programmers.co.kr/learn/courses/30/lessons/12979

def solution(n, stations, w):
    no_stations =  []
    from_ = 1
    
    for i in range(len(stations)):
        to = stations[i] - w - 1
        no_stations.append(to - from_ + 1)
        from_ = stations[i] + w + 1
    
    if from_ <= n :
        no_stations.append(n - from_ + 1)
        
    count = 0
    
    for empty in no_stations:
        if empty % (2 * w + 1) == 0 :
            count += empty // (2 * w + 1)
        else:
            count += empty // (2 * w + 1) + 1
        
    return count

print(solution(11,[4,11],1))
print(solution(16,[9],2))
