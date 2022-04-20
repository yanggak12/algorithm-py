def solution(lottos, win_nums):
    answer = []
    max_a = 0
    min_a = 0

    for i in range(len(lottos)):
        if lottos[i] == 0:
            max_a += 1
            continue
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                max_a += 1
                min_a += 1
    answer.append(7 - max_a if 1 - max_a < 0 else 6)
    answer.append(7 - min_a if 1 - min_a <= 0 else 6)

    return answer


if __name__ == '__main__':
    solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
    solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
    solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])
