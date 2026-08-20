# 어떻게 차례대로 할 수 잇는 거징
# 이거 파이썬은 왜 안되죠????????!!!!!!!!!!!!!!

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]

    stack = []

    