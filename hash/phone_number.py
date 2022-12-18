# 프로그래머스 - 전화번호 목록 https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3
# 

def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[i] in phone_book[j][0:len(phone_book[i])]:
                return False
            
    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))

phone_book = ["123","456","789"]
print(solution(phone_book))

phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))
