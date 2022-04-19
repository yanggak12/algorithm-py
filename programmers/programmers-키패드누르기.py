def solution(numbers, hand):
    answer = ''
    l = '*'
    r = '#'
    p_nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    for n in numbers:
        if n == 1 or n == 4 or n == 7 or n == '*':
            l = n
            answer += 'L'
        elif n == 3 or n == 6 or n == 9 or n == '#':
            r = n
            answer += 'R'
        else:
            l_t = tuple()
            r_t = tuple()
            n_t = tuple()
            for i in range(4):
                for j in range(3):
                    if l == p_nums[i][j]:
                        l_t = (i, j)
                    if r == p_nums[i][j]:
                        r_t = (i, j)
                    if n == p_nums[i][j]:
                        n_t = (i, j)
            if abs(n_t[0] - l_t[0]) + abs(n_t[1] - l_t[1]) > abs(n_t[0] - r_t[0]) + abs(n_t[1] - r_t[1]):
                r = n
                answer += 'R'
            elif abs(n_t[0] - l_t[0]) + abs(n_t[1] - l_t[1]) == abs(n_t[0] - r_t[0]) + abs(n_t[1] - r_t[1]):
                if hand == 'left':
                    l = n
                    answer += 'L'
                else:
                    r = n
                    answer += 'R'
            else:
                l = n
                answer += 'L'
    print(answer)
    return answer


if __name__ == '__main__':
    solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
    solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
    solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")
