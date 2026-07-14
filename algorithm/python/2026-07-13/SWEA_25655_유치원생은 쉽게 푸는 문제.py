# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 1, 0, 0, 0, 1, 0, 1, 0, 2, 1

T = int(input())

for tc in range(1, T + 1):
    X = int(input())

    if X == 1:
        answer = '0'

    elif X % 2 == 0:
        # X가 짝수이면 8을 X // 2개 사용
        answer = '8' * (X // 2)

    else:
        # X가 홀수이면 4로 구멍 1개를 만들고,
        # 나머지는 8로 구멍 2개씩 만듦
        answer = '4' + '8' * (X // 2)

    print(answer)