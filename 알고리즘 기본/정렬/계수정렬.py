array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트를 선언!! (단, 모든 값은 0으로 초기화)
count = [0 for i in range(max(array) + 1)]

# 각 데이터에 해당하는 인덱스의 값을 증가
for data in array:
    count[data] += 1

# 리스트에 기록된 정렬 정보 확인
for i in range(len(count)):
    for num in range(count[i]):
        print(i, end=' ')   # 띄어씌기를 구분으로 등장한 횟수만큼 인덱스 출력