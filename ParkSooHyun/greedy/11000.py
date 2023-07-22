#강의실 배정 
import sys
n = int(sys.stdin.readline())
# 강의실 시간 input 받아오기
time = []
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    time.append(data)
    
#si <= ti를 적용하기 위해 si(시작시간) 순으로 오름차순 정렬

minimum = 0

# 강의가 끝나는 시간
finish = [0,]
for t in time:
    s = t[0] # 시작 시간
    o = t[1] # 끝나는 시간
    #minimum = min(finish)
    if s >= minimum :        
        finish.remove(minimum)
        finish.append(o)
        #if (len(finish) == 1) or (o < minimum):
        minimum = o
    else:
        if o < minimum:
            minimum = o
        finish.append(o)
   
    #finish.sort()

print(len(finish))
