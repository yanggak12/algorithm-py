n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

big_one = arr[-1]
big_two = arr[-2]

cnt = int(m / (k+1)) * k  # arr의 가장 큰 수가 있는 개수

answer = cnt * big_one
answer += big_two * (m - cnt)
print(answer)
