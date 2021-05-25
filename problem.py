person_min = 2      # 구분할 수 있는 최소 인원
person_max = 10     # 구분할 수 있는 최대 인원
person_total = 100  # 최대 인원
memo = {}           # 메모화 변수

# 전체 x명 중 y명씩 앉는 모든 경우의 수를 구하는 함수
def problem(x, y):
    key = str([x, y]) # remain명 중에 sitted명이 앉는 경우의 수 메모화

    if key in memo:
        return memo[key]
    if x < 0:
        return 0
    if x == 0:
        return 1

    # 재귀 처리
    count = 0
    for i in range(y, person_max + 1):
        # i명씩 앉을 때의 모든 경우의 수 구하기
        count += problem(x - i, i)

    memo[key] = count

    return count

print(problem(person_total, person_min))
print(memo)
