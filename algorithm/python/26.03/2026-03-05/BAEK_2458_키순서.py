import sys
input = sys.stdin.readline
from collections import deque

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
                

N, M = map(int, input().split())

# 큰 놈 작은 놈 따로 저장
bgraph = [[] for _ in range(N+1)]
sgraph = [[] for _ in range(N+1)]

for _ in range(1, N+1):
    a, b = map(int, input().split())
    bgraph[a].append(b)
    sgraph[b].append(a)

answer = 0

for i in range(1, N+1):
    taller = bfs(i, bgraph)
    shorter = bfs(i, sgraph)

    if taller + shorter == N - 1:
        answer += 1

print(answer)