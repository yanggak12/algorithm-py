def solution():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    min_index = 0
    for i in range(len(array)):
        if array[min_index] > i:
            min_index = i
    print(array[min_index])


if __name__ == '__main__':
    solution()


