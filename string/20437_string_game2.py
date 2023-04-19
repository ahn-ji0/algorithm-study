# 문자열 게임 2 - https://www.acmicpc.net/problem/20437

import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    word = input().strip()
    K = int(input())

    alphabet = dict()
    for i in range(len(word)):
        if word[i] not in alphabet:
            alphabet[word[i]] = []
        else:
            prev = alphabet[word[i]][-1]

        alphabet[word[i]].append(i)

    min_val = len(word) + 1
    max_val = -1

    for k in alphabet.keys():
        idxs = alphabet[k]
        if len(idxs) < K:
            continue
        for i in range(K-1, len(idxs)):
            val = idxs[i] - idxs[i - K + 1] + 1
            min_val = min(min_val, val)
            max_val = max(max_val, val)

    if max_val == -1:
        print(-1)
        continue

    print(min_val, max_val)


