from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    today = 0
    idx = -1
    dq = deque(progresses)
    for i in range(len(dq)):
        this = dq.popleft()
        day = math.ceil((100-this) / speeds[i])
        if day > today:
            today = day
            idx += 1
            cnt = 1
            answer.append(cnt)
        else:
            answer[idx] += 1
    return answer
