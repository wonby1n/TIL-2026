T = 10

for tc in range(1, T + 1):
    N = int(input())
    word = input().strip()

    stack = []
    result = 1

    pairs = {
        ')': '(',
        '}': '{',
        ']': '[',
        '>': '<'
    }

    for char in word:
        # 여는 괄호라면 저장
        if char in '({[<':
            stack.append(char)

        # 닫는 괄호라면 짝 확인
        else:
            # 여는 괄호가 없거나 짝이 다르면 유효하지 않음
            if not stack or stack[-1] != pairs[char]:
                result = 0
                break

            stack.pop()

    # 여는 괄호가 남아 있어도 유효하지 않음
    if stack:
        result = 0

    print(f'#{tc} {result}')