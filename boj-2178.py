from collections import deque


def solution():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input())))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if matrix[nx][ny] == 0:
                    continue
                if matrix[nx][ny] == 1:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append((nx, ny))

        return matrix[n-1][m-1]

    return bfs(0, 0)

if __name__ == '__main__':
    print(solution())
