def solution(n):
    if n == 1:
        return 1
    return solution(n-1) + 4*(n-1)

if __name__ == '__main__':
    print(solution(3))