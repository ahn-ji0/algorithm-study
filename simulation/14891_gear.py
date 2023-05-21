gear = [list(input()) for i in range(4)]
# 0 1 *2* 3 4 5 *6* 7

K = int(input())
rotate = [tuple(map(int, input().split())) for i in range(K)]

def do_rotate(num, dir):
    if dir == 1:
        gear[num] = gear[num][-1:] + gear[num][:-1]
    else:
        gear[num] = gear[num][1:] + gear[num][:1]

def get_status():
    status = []
    for i in range(3):
        if gear[i][2] == gear[i+1][6]:
            status.append(0)
        else:
            status.append(1)

    return status

for num, dir in rotate:
    status = get_status()
    num -= 1
    do_rotate(num, dir)

    tmp_num, tmp_dir = num, dir
    while tmp_num - 1 >= 0 and status[tmp_num - 1] == 1:
        tmp_num -= 1
        tmp_dir *= (-1)
        do_rotate(tmp_num, tmp_dir)

    tmp_num, tmp_dir = num, dir
    while tmp_num < 3 and status[tmp_num] == 1:
        tmp_num += 1
        tmp_dir *= (-1)
        do_rotate(tmp_num, tmp_dir)

total = 0
for i in range(4):
    if gear[i][0] == '1':
        total += 2 ** i

print(total)


