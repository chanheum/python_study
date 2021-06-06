N, K = map(int, input().split(' '))

num_1 = list(map(int, input().split(' ')))
num_2 = list(map(int, input().split(' ')))

def max_swap(K):
    # K회 바꿔치기 수행
    for i in range(K):
        # 각 리스트 별 최솟값을 저장
        n_min_1 = min(num_1)
        n_max_2 = max(num_2)

        for num in range(N):
            # 가장 작은 값이 있는 곳을 탐색
            if num_1[num] == n_min_1:
                min_index_1 = num
            # 가장 큰 값이 있는 곳을 탐색
            if num_2[num] == n_max_2:
                max_index_2 = num
        # 스와프 수행
        num_1[min_index_1], num_2[max_index_2] = num_2[max_index_2], num_1[min_index_1]

    # 최종 스와프가 완료된 배열1의 원소의 합 리턴
    return (sum(num_1))

print(max_swap(K))