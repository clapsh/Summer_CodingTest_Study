from collections import deque
import math

n,m = map(int, input().split())
removelist = list(map(int, input().split()))
# 회전하는 큐 생성
lst = []
for i in range(1, n+1):
    lst.append(i)

que = deque(lst)
cnt = 0
length = len(que)
halfIdx = math.ceil(length/2)

while len(removelist):
    # 1번연산 뽑으려는 수와 첫번째 요소가 일치하는 경우
    if que[0] == removelist[0]:
        removelist.pop(0)
        que.popleft()
        length -= 1
        halfIdx = math.ceil(length/2)
        continue

    # 뽑으려는 수가 절반 + 1 전에 있는 경우 2번연산
    idx = que.index(int(removelist[0]))
    if idx < halfIdx:
        que.rotate(-1)
        cnt += 1
        
    else:
        que.rotate(1)
        cnt += 1

print(cnt)
        



    
