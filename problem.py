person_min = 2
person_max = 10
person_total = 100
memo = {}

def problem(remain, sitted):
    key = str([remain, sitted])
    # 종료 조건
    if key in memo:
        return memo[key]
    if remain < 0:
        return 0        # 무효하니 0 리턴
    if remain == 0:
        return 1        # 유효하니 수를 세면 돼서 1을 리턴

    # 재귀처리
    count = 0
    for i in range(sitted, person_max + 1):
        count += problem(remain - i, i)

    # 메모화 처리
    memo[key] = count
    # 종료
    return count

print(problem(person_total, person_min))