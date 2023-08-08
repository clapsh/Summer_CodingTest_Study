def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0:
            dfs(nx)

n=int(input())
v=int(input()) 
# 그래프 
graph = [[] for i in range(n+1)] 
# 방문여부 표시
visited=[0]*(n+1) 

# 양방향 그래프
for i in range(v):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a) 

dfs(1)
print(sum(visited)-1)