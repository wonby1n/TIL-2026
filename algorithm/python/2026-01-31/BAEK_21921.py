import sys
input = sys.stdin.readline

N, X = map(int, input().split())
blog = list(map(int, input().split()))

'''
max_sum = 0
count = 0

이중 for문?
for i in range(0, N - X + 1):
    s = 0

    for j in range(i, i + X):
        s += blog[j]

    if s > max_sum:
        max_sum = s
        count = 1
    elif s == max_sum:
        count += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)

시간초과 .. ㅜㅜ
'''

# 슬라이딩 윈도우 사용
window_sum = 0

for i in range(0, X):
    window_sum += blog[i]

max_sum = window_sum
count = 1

# 한 칸씩 오른쪽으로 밀기
for i in range(X, N):
    window_sum += blog[i] 
    window_sum -= blog[i - X]  

    if window_sum > max_sum:
        max_sum = window_sum
        count = 1
    elif window_sum == max_sum:
        count += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)