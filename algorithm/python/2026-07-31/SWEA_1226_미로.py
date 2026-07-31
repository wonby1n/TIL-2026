def miro_start(sr, sc):
    stack = [(sr, sc)]
    visited = [[False] * 16 for _ in range(16)]
    visited[sr][sc] = True

    # 상, 하, 좌, 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while stack:
        r, c = stack.pop()

        # 도착점 발견
        if miro[r][c] == 3:
            return 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if (
                0 <= nr < 16
                and 0 <= nc < 16
                and miro[nr][nc] != 1
                and not visited[nr][nc]
            ):
                visited[nr][nc] = True
                stack.append((nr, nc))

    # 도착점까지 갈 수 없음
    return 0

T = 10

for tc in range(1, T + 1):
    t = int(input())
    miro = [list(map(int, input().strip())) for _ in range(16)]

    for r in range(16):
        for c in range(16):
            if miro[r][c] == 2:
                sr, sc = r, c

    result = miro_start(sr, sc)

    print(f'#{t} {result}')