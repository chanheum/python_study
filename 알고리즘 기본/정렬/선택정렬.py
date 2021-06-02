array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i   # 가장 작은 원소의 인덱스 (가장 앞쪽 원소가 최솟값)
    for j in range(i + 1, len(array)):
        # 가장 작은 수의 인덱스를 얻어옴
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]