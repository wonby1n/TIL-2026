'''
양방향 그래프
1번 정점에서 N번 정점까지 최단거리로 가고 싶음
v1, v2 정점은 반드시 통과해서 가야 함
중복 방문 가능
'''

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def dijkstra(start_node, graph, N):
    # 무한대로 거리 정해두기
    dist = [INF] * (N+1)
    dist[start_node] = 0

    # heap 사용
    q = []
    # 거리, 시작 노드 넣어주기
    heappush(q, (0, start_node))

    while q:
        now_dist, now_node = heappop(q)

        # 만약 더 작은 값이 있다면 스킵하기
        if now_dist > dist[now_node]:
            continue

        for next_node, cost in graph[now_node]:
            next_dist = now_dist + cost

            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heappush(q, (next_dist, next_node))

    return dist


# 정점의 개수 N, 간선의 개수 E
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

v1, v2 = map(int, input().split())

INF = 10**15

# 총 3번 하기
dist1 = dijkstra(1, graph, N)
distV1 = dijkstra(v1, graph, N)
distV2 = dijkstra(v2, graph, N)

# 1 -> v1 -> v2 -> N
path1 = dist1[v1] + distV1[v2] + distV2[N]
# 1 -> v2 -> v1 -> N
path2 = dist1[v2] + distV2[v1] + distV1[N]   

ans = min(path1, path2)

if ans >= INF:
    print(-1)
else:
    print(ans)