graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 방문했는지 방문하지 않았는지 표시해놓기 위한 리스트 변수
visited = [False] * 9

def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        # 방문하지 않은 지점을 방문하는 방식
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)