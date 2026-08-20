for _ in range(10):
    tc, edge = map(int, input().split())
    data = list(map(int, input().split()))

    graph = [[] for _ in range(100)]

    for i in range(edge):
        start = data[i * 2]
        end = data[i * 2 + 1]
        graph[start].append(end)

    visited = [False] * 100
    stack = [0]
    visited[0] = True

    answer = 0

    while stack:
        current = stack.pop()

        # 99번에 도착하면 길 존재
        if current == 99:
            answer = 1
            break

        for next_node in graph[current]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)

    print(f"#{tc} {answer}")