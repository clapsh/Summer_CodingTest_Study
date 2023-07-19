gear = [list(map(int, input())) for _ in range(4)]
n = int(input())
# (1,3) (2,4)끼리 같은 방향으로 회전
dirc = [1, -1 ,1,-1] 
isSpin = [0,0,0,0]

for _ in range(n):
    tNum , tDir = map(int, input().split())
    isSpin = [0,0,0,0]
    #isSpin 구하기
    isSpin[tNum-1] = 1
    #tNum 전의 톱니바퀴인 경우 
    inc = 1
    while True:
        idx = (tNum-1)+inc
        # 종료조건
        if idx >= 4:
            break
        # 톱니바퀴의 3번째, 7번째 극이 다르면 isSpin = true
        if gear[idx-1][2] + gear[idx][6] == 1:
            isSpin[idx] = 1
        #다른경우 isSpin = false
        else:
            break
        inc += 1
    #tNum 전의 톱니바퀴인 경우        
    inc = 1
    #print('isspin1',isSpin)
    while True:
        idx = (tNum-1)-inc
        # 종료조건
        if idx < 0:
            break
        # 톱니바퀴의 3번째, 7번째 극이 다르면 isSpin = true
        if gear[idx][2] + gear[idx+1][6] == 1:
            isSpin[idx] = 1
        #다른경우 isSpin = false
        else:
            break
        inc += 1
    #print('isspin2',isSpin)
    
    
    for i in range(4):
        if isSpin[i]:
            #돌리는 톱니바퀴와 같은 방향으로 회전하는 경우
            if dirc[i] * dirc[tNum-1] == 1:
                #시계방향인경우
                if tDir == 1:
                    temp = gear[i][7]
                    del gear[i][7]
                    gear[i].insert(0,temp)
                #반시계방향인 경우:
                else:
                    temp = gear[i][0]
                    del gear[i][0]
                    gear[i].append(temp)
            #돌리는 톱니바퀴와 다른 방향으로 회전하는 경우 
            else:
                #시계방향인경우
                if tDir == 1:
                    temp = gear[i][0]
                    del gear[i][0]
                    gear[i].append(temp)
                #반시계방향인 경우:
                else:
                    temp = gear[i][7]
                    del gear[i][7]
                    gear[i].insert(0,temp)
        
res = 0
mul = 1
for i in range(4):
        res += mul*pow(2,i)*gear[i][0]    
print(res)