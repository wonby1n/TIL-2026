import sys
from collections import deque
input = sys.stdin.readline


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def choco(box):
    visited = [[0]*3 for _ in range(3)]
    groups = []

    for r in range(3):
        for c in range(3):

            if box[r][c] != 'O':
                continue
            if visited[r][c] == 1:
                continue

            q = deque()
            q.append((r, c))
            visited[r][c] = 1
            cnt = 1

            while q:
                cr, cc = q.popleft()

                for dr, dc in delta:
                    nr = cr + dr
                    nc = cc + dc
                    
                    if 0 <= nr < 3 and 0 <= nc < 3:
                        if visited[nr][nc] == 0 and box[nr][nc] == 'O':
                            visited[nr][nc] = 1
                            q.append((nr, nc))
                            cnt += 1

            groups.append(cnt)
    
    groups.sort()
    return groups

T = int(input())
for tc in range(1, T+1):
    box = []
    for _ in range(3):
        a = input().strip()
        box.append(list(a))
    
    # 화면(-)에 표시된 숫자의 개수 / 숫자의 목록
    a = list(map(int, input().split()))
    n = a[0]
    nums = a[1:]
    nums.sort()

    groups = choco(box)

    if len(nums) != n:
        print(0)
    else:
        if groups == nums:
            print(1)
        else:
            print(0)