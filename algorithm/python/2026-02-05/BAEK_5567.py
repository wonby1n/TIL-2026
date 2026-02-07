import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n + 1) 
q = deque()

dist[1] = 0
q.append(1)

while q:
    now = q.popleft()

    if dist[now] == 2:
        continue

    for nxt in graph[now]:
        if dist[nxt] == -1:
            dist[nxt] = dist[now] + 1
            q.append(nxt)

result = 0
for i in range(2, n + 1):
    if dist[i] == 1 or dist[i] == 2:
        result += 1

print(result)