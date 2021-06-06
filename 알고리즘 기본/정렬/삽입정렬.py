array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    # j : 확인하고자 하는 순서 
    for j in range(i, 0 , -1):      # 인덱스 i부터 1씩 감소하며 반복 (위치 i부터 위치 array[1]까지 확인)
        if array[j] < array[j-1]:   # 한 칸씩 왼쪽으로 이동하면서 좌측 요소랑 크기 비교
            array[j], array[j-1] = array[j-1], array[j]
        else:                       # 자기보다 작은 데이터를 만나면 그대로 둠
            break

print(array)
