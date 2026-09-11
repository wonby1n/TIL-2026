def inorder(t):
    if t > N:
        return
    inorder(t * 2) # 왼쪽
    print(tree[t], end ='')
    inorder(t * 2 + 1) # 오른쪽

T = 10
    
for tc in range(1, 11):
    N = int(input())
    tree = [''] * (N + 1)

    for _ in range(N):
        data = input().split()

        node = int(data[0])
        tree[node] = data[1]

    print(f'#{tc}', end = ' ')
    inorder(1)
    print()