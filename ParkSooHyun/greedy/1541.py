data = list(map(str,input().split('-')))
res = 0
for index,d in enumerate(data):
    sum_data = list(map(int, d.split('+')))
    sum_res = 0
    for s in sum_data:
        sum_res += s
    if index == 0:
        res += sum_res
    else:
        res -= sum_res
        
print (res)