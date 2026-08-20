'''
BAEK_17471_게리맨더링
'''

from collections import deque
from itertools import combinations


N = int(input())
people = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    graph[i] = data[1:]

def is_connected(team_set):
    # 팀이 비어있으면 바로 false 반환
    if not team_set:
        return False

    # team_set에서 아무거나 꺼내서 시작점으로 잡음
    start = next(iter(team_set))

    q = deque([start])
    visited = set([start])

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if (nxt in team_set) and (nxt not in visited):
                visited.add(nxt)
                q.append(nxt)

    # 방문한 구역 수가 팀 크기와 같으면 한 덩어리(연결)
    return len(visited) == len(team_set)


INF = 10**18
answer = INF

# A팀, B팀 을 구하기 위해서
all_nodes = list(range(1, N+1))
all_set = set(all_nodes)

for k in range(1, N):
    # A팀 크기를 1명(구역 1개)부터 N-1개까지 바꿔가며 시도
    for comb in combinations(all_nodes, k):
        A = set(comb)
        B = all_set - A

        if not is_connected(A):
            continue
        if not is_connected(B):
            continue

        sumA = 0
        sumB = 0
        
        # 팀에 속한 구역들의 인구수 더하기
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