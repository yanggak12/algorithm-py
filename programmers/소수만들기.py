import math
from itertools import combinations


def is_prime_num(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def solution(nums):
    answer = 0
    for num in list(combinations(nums, 3)):
        this_num = num[0] + num[1] + num[2]
        if is_prime_num(this_num):
            answer += 1

    return answer


if __name__ == '__main__':
    solution([1, 2, 3, 4])
    solution([1, 2, 7, 6, 4])
