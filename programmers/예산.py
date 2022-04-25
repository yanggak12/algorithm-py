

def solution(d, budget):
    answer = 0
    d.sort()
    price = 0
    for i in range(len(d)):
        price += d[i]
        if price > budget:
            break
        answer += 1


    return answer


if __name__ == '__main__':
    solution([1, 3, 2, 5, 4], 9)
    solution([2, 2, 3, 3], 10)
