T = int(input())

for _ in range(T):
    tc = int(input())
    scores = list(map(int, input().split()))

    # 0점부터 100점까지 등장 횟수 저장
    count = [0] * 101

    for score in scores:
        count[score] += 1

    answer = 0

    # 작은 점수부터 확인하면서 같아도 갱신
    for score in range(101):
        if count[score] >= count[answer]:
            answer = score

    print(f"#{tc} {answer}")