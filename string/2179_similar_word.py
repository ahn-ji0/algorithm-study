# 비슷한 단어 - https://www.acmicpc.net/problem/2179

import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = ord('z') - ord('a') + 1
words = [[] for i in range(M)]
for i in range(N):
    word = input().rstrip()
    idx = ord(word[0]) - ord('a')
    words[idx].append((word, i))

def compare(w1, w2):
    cnt = 0
    for i in range(min(len(w1), len(w2))):
        if w1[i] != w2[i]:
            break
        cnt += 1

    return cnt


max_words = []
max_length = 0

for k in range(M):
    if len(words[k]) < 2:
        continue

    for i in range(len(words[k])):
        for j in range(i + 1, len(words[k])):
            l = compare(words[k][i][0], words[k][j][0])
            if l > max_length:
                max_length = l
                max_words = [(words[k][i][1], words[k][j][1],words[k][i][0], words[k][j][0])]
            elif l == max_length:
                heapq.heappush(max_words, (words[k][i][1], words[k][j][1], words[k][i][0], words[k][j][0]))

_, _, S, T = heapq.heappop(max_words)
print(S)
print(T)