def dfs(node, length):
    global answer

    answer = max(answer, length)

    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, length + 1)
            visited[next_node] = False


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    answer = 1

    for start in range(1, N + 1):
        visited = [False] * (N + 1)
        visited[start] = True
        dfs(start, 1)

    print(f"#{tc} {answer}")