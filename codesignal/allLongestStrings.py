def solution(inputArray):
    max_len = 0
    output_list = []
    for s in inputArray:
        if len(s) > max_len:
            max_len = len(s)
    for s in inputArray:
        if len(s) == max_len:
            output_list.append(s)

    return output_list

# 좋은 다른 풀이
# def solution(inputArray):
#     m = max(len(s) for s in inputArray)
#     r = [s for s in inputArray if len(s) == m]
#     return r


if __name__ == '__main__':
    print(solution(["aba", "aa", "ad", "vcd", "aba"]))