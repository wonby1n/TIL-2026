def min_days(target):
    diffs = [target - h for h in heights]
    total_v = sum(diffs)
    if total_v == 0:
        return 0
    
    need1 = (d % 2 for d in diffs)
    
    low = 0
    high = 10**18

    answer = high

    while low<=high:
        mid = (low + high) // 2
        
        a = (mid + 1) // 2
        b = mid // 2

        if a >= need1 and (a+2*b) >= total_v:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heights = list(map(int, input().split()))

    # 제일 큰 나무
    max_h = max(heights)

    res1 = min_days(max_h)
    res2 = min_days(max_h+1)

    result = min(res1, res2)