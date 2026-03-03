from collections import deque

N, M = map(int, input().split())

# 큰 학생들, 작은 학생들 목록 따로 받기
bgraph = [[] for _ in range(N+1)]
sgraph = [[] for _ in range(N+1)]

for _ in range(1, N+1):
    a, b = map(int, input().split())
    sgraph[a].append(b)
    bgraph[b].append(a)

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

answer = 0

for i in range(1, N+1):
    taller = bfs(i, bgraph)
    shorter = bfs(i, sgraph)

    if taller + shorter == N - 1:
        answer += 1

print(answer)