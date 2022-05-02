def solution():
    n = int(input())
    answer = 0
    i = 1
    while True:
        if n // 5 ** i < 1:
            break
        answer += n // 5 ** i
        i += 1
    print(answer)


if __name__ == '__main__':
    solution()
