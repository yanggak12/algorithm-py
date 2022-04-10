def solution():
    n = int(input())
    meet_arr = []
    cnt = 0
    now = 0
    for i in range(n):
        meet_arr.append(tuple(map(int, input().split())))
    meet_arr.sort(key=lambda x: (x[1], x[0]))
    for meet in meet_arr:
        if now <= meet[0]:
            cnt += 1
            now = meet[1]
    return cnt


if __name__ == '__main__':
    print(solution())
