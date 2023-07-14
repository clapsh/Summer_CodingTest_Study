#거스름돈
#5, 2

money=int(input())
count=0

while True:
    if money%5==0:
        money-=5
        count+=1
    else:
        money-=2
        count+=1
    if money<=0:
        break
if money<0: #나눠지지 않아도 count 증가함!
    print(-1)
else:
    print(count)
