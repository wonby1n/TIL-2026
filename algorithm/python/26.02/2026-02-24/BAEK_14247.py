'''
BAEK_14247_나무 자르기
하루에 한 나무씩 N일 산에 오르면서 나무를 자를 예정
나무들이 밤만 되면 다른 속도로 자람
자른 이후에도 나무는 0부터 다시 자람
같은 나무를 여러번 자를 수 있음
성장률이 제일 큰 나무만 자르는 게 낫지 않나?
나무1: H1=1, A1=1
나무2: H2=2, A2=5

0일차 아침: 나무2 높이 = 2 → 얻음 2, 나무2=0
0일차 밤: 나무1=1+1=2, 나무2=0+5=5
1일차 아침: 나무2 높이 = 5 → 얻음 5
총합 = 2 + 5 = 7

0일차 아침: 나무1 높이 = 1 → 얻음 1, 나무1=0
0일차 밤: 나무1=0+1=1, 나무2=2+5=7
1일차 아침: 나무2 높이 = 7 → 얻음 7
총합 = 1 + 7 = 8

성장량이 작은 나무 먼저 자르고
성장량이 큰 나무를 뒤에 자르기
'''
import sys
input = sys.stdin.readline


N = int(input())
# 길이
length = list(map(int, input().split()))
# 성장
speed = list(map(int, input().split()))

trees = []
for i in range(N):
    trees.append((speed[i], length[i]))

# 성장량에 따라서 정렬
trees.sort()

answer = 0
for day in range(N):
    a, b = trees[day]
    answer += b + a * day

print(answer)