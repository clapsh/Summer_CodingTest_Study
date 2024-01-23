n = int(input()) # n<= 20
L = list(map(int, input().split())) # 체력
J = list(map(int, input().split())) # 기쁨
L, J = [0]+L , [0]+J

dp = [[0 for _ in range(101)] for _ in range (n+1)]

for i in range (1, n+1):
    for j in range (1, 101):
        if L[i] <= j: #체력이 있을 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]]+J[i]) # 이전 행의 체력과 이전 행의 체력에서 L[i], J[i] 값을 계산한 값을 비교
        else: # 체력이 없을 경우 이전 행이 최댓값이기 때문
            dp[i][j] = dp[i-1][j]

print(dp[n][99]) #체력의 최댓값

# 배낭문제