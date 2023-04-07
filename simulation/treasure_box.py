# SWEA 보물상자 비밀번호 - https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K= map(int, input().split())
    hex = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8,
           "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

    nums_string = list(input())
    nums = [hex[i] for i in nums_string]

    each = int(N/4)
    start_idx = 0
    numbers = set()
    for i in range(each):
        curr_idx = start_idx
        for j in range(4): #각변
            tmp_num = 0
            for digit in range(each): # 각숫자
                tmp_num += nums[curr_idx] * 16 ** (each-1-digit)
                curr_idx = (curr_idx + 1) % N
            numbers.add(tmp_num)

        start_idx = (start_idx - 1) % N

    final_nums = sorted(list(numbers), reverse=True)
    print("#{} {}".format(test_case, final_nums[K-1]))