# 갈 때, 올 때 두 번 사용해야 함

from heapq import heappop, heappush

def dijkstra(start, graph):
    INF = float('inf')
    distance = [INF] * (N + 1)
    distance[start] = 0

    pq = [(0, start)]

    while pq:

        # 지금 갈 수 있는 곳 중 제일 싼 곳
        dist, now = heappop(pq)

        # 더 싼 곳 있으면 pass
        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            new_dist = dist + cost

            if new_dist < distance[next_node]:
                distance[next_node] = new_dist

                heappush(pq, (new_dist, next_node))

    return distance

T = int(input())
for tc in range(1, T+1):

    # N : 집 개수, M 개의 줄 , X : 목표 집
    N, M, X = map(int, input().split())
    load = [[] for _ in range(N+1)]
    r_load = [[] for _ in range(N+1)]
    
    
    for _ in range(M): 
        x,y,c = map(int, input().split())

        load[x].append((y,c))
        r_load[y].append((x,c))


    back = dijkstra(X, load)
    go = dijkstra(X, r_load)
    answer = 0

    for i in range(1, N+1):
        answer = max(answer, (back[i]+go[i]))


    print(f'#{tc} {answer}')