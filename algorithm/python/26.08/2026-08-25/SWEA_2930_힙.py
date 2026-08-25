# 1 x : 최대 힙에 x를 삽입
# 2 : 최대 힙에서 최댓값을 삭제하고 출력

import heapq

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    heap = []
    result = []

    for _ in range(N):
        command = list(map(int, input().split()))

        if command[0] == 1:
            value = command[1]
            heapq.heappush(heap, -value)
        else:
            if heap:
                result.append(-heapq.heappop(heap))
            else:
                result.append(-1)

    print(f"#{tc}", *result)