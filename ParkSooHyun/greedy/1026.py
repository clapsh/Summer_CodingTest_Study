n = input()
#데이터 공백으로 구분하여 입력받기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#a는 오름차순 정렬 
a.sort()
# b 내림 차순 정렬
b.sort(reverse=True)

res = 0
for i in range(int(n)):
    res += (a[i]*b[i])
    
print(res)