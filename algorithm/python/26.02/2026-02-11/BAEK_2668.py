import sys
input = sys.stdin.readline

'''
1번째 줄에서 뽑은 애들의 밑에 있는 애들이랑 구성이 같아야 함
1 2 3 4 5 6 7
3 1 1 5 5 4 6
1-3, 3-1, 5-5 이렇게 구성해야지 [1,3,5] 집합 가능
'''

'''
dfs로 싸이클 찾기
'''

def dfs(x):
    
    # 방문 처리
    visited[x] = 1
    # 현재 사이클 처리
    cycle[x] = 1
    
    # 현재 인덱스에 해당하는 애가 같은지
    nx = nums[x]

    # 1. 다음 노드가 방문 안했으면 계속 따라감
    if visited[nx] == 0:
        dfs(nx)

    # 2. 방문했으면 사이클인지 보기
    else:
        if cycle[nx] == 1:
            #  nx부터 다시 따라가며 사이클에 포함된 노드를 전부 picked로 표시
            cur = nx

            # cur을 계속 이동시키며 사이클 한 바퀴를 돌 때까지 picked 처리
            while True:
                # cur은 사이클에 속하므로 뽑힐 수 있는 숫자
                picked[cur] = 1

                # cur -> a[cur]
                cur = nums[cur]

                # 다시 nx로 돌아오면 사이클 표시 끝
                if cur == nx:
                    break

    # 현재 경로에서 제
    cycle[x] = 0 


N = int(input())
nums = [0] * (N+1)

for i in range(1,N + 1):
    nums[i] = int(input())

# 방문했는지
visited = [0] * (N+1)
# 현재 사이클 안인지
cycle = [0] * (N+1)

picked = [0] * (N+1)

for i in range(1,N+1):
    if visited[i] == 0:
        dfs(i)

ans = []
for i in range(1, N + 1):
    if picked[i] == 1:
        ans.append(i)


print(len(ans))

for x in ans:
    print(x)