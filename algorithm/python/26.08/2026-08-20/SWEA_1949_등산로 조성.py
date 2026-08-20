def dfs(r, c, height, length, used):
    global answer

    answer = max(answer, length)

    for dr, dc in dir:
        nr = r + dr
        nc = c + dc

        # 범위를 벗어나거나 이미 방문했으면
        if not (0 <= nr < N and 0 <= nc < N):
            continue

        if visited[nr][nc]:
            continue

        next_h = mountain[nr][nc]

        # 다음 칸이 더 낮으면 패스
        if next_h < height:
            visited[nr][nc] = True
            dfs(nr, nc, next_h, length + 1, used)
            visited[nr][nc] = False

        # 아직 공사 안했으면
        elif not used:
            # 최대 K만큼 깎았을 때 현재 높이보다 낮아질 수 있는지 확인
            if next_h - K < height:
                visited[nr][nc] = True

                # 현재 높이보다 딱 1만큼 낮게 깎는 것이 가장 유리
                dfs(nr, nc, height - 1, length + 1, True)

                visited[nr][nc] = False


T = int(input())

dir = [(-1,0), (1,0), (0,-1), (0,1)]

for tc in range(1, T+1):
    N, K = map(int, input().split())

    mountain = [list(map(int, input().split()))for _ in range(N)]

    # 가장 높은 봉우리는?
    max_h = max(map(max, mountain))

    answer = 0
    visited = [[False] * N for _ in range(N)]

    # 가장 높은 봉우리 찾기
    for r in range(N):
        for c in range(N):
            if mountain[r][c] == max_h:
                visited[r][c] = True
                dfs(r,c, max_h, 1, False)
                visited[r][c] = False


    print(f'#{tc} {answer}')