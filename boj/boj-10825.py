def solution():
    n = int(input())
    st_list = []
    for _ in range(n):
        st_list.append(tuple(input().split(" ")))
    st_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

    for s in st_list:
        print(s[0])


if __name__ == '__main__':
    solution()
