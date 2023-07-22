n = int(input())
class_time = []
for i in range(n):
    class_time.append(list(map(int,input().split())))

# 회의가 끝나는 시간을 기준으로 정렬
# 시작시간이/
'''
2
9 9
1 9
처럼 입력되는 경우 종료시간만을 기준으로 정렬하면 
[[9, 9], [1, 9]] 이렇게 돼서 1은 [9,9]의 종료시간인 9보다 작으므로 최대 회의의 개수가 1이되어버린다.
[ [1, 9], [9, 9]] 와 같이 되어야하므로 시작시간을 기준으로 먼저 정렬하고 
종료시간을 기준으로 다시 정렬해야 한다. 
'''

class_time.sort(key=lambda class_time: class_time[0])
class_time.sort(key=lambda class_time: class_time[1])

# 1. 다음 회의의 시작시간이 현재 회의의 종료시간보다 크거나 같은 경우
# 카운트를 늘려준다.
# 2. 다음 회의의 시작시간이 현재 회의의 종료시간보다 작을 경우
# 다음 회의로 넘어간다.
count = 0
cur_finish = 0
for ct in class_time:
    if ct[0] >= cur_finish:
        count += 1
        cur_finish = ct[1]
    else:
        continue
    
print(count)