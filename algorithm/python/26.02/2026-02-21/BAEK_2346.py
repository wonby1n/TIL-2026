'''
BAEK_2346_풍선 터뜨리기
풍선이 원형으로 놓여 있음
제일 처음 1번 풍선을 터뜨리고, 안에 있는 종이에 적힌 풍선을 터뜨림
양수면 오른쪽, 음수는 왼쪽
이동할 때 이미 터진 풍선은 제외

deque.rotate() 사용하기 : 덱을 원형으로 회전시키는 메서드

dq = deque([1,2,3,4,5])
dq.rotate(1) 오른쪽 1칸
결과: [5,1,2,3,4]

dq.rotate(-2) 왼쪽 2칸
결과: [3,4,5,1,2]
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
moves = list(map(int, input().split()))

# (풍선번호, 이동값) 저장
dq = deque()
i = 1
while i <= N:
    dq.append((i, moves[i - 1]))
    i += 1

answer = []

while dq:
    # 1) 맨 앞 풍선 터뜨리기
    num, k = dq.popleft()
    answer.append(num)

    # 2) 더 터뜨릴 풍선이 없으면 종료
    if not dq:
        break

    # 3) 이동
    if k > 0:
        # 오른쪽으로 k칸 -> 이미 다음 풍선은 맨 앞이 됐으니 (k-1)만 추가로 이동
        dq.rotate(-(k - 1))
    else:
        # 왼쪽으로 |k|칸
        dq.rotate(-k)

# 출력
print(*answer)