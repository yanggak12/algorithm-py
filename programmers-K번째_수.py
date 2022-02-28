def solution(array, commands):
    answer = []
    for idx in range(len(commands)):
        i, j, k = commands[idx]
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])

    return answer
