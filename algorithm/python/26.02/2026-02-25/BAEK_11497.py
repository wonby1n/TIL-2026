'''
BAEK_11497_통나무 건너뛰기
N개의 통나무를 원형으로 세워 놓고 뛰어놀기
[2, 4, 5, 7, 9]
얘네들을 자유롭게 배치해보자
난이도 = 인접한 두 통나무 간의 높이의 차의 최댓값
주의해야 할 점은 맨 처음 통나무랑 맨 마지막 통나무도 인접해있기 때문에 그 차이도 생각을 해야 한다
하나씩 보면서 자리 바꾸기?
지그재그로 배치하면 차이가 적게 난다
2
2 4
2 5 4
2 5 7 4
2 5 9 7 4

'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    namu = list(map(int, input().split()))

    # 일단 순서대로 세우기
    namu.sort()

    answer = 0

    i = 0
    while i <= N - 3:
        now = namu[i+2] - namu[i]
        if now > answer:
            answer = now
        i += 1
    
    print(answer)