def solution():
    n = int(input())
    rgb_list = []
    for _ in range(n):
        rgb_list.append(list(map(int, input().split())))

    for i in range(1, n):
        rgb_list[i][0] += min(rgb_list[i-1][1], rgb_list[i-1][2])
        rgb_list[i][1] += min(rgb_list[i-1][0], rgb_list[i-1][2])
        rgb_list[i][2] += min(rgb_list[i-1][0], rgb_list[i-1][1])

    return min(rgb_list[n-1])


if __name__ == '__main__':
    print(solution())
