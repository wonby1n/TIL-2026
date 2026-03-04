from collections import deque

def bfs(start, g):
    visited = [0] * (N+1)
    q = deque()

    visited[start] = 1
    q.append(start)

    cnt = 0

    while q:
        now = q.popleft()

        for nxt in g[now]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                q.append(nxt)
                cnt += 1

    return cnt


N, M = map(int, input().split())

# 큰놈 작은놈 따로 저장
bgraph = [[] for _ in range(N+1)]
sgraph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    bgraph[a].append(b)
    sgraph[b].append(a)

answer = 0

for i in range(1, N+1):
    taller = bfs(i, bgraph)
    smaller = bfs(i, sgraph)

    if taller + smaller == N - 1:
        answer += 1

print(answer)
