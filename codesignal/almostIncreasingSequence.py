def solution(sequence):
    remove_count = 0
    if sequence[0] >= sequence[1]:
        remove_count += 1
    i = 2
    while i < len(sequence):
        if sequence[i-1] >= sequence[i]:
            remove_count += 1
            if sequence[i-2] >= sequence[i]:
                sequence[i] = sequence[i-1]
        i += 1

    return remove_count < 2


if __name__ == '__main__':
    print(solution([1, 3, 2, 1]))