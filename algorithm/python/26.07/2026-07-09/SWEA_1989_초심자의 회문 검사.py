T = int(input())
for tc in range(1, T+1):
    word = list(input())
    isPalindrome = 1

    left = 0
    right = len(word) - 1

    # left가 right보다 작을 때 동안 반복!
    while left < right:
        # 만약 회문이면
        if word[left] == word[right]:
            left += 1
            right -= 1
        
        else:
            isPalindrome = 0
            break
    
    print(f"#{tc} {isPalindrome}")