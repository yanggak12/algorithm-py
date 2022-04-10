def solution(statues):
    cnt = 0
    sorted_statues = sorted(statues)
    for i in range(1, len(sorted_statues)):
        if sorted_statues[i] - sorted_statues[i - 1] != 1:
            cnt += sorted_statues[i] - sorted_statues[i - 1] - 1
    return cnt


if __name__ == '__main__':
    print(solution([6, 2, 3, 8]))
