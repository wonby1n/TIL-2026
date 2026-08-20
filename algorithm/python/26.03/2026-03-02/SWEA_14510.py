'''
SWEA_14510_나무 높이
나무가 여러 개 있어.
모든 나무를 제일 큰 나무 높이(또는 그보다 1 더 큰 높이)까지 키우고 싶어.
근데 물 주는 규칙이 특이해:
1일차: 물 주면 +1
2일차: 물 주면 +2
3일차: 물 주면 +1
4일차: 물 주면 +2
… 이런 식으로 반복

그리고 하루에 딱 1그루만 물 줄 수 있어.
(아무 것도 안 하는 날도 가능)

목표는: 최소 며칠 만에 다 맞추기
'''
# target : 목표 높이
def min_days(target):
    # 추가로 커야 하는 높이
    diffs = [target - h for h in heights]
    
    # 홀수 날(+1)이 반드시 필요한 횟수
    need1 = sum(d % 2 for d in diffs)

    # 모든 나무가 target에 도달하기 위해 필요한 "총 성장량 합"
    total_v = sum(diffs)

    # 이미 모든 나무가 target에 도달했으면
    if total_v == 0:
        return 0
    
    # 일수의 최솟값 최댓값 정해놓기
    low = 0
    high = 10**19

    answer = high
    # target에 맞출 수 있는 최소 날짜 답을 저장할 변수(초기값은 큰 값)

    while low <= high:
        mid = (low + high) // 2
        # mid일 안에 target 달성 가능?을 검사할 현재 날짜 후보

        a = (mid + 1) // 2
        # a: mid일 동안 존재하는 홀수날 개수 (= +1을 줄 수 있는 날의 최대 횟수)
        # 예) mid=5일이면 (1,3,5) -> a=3

        b = mid // 2
        # b: mid일 동안 존재하는 짝수날 개수 (= +2를 줄 수 있는 날의 최대 횟수)
        # 예) mid=5일이면 (2,4) -> b=2

        # 조건 1) +1이 반드시 필요한 횟수(need1)만큼 홀수날(a)이 충분한가?
        # 조건 2) mid일 동안 만들 수 있는 최대 성장량이 총 필요 성장량(total_v) 이상인가?
        if a >= need1 and (a + 2 * b) >= total_v:
            answer = mid        # mid일로 가능하니까 답 후보 갱신
            high = mid - 1   # 더 작은 일수로도 가능한지 왼쪽(작은 범위) 탐색
        else:
            low = mid + 1    # mid일로 불가능하면 더 큰 일수로 오른쪽 탐색

    return answer

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    heights = list(map(int, input().split()))

    # 현재 나무 중 제일 큰 높이
    max_h = max(heights)

    res1 = min_days(max_h)
    # (패턴이 +1/+2 번갈아라서, 가끔 1 더 키우는 게 더 빨라지는 경우가 있음)
    res2 = min_days(max_h + 1)

    result = min(res1, res2)

    print(f'#{tc} {result}')