def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for b in board:
            if b[m-1] != 0:
                if len(stack) > 0 and stack[-1] == b[m-1]:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(b[m-1])
                b[m-1] = 0
                break
    return answer


if __name__ == '__main__':
    solution([[0, 0, 0, 0, 0],
              [0, 0, 1, 0, 3],
              [0, 2, 5, 0, 1],
              [4, 2, 4, 4, 2],
              [3, 5, 1, 3, 1]],
             [1, 5, 3, 5, 1, 2, 1, 4])
