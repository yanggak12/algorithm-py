import sys
import heapq

N = int(input())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x:
        # 튜플을 통해 쌍 형태로 푸시해서 원본값까지 비교해서 힙 정렬
        heapq.heappush(heap, (abs(x), x))
    else:
        print(heapq.heappop(heap)[1] if heap else 0)
