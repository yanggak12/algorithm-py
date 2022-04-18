from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_set = set(report)
    reported = defaultdict(int)
    report_record = defaultdict(set)
    temp = []
    for r in report_set:
        a, b = r.split(" ")
        reported[b] += 1
        report_record[a].add(b)

        if reported[b] == k:
            temp.append(b)
    print(report_record, temp)
    for t in temp:
        for i in range(len(id_list)):
            if t in report_record[id_list[i]]:
                answer[i] += 1

    return answer


if __name__ == '__main__':
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2)
