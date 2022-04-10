def solution(matrix):
    answer = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                for k in range(len(matrix)):
                    matrix[k][j] = 0
            else:
                answer += matrix[i][j]
    return answer


if __name__ == '__main__':
    print(solution([[0, 1, 1, 2],
                    [0, 5, 0, 0],
                    [2, 0, 3, 3]]))
