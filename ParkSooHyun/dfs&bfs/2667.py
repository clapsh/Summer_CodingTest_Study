from collections import deque
# 상 하 좌 우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# bfs
def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    # 방문 여부 체크
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

# 그래프 입력
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
# 단지 내 집 개수 세기
cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

#단지 정렬 후 출력
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])