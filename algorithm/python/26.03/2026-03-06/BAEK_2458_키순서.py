from collections import deque

N, M = map(int, input().split())

# 큰 놈 작은 놈 구분해서 저장
bgraph = [[] for _ in range(N+1)]
sgraph = [[] for _ in range(N+1)]

for _ in range(1, N+1):
    a, b = map(int, input().split())
    bgraph[a].append(b)
    sgraph[b].append(a)

def bfs(start, g):
    visited = [0] * (N+1)
    q = deque()

    q.append(start)
    visited[start] = 1

    cnt = 0 

    while q:
        now = q.popleft()

        for nxt in g[now]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                q.append(nxt)
                cnt +=1

    return cnt

answer = 0

for i in range(1, N+1):
    res1 = bfs(i, bgraph)
    res2 = bfs(i, sgraph)

    if res1 + res2 == N - 1:
        answer += 1

print(answer)