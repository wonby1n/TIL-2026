'''
서로 다른 N개의 자연수의 합 = S
N의 최댓값은?
반복문으로 작은 숫자부터 더해가면 됨
'''

import sys

input = sys.stdin.readline

S = int(input())

total_sum = 0
cnt = 0

for i in range(1, S + 1):
    total_sum += i

    if total_sum > S:
        break

    cnt += 1

print(cnt)