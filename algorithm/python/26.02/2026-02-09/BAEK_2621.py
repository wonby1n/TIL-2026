import sys
input = sys.stdin.readline

numbers = []
colors = set()

for _ in range(5):
    c, n = input().split()
    colors.add(c)
    numbers.append(int(n))

numbers.sort()
max_num = numbers[4]

# 1) 같은 색
is_flush = (len(colors) == 1)

# 2) 연속 체크
is_straight = True
for i in range(4):
    if numbers[i] + 1 != numbers[i + 1]:
        is_straight = False
        break

# 3) 숫자 개수 세기
cnt = {}
for x in numbers:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1

# 4) 등장횟수 패턴 만들기
freq = []
for k in cnt:
    freq.append(cnt[k])
freq.sort()

# 규칙 1
if is_flush and is_straight:
    result = 900 + max_num

# 규칙 2
elif freq == [1, 4]:
    four = 0
    for k in cnt:
        if cnt[k] == 4:
            four = k
            break
    result = 800 + four

# 규칙 3
elif freq == [2, 3]:
    three = 0
    two = 0
    for k in cnt:
        if cnt[k] == 3:
            three = k
        elif cnt[k] == 2:
            two = k
    result = 700 + three * 10 + two

# 규칙 4
elif is_flush:
    result = 600 + max_num

# 규칙 5
elif is_straight:
    result = 500 + max_num

# 규칙 6
elif freq == [1, 1, 3]:
    three = 0
    for k in cnt:
        if cnt[k] == 3:
            three = k
            break
    result = 400 + three

# 규칙 7
elif freq == [1, 2, 2]:
    pair = []
    for k in cnt:
        if cnt[k] == 2:
            pair.append(k)
    pair.sort()
    result = 300 + pair[1] * 10 + pair[0]

# 규칙 8
elif freq == [1, 1, 1, 2]:
    two = 0
    for k in cnt:
        if cnt[k] == 2:
            two = k
            break
    result = 200 + two

# 규칙 9
else:
    result = 100 + max_num

print(result)
