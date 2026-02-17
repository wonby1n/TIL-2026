import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    dist = [INF] * (n + 1)
    prev = [0] * (n + 1)

    dist[start] = 0
    q = [(0, start)]  # (비용, 도시)

    while q:
        cost, now = heapq.heappop(q)

        # 이미 더 싼 경로로 처리됐으면 무시
        if cost != dist[now]:
            continue

        for nxt, w in graph[now]:
            ncost = cost + w

            # 더 싸면 갱신 + 어디서 왔는지 기록
            if ncost < dist[nxt]:
                dist[nxt] = ncost
                prev[nxt] = now
                heapq.heappush(q, (ncost, nxt))

    # 경로 복원 (end에서 start까지 거꾸로 따라가기)
    path = []
    cur = end
    while cur:
        path.append(cur)
        if cur == start:
            break
        cur = prev[cur]

    path.reverse()
    return dist[end], path

# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    # 출발도시, 도착도시, 버스비용
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 구하고 싶은 출발도시, 도착도시
start, end = map(int, input().split())

INF = float('inf')

cost, path = dijkstra(start)
print(cost)
print(len(path))
print(*path)