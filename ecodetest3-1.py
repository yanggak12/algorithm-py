# 거스름돈 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정하고, 거슬러줘야 할 돈이 N원이라면 거슬러줘야 할 동전의 최소 개수를 구하라. (N은 10의 배수)

N = int(input())
cnt = 0

coin_types = [500,100,50,10]

for coin in coin_types:
    cnt += N // coin
    N %= coin # %= 나머지를 왼쪽 변수에 할당 n = n % coin

print(cnt)
