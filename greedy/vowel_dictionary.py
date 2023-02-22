# 프로그래머스 모음 사전 https://school.programmers.co.kr/learn/courses/30/lessons/84512

vowels = ["A", "E", "I", "O", "U"]

def find_all(depth, word):
    global total_words
    
    if depth == 5:
        return
    
    for i in range(len(vowels)):
        total_words.append(word + vowels[i])
        find_all(depth+1, word + vowels[i])

def solution(word):
    global total_words 
    total_words = list()
    
    find_all(0, "")
    
    return total_words.index(word) + 1

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))