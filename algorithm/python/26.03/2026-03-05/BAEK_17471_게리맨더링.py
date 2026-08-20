from collections import deque
from itertools import combinations

N = int(input())
people = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
for i in range(1, N +1):
    data = list(map(int, input().split()))
    graph[i] = data[1:]

def is_connected(team_set):
    if not team_set:
        return False
    
    start = next(iter(team_set))

    q = deque([start])
    visited = set([start])
    
    while q:
        now = q.popleft

        for nxt in graph[now]:
            if nxt in team_set and nxt not in visited:
                visited.add(nxt)
                q.append(nxt)

    return len(visited) == len(team_set)

INF = 10 ** 18
answer = INF

# A팀, B팀을 구하기 위해서
all_nodes = list(range(1, N+1))
all_set = set(all_nodes)

for k in range(1, N):
    for comb in combinations(all_nodes, k):
        A = set(comb)
        B = all_set-A

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

        diff = abs(sumB-sumA)

        if diff < answer:
            answer = diff

if answer == INF:
    print(-1)
else:
    print(answer)