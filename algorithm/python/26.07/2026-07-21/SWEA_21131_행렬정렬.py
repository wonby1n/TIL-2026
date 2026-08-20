# 1 이상 N이하의 정수 x를 고른다
# 1행 ~ x행, 1열 ~ x열에 해당하는 x*x크기의 부분행렬을 전치(transpose)시킨다.
# 그러면, 모든 1<= i,j <=x에 대해, A[i,j]는 기존A[j,i]의 값으로 바뀐다.

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    # 지금까지 전치가 홀수번 적용됐는지 확인
    is_transposed = False

    # 오른쪽 끝부터 확인
    for i in range(N - 1, -1, -1):

        if not is_transposed:
            # 전치되지 않은 상태라면 첫 번째 행의 값을 확인
            current = square[0][i]
        else:
            # 전치된 상태라면 첫 번째 열의 값이 위쪽으로 올라옴
            current = square[i][0]

        # 정답 행렬의 [0][i]에는 i + 1이 있어야 함
        if current != i + 1:
            answer += 1
            is_transposed = not is_transposed

    print(answer)