# 상, 하 , 좌, 우, 앞, 뒤    
dy = [-3, +3, 0 , 0, -1 , +1]
dx = [0, 0 , -1, +1 , 0 , 0 ]
def dfs(nodeX, nodeY):
    for i in range(6):      
        x = nodeX + dx[i]
        y = nodeY + dy[i]
        if x < m and x >= 0 and y < n*h and y >= 0:
             # 토마토가 0인 경우
            if tomato[y][x] == 0 and not visited[y][x]:
                tomato[y][x] = tomato[nodeY][nodeX] +1
                dfs(x,y)


# m, n , h입력 받기
m,n,h = map(int, input().split())
# 토마토 입력값
tomato = [[] for _ in range(n*h)]
visited = [[False]*m for _ in range(n*h)]
strX = -1
strY = -1
for i in range(n*h):
    tomato[i] = list(map(int, input().split()))
for x in range(n*h):
    for y in tomato[x]:
        if y == 1 :
            strX = y
            strY = x
            break
    if strX != -1 and strY != -1:
        break
dfs(strX, strY)
print(tomato)



depth = 0

    