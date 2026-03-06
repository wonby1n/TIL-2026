from collections import deque
from itertools import combinations

N = int(input())
people = [0] + list(map(int, input().split()))

graph = [[] for _ in range(1, N+1)]
for i in range(1, N+1):
    
    data = list(map(int, input().split()))
    # 총 갯수는 걍 버림
    graph[i] = data[1:]

def is_connected(team_set):
    if not team_set:
        return False
    
    start = next(iter(team_set))

    q = deque([start])
    visited = set([start])

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if (nxt in team_set) and (nxt not in visited):
                q.append(nxt)
                visited.add(nxt)
    
    return len(team_set) == len(visited)


INF = 10 ** 18
answer = INF

all_nodes = list(range(1, N+1))
all_set = set(all_nodes)


for k in range(1, N+1):
    for comb in combinations(is_connected, k):
        A = set(comb)
        B = all_set - A

        if not is_connected(A):
            continue
        if not is_connected(B):
            continue

        sumA = 0
        sumB = 0

        for x in A:
            sumA += people[x]
        for x in B:
            sumB += people[x]

        diff = abs(sumA - sumB)

        if diff < answer:
            answer = diff

if answer == INF:
    print(-1)
else:
    print(answer)