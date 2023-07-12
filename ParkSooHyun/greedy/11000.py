#강의실 배정 
n = input()
# 강의실 시간 input 받아오기
time = []
for i in range(int(n)):
    data = list(map(int, input().split()))
    time.append(data)
    
#si <= ti를 적용하기 위해 si(시작시간) 순으로 오름차순 정렬
time.sort(key=lambda t:t[0])
# 강의가 끝나는 시간
finish = [0,]
res = 0
for t in time:
    s = t[0]
    o = t[1]
    for idx,f in enumerate(finish):
        if s >= f : 
            finish[idx] = o
            finish.sort()
            break
        else:
            finish.append(o)
            break

print(len(finish))
