# 주사위 윷놀이 - https://www.acmicpc.net/problem/17825

dice = list(map(int, input().split()))
START = 0
END = 0
start_stream = [(0,0), (1,2), (2,4),(3,6),(4,8), (5,10),(6,12),(7,14),(8,16),(9,18),(10,20),(17,22),(18,24),(19,26),(20,28),(21,30),(28,32),(29,34),(30,36),(31,38),(27,40), (32, END)]
ten_stream = [(5,10), (11,13), (12,16), (13,19), (14,25),(25,30), (26,35), (27,40),(32, END)]
twenty_stream = [(10,20), (15,22), (16,24), (14,25), (25,30), (26,35), (27,40),(32, END)]
thirty_stream = [(21,30), (22,28), (23,27), (24,26), (14,25), (25,30), (26,35), (27,40),(32, END)]

def move_stream(stream, idx):
    for i in range(len(to_blue)):
        if streams[stream][idx][0] == to_blue[i]:
            return i + 1

    return stream

def play_game(depth, visit, player, total):
    global max_value
    if depth == 10:
        max_value = max(max_value, total)
        return

    for i in range(len(player)):
        num, stream, idx, arrived = player[i]

        if arrived:
            continue

        to_idx = idx + dice[depth]

        # 끝났다면
        if to_idx >= len(streams[stream]) - 1:
            visit[num] = False
            player[i] = (num, stream, idx, True)
            play_game(depth+1, visit, player, total)
            player[i] = (num, stream, idx, False)
            visit[num] = True
            continue

        to_num = streams[stream][to_idx][0]
        # 누가 있다면
        if visit[to_num]:
            continue

        to_stream = move_stream(stream, to_idx)
        if to_stream != stream:
            to_idx = 0

        visit[num] = False
        visit[to_num] = True
        player[i] = (to_num, to_stream, to_idx, arrived)
        play_game(depth + 1, visit, player, total + streams[to_stream][to_idx][1])
        player[i] = (num, stream, idx, arrived)
        visit[to_num] = False
        visit[num] = True

to_blue = [5, 10, 21]
streams = [start_stream, ten_stream, twenty_stream, thirty_stream]
player = [(0, 0, 0, False) for i in range(4)]
visit = [False for j in range(33)]
max_value = 0
play_game(0, visit, player, 0)
print(max_value)