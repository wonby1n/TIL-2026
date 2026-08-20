from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

'''
큐에 넣었다가 빼는 건가?
'''

result = []

q = deque()
for i in range(1, N+1):
    q.append(i)

while q:
    for _ in range(K-1):
        q.append(q.popleft())

    result.append(q.popleft())


# print("<", end='')
# for i in range(0, len(result)):
#     print(result[i], end = '')
#     if i != len(result) - 1:
#         print(", ", end='')
# print(">", end='')

print("<" + ", ".join(map(str, result)) + ">")