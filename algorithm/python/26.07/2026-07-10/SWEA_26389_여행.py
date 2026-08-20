# 세준이는 무한한 이차원 평면에 살며.. 집은 원점 (0,0)
# i번째 날에는 동서남북 중 A[i]의 방향으로 양의 정수 거리만큼 이동
# N번째 날에는 이동을 끝낸 순간 집으로 돌아와야 함
# 문자열 A는 네 개의 문자 ‘N’, ‘W’, ‘S’, ‘E’ 
# 이는 각각 ‘북쪽’, ‘서쪽’, ‘남쪽’, ‘동쪽’

# 간단하게 생각해서, 위로 갔으면 밑으로 가고, 오른쪽으로 가면 왼쪽으로 가기만 하면 되는 거 아닌가?

T = int(input())
for tc in range(1, T+1):
    word = list(input())
    
    north = 0
    east = 0
    west = 0
    south = 0

    for w in range(len(word)):
        if word[w] == 'N':
            north +=1
        if word[w] == 'E':
            east +=1
        if word[w] == 'W':
            west +=1
        if word[w] == 'S':
            south +=1
    
    # 숫자가 똑같으면 될듯?
    # if (north == south) and (east == west):
    #     print('Yes')
    # else:
    #     print('No')

    # 생각해보니까 계속 왼쪽으로 갔다가 마지막에 오른쪽에 가기만 하면 집에 돌아갈 수 있구나
    # 방향 중 하나만 있으면 안 됨

    if (north == 0) != (south == 0) or (east == 0) != (west == 0):
        print('No')
    else:
        print('Yes')