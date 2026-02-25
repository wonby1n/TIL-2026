'''
BAEK_1463_1로 만들기
X % 3 == 0 이면 3으로 나누기
X % 2 == 0 이면 2로 나누기
아니면 1을 빼기
연산의 최솟값을 구하라
N = 10
2로 나누면 : 10 -> 5 -> 4 -> 2 -> 1 (3번)
1 빼서 3의 배수 만들면 : 10 -> 9 -> 3 -> 1 (3번)
하.. dp로 해야되네..
'''
import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

dp = [0] * (N + 1)

# dp[1]은 늘 0

for i in range(2, N + 1):
    # 1을 빼는 경우를 기본값으로
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])