# 전체쪽수 P, A가 찾는 번호, B가 찾는 번호
# 먼저 찾는 사람이 이김, 비기면 0

T = int(input())

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    def binary_search(target):
        left = 1
        right = P
        count = 0

        while left <= right:
            middle = (left + right) // 2
            count += 1

            if middle == target:
                return count

            elif middle < target:
                # 목표 페이지가 가운데보다 오른쪽에 있음
                left = middle

            else:
                # 목표 페이지가 가운데보다 왼쪽에 있음
                right = middle

    a_count = binary_search(A)
    b_count = binary_search(B)

    if a_count < b_count:
        answer = "A"
    elif a_count > b_count:
        answer = "B"
    else:
        answer = 0

    print(f"#{tc} {answer}")