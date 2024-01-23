def dfs(node):
    for n in graph[node]:
        #방문하지 않은 경우
        if check[n] == 0:
             check[n] = check[node] + 1
             dfs(n)

# 전체 사람 수
n = int(input())
# 촌수를 구해야하는 사람 
fst, sec = map(int,input().split())
# 그래프 (양방향) (인덱스 == 사람 번호)
graph = [[] for _ in range(n+1)]
m = int(input())
for _ in range(m):
    u , v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 길이 탐색
check = [0]*(n+1)
dfs(fst)

print(check[sec] if check[sec] else -1)