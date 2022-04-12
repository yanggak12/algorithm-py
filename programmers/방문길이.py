def solution(dirs):
    x = 0
    y = 0
    visited = set()
    for d in dirs:
        if d == 'U':
            if abs(y+1) > 5:
                continue
            visited.add((x, y, x, y + 1))
            visited.add((x, y + 1, x, y))
            y += 1
        elif d == 'D':
            if abs(y-1) > 5:
                continue
            visited.add((x, y, x, y - 1))
            visited.add((x, y - 1, x, y))
            y -= 1
        elif d == 'R':
            if abs(x+1) > 5:
                continue
            visited.add((x, y, x + 1, y))
            visited.add((x + 1, y, x, y))
            x += 1
        elif d == 'L':
            if abs(x-1) > 5:
                continue
            visited.add((x, y, x - 1, y))
            visited.add((x - 1, y, x, y))
            x -= 1

    return int((len(visited) / 2))


if __name__ == '__main__':
    print(solution("LULLLLLLU"))
