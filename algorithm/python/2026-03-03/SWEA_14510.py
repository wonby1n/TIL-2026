def min_days(target):
    # target까지 되려면 커야 하는 높이들
    diffs = [target - h for h in heights]
    # 모든 나무가 target에 도달하기 위한 총 성장량 합
    total_v = sum(diffs)

    if total_v == 0:
        return 0

    # 홀수 날이 반드시 필요한 횟수
    need1 = sum(d % 2 for d in diffs)

    low = 0
    high = 10**18

    # 최댓값으로 답 정해두고 갱신
    answer = high

    while low <= high:
        mid = (low + high) // 2

        a = (mid + 1) // 2
        b = (mid) // 2

        if a >= need1 and (a + 2*b) >= total_v:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 나무들의 높이
    heights = list(map(int, input().split()))
    
    max_h = max(heights)

    res1 = min_days(max_h)

    res2 = min_days(max_h+1)

    result = min(res1, res2)

    print(f'#{tc} {result}')