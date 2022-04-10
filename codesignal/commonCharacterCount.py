def solution(s1, s2):
    answer = 0
    s_set = set([])
    if len(s1) < len(s2):
        smaller_s = s1
        larger_s = s2
    else:
        smaller_s = s2
        larger_s = s1

    for w in smaller_s:
        if larger_s.find(w) >= 0:
            s_set.add(w)
    for s in s_set:
        answer += min(smaller_s.count(s), larger_s.count(s))
    return answer

# Best Code
# def solution(s1, s2):
#     com = [min(s1.count(i), s2.count(i)) for i in set(s1)]
#     return sum(com)


if __name__ == '__main__':
    print(solution("aabcc", "adcaa"))