def dfs(idx, result):
    global max_result, min_result

    # 모든 숫자를 사용한 경우
    if idx == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    # 0: +, 1: -, 2: *, 3: /
    for op in range(4):
        if operators[op] == 0:
            continue

        operators[op] -= 1

        if op == 0:
            dfs(idx + 1, result + numbers[idx])

        elif op == 1:
            dfs(idx + 1, result - numbers[idx])

        elif op == 2:
            dfs(idx + 1, result * numbers[idx])

        else:
            # int()를 사용하면 음수도 0을 향해 버림
            dfs(idx + 1, int(result / numbers[idx]))

        # 사용한 연산자 복구
        operators[op] += 1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # +, -, *, /의 개수
    operators = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    max_result = -float('inf')
    min_result = float('inf')

    # 첫 번째 숫자는 이미 계산 결과에 넣어둠
    dfs(1, numbers[0])

    print(f'#{tc} {max_result - min_result}')