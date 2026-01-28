import sys
input = sys.stdin.readline

N = int(input())

top = list(map(int, input().split()))

# 레이저 발사는 왼쪽으로

# 내가 발사한 레이저를 받은 탑의 번호 (1번부터 시작) 출력
# 내 레이저를 수신한 탑이 없으면 0 출력

result = [0] * N
stack = [] # (index, height)


for i in range(N):
    # 현재 탑보다 낮은 탑들은 레이저를 막아줄 수 없어서 제거
    while stack and stack[-1][1] < top[i]:
        stack.pop()


    # 남아있으면 가장 가까운 왼쪽의 높은 탑
    if stack:
        result[i] = stack[-1][0] + 1


    # 현재 탑을 후보로 넣기
    stack.append((i, top[i]))


print(*result)