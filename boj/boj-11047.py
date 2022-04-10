import sys


def solution():
    n, k = map(int, sys.stdin.readline().split())
    arr = []
    cnt = 0
    for i in range(n):
        val = int(sys.stdin.readline().split()[0])
        arr.append(val)

    for i in reversed(range(len(arr))):
        cnt += int(k/arr[i])
        k = k % arr[i]

    return cnt


if __name__ == '__main__':
    print(solution())
